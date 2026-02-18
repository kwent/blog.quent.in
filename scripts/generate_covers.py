#!/usr/bin/env python3
"""Generate AI cover images for existing Hugo blog posts that don't have one.

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


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def generate_cover_image(client, title: str, tags: list[str]) -> bytes | None:
    from google import genai

    tag_context = f" Related topics: {', '.join(tags)}." if tags else ""
    prompt = (
        f"Create a minimal, modern blog header image for a technical article titled \"{title}\".{tag_context} "
        f"Style: clean gradient background with subtle geometric shapes or abstract tech iconography. "
        f"No text in the image. Aspect ratio 16:9. Soft colors that work well with both light and dark themes."
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-05-20",
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
    parser = argparse.ArgumentParser(description="Backfill AI cover images for existing blog posts")
    parser.add_argument("--dry-run", action="store_true", help="Preview what would be generated without making changes")
    parser.add_argument("--post", default=None, help="Only generate for a specific post slug")
    parser.add_argument("--limit", type=int, default=0, help="Max number of posts to process (0 = all)")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between API calls in seconds (default: 2)")
    args = parser.parse_args()

    if args.dry_run:
        posts = get_posts_missing_covers()
        print(f"Found {len(posts)} posts without cover images:\n")
        for p in posts:
            post = frontmatter.load(p)
            print(f"  - {post['title']} ({p.name})")
        return

    from google import genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    STATIC_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    if args.post:
        # Find specific post by slug
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
            image_data = generate_cover_image(client, title, tags)

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
                print(f"         -> SKIPPED (no image generated)")
                failed += 1

        except Exception as e:
            print(f"         -> FAILED: {e}")
            failed += 1

        if i < total:
            time.sleep(args.delay)

    print(f"\nDone! {success} covers generated, {failed} failed.")


if __name__ == "__main__":
    main()
