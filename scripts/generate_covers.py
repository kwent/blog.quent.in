#!/usr/bin/env python3
"""Generate AI cover images for existing Hugo blog posts that don't have one.

Uses a 2-pass approach:
  Pass 1: Text model reads the full article and produces a focused image brief
  Pass 2: Image model generates the cover from that brief + style directive

Usage:
    uv run scripts/generate_covers.py                    # backfill all posts missing covers
    uv run scripts/generate_covers.py --dry-run          # preview what would be generated
    uv run scripts/generate_covers.py --post "slug"      # generate for a specific post
    uv run scripts/generate_covers.py --limit 5          # only process 5 posts

Requires:
    export GEMINI_API_KEY=your_key
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path

import frontmatter

BLOG_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = BLOG_ROOT / "content" / "posts"
STATIC_IMAGES_DIR = BLOG_ROOT / "static" / "images" / "covers"

# Consistent style directive shared across all cover generations.
# This ensures visual cohesion when backfilling or creating new posts.
# Written as natural language per Nano Banana prompt engineering best practices.
STYLE_DIRECTIVE = (
    "Create the image as a bold, eye-catching illustration in the style of a YouTube thumbnail — "
    "vibrant, high-contrast, and impossible to scroll past. "
    "Use rich saturated colors with strong complementary pairings: "
    "electric blues with hot oranges, deep purples with bright cyans, "
    "vivid teals with warm magentas. "
    "The background should be a dramatic gradient or radial glow "
    "with subtle light rays or bokeh effects "
    "that create depth and energy. "
    "Place a large, bold central icon or visual metaphor that fills most of the frame — "
    "make it pop with a slight glow, drop shadow, or bright outline to give it punch. "
    "The composition should feel dynamic and energetic, like a tech product launch visual. "
    "Think Fireship YouTube thumbnails or Vercel conference graphics. "
    "Do not include any text, letters, words, labels, or watermarks anywhere in the image. "
    "Keep it as an illustration — no photorealism or stock photo aesthetics. "
    "The final image should be in 16:9 landscape aspect ratio at 1792x1024 pixels."
)

# Pass 1 system prompt: instruct the text model to produce an image brief.
SUMMARIZER_PROMPT = (
    "You are an art director creating cover image briefs for a tech blog. "
    "Read the article below and produce a short image brief (2-3 sentences max) that describes "
    "a single abstract visual metaphor for this article. "
    "Focus on one iconic symbol or scene that captures the core concept. "
    "Be specific about the metaphor — describe what the central object looks like, "
    "its shape, and any small supporting elements around it. "
    "Do NOT suggest any text, letters, or words in the image. "
    "Do NOT describe colors or style — just the subject and composition.\n\n"
    'Example output: "A large magnifying glass hovering over a grid of tiny database cylinders, '
    'with thin connection lines radiating outward like a spider web."'
)


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def strip_markdown(content: str) -> str:
    """Strip markdown formatting to get plain text for the summarizer."""
    text = content
    text = re.sub(r"```[\s\S]*?```", "", text)  # code blocks
    text = re.sub(r"`[^`]+`", "", text)  # inline code
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", text)  # images
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # inline links
    text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", r"\1", text)  # reference links
    text = re.sub(r"^\[\d+\]:.*$", "", text, flags=re.MULTILINE)  # link defs
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)  # headings
    text = re.sub(r"[*_]{1,3}", "", text)  # bold/italic
    text = re.sub(r"\n{3,}", "\n\n", text)  # excess newlines
    return text.strip()


def pass1_summarize(client, title: str, tags: list[str], content: str) -> str:
    """Pass 1: Use text model to read the article and produce a focused image brief."""
    plain_content = strip_markdown(content)
    # Truncate to ~2000 chars to stay within reasonable token limits
    if len(plain_content) > 2000:
        plain_content = plain_content[:2000] + "..."

    tag_str = f"Tags: {', '.join(tags)}" if tags else ""

    user_prompt = f"Title: {title}\n{tag_str}\n\nArticle content:\n{plain_content}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {"role": "user", "parts": [{"text": f"{SUMMARIZER_PROMPT}\n\n{user_prompt}"}]},
        ],
    )

    return response.text.strip()


def pass2_generate_image(client, title: str, image_brief: str) -> bytes | None:
    """Pass 2: Generate the cover image from the brief + style directive."""
    from google import genai

    prompt = (
        f'I need a cover image for a technical blog post titled "{title}".\n\n'
        f"Image concept: {image_brief}\n\n"
        f"{STYLE_DIRECTIVE}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt],
        config=genai.types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data and part.inline_data.mime_type.startswith("image/"):
            return part.inline_data.data

    return None


def get_posts_missing_covers() -> list[Path]:
    posts = []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        post = frontmatter.load(path)
        if not post.get("cover"):
            posts.append(path)
    return posts


def main():
    parser = argparse.ArgumentParser(
        description="Backfill AI cover images for existing blog posts",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    parser.add_argument("--post", default=None, help="Specific post slug")
    parser.add_argument("--limit", type=int, default=0, help="Max posts (0=all)")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay in seconds")
    parser.add_argument("--show-prompt", action="store_true", help="Print image brief")
    args = parser.parse_args()

    from google import genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    if args.dry_run:
        posts = get_posts_missing_covers()
        print(f"Found {len(posts)} posts without cover images:\n")
        for p in posts:
            post = frontmatter.load(p)
            title = post.get("title", "Untitled")
            tags = post.get("tags", []) or []
            print(f"  - {title} ({p.name})")
            if args.show_prompt:
                brief = pass1_summarize(client, title, tags, post.content)
                print(f"    Brief: {brief}\n")
        return

    STATIC_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    if args.post:
        matches = [p for p in CONTENT_DIR.glob("*.md") if args.post in p.name]
        if not matches:
            print(f"Error: No post found matching '{args.post}'")
            sys.exit(1)
        posts_to_process = matches[:1]
    else:
        posts_to_process = get_posts_missing_covers()

    if args.limit > 0:
        posts_to_process = posts_to_process[: args.limit]

    total = len(posts_to_process)
    print(f"Processing {total} posts...\n")

    success = 0
    failed = 0

    for i, path in enumerate(posts_to_process, 1):
        post = frontmatter.load(path)
        title = post.get("title", "Untitled")
        tags = post.get("tags", []) or []
        slug = post.get("slug") or slugify(title)

        print(f"[{i}/{total}] {title}")

        try:
            # Pass 1: Summarize article into image brief
            brief = pass1_summarize(client, title, tags, post.content)
            print(f"         Brief: {brief[:120]}...")

            # Pass 2: Generate image from brief
            image_data = pass2_generate_image(client, title, brief)

            if image_data:
                image_filename = f"{slug}.png"
                image_path = STATIC_IMAGES_DIR / image_filename
                image_path.write_bytes(image_data)

                cover_path = f"/images/covers/{image_filename}"
                post["cover"] = cover_path
                frontmatter.dump(post, path)

                print(f"         -> {cover_path}")
                success += 1
            else:
                print("         -> SKIPPED (no image generated)")
                failed += 1

        except Exception as e:
            print(f"         -> FAILED: {e}")
            failed += 1

        if i < total:
            time.sleep(args.delay)

    print(f"\nDone! {success} covers generated, {failed} failed.")


if __name__ == "__main__":
    main()
