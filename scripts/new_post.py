#!/usr/bin/env python3
"""Create a new Hugo blog post with an AI-generated cover image.

Usage:
    uv run scripts/new_post.py "My Post Title" --tags tag1,tag2 --categories dev,web
    uv run scripts/new_post.py "My Post Title" --no-cover
    uv run scripts/new_post.py "My Post Title" --cover-prompt "A custom prompt for the image"

Requires:
    export GEMINI_API_KEY=your_key
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

BLOG_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = BLOG_ROOT / "content" / "posts"
STATIC_IMAGES_DIR = BLOG_ROOT / "static" / "images" / "covers"


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def generate_cover_image(title: str, tags: list[str], custom_prompt: str | None = None) -> bytes | None:
    from google import genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        return None

    client = genai.Client(api_key=api_key)

    if custom_prompt:
        prompt = custom_prompt
    else:
        tag_context = f" Related topics: {', '.join(tags)}." if tags else ""
        prompt = (
            f"Create a minimal, modern blog header image for a technical article titled \"{title}\".{tag_context} "
            f"Style: clean gradient background with subtle geometric shapes or abstract tech iconography. "
            f"No text in the image. Aspect ratio 16:9. Soft colors that work well with both light and dark themes."
        )

    print(f"Generating cover image...")
    print(f"Prompt: {prompt[:120]}...")

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

    print("Warning: No image was generated in the response.")
    return None


def create_post(
    title: str,
    tags: list[str] | None = None,
    categories: list[str] | None = None,
    generate_cover: bool = True,
    cover_prompt: str | None = None,
) -> Path:
    tags = tags or []
    categories = categories or []
    slug = slugify(title)
    now = datetime.now()
    date_prefix = now.strftime("%Y-%m-%d")
    date_full = now.strftime("%Y-%m-%dT%H:%M:%S%z") or now.strftime("%Y-%m-%dT%H:%M:%S-0700")

    filename = f"{date_prefix}-{slug}.md"
    filepath = CONTENT_DIR / filename

    if filepath.exists():
        print(f"Error: Post already exists at {filepath}")
        sys.exit(1)

    cover_path = ""
    if generate_cover:
        image_data = generate_cover_image(title, tags, cover_prompt)
        if image_data:
            STATIC_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
            image_filename = f"{slug}.png"
            image_path = STATIC_IMAGES_DIR / image_filename
            image_path.write_bytes(image_data)
            cover_path = f"/images/covers/{image_filename}"
            print(f"Cover image saved to {image_path}")

    front_matter_lines = [
        "---",
        f'title: "{title}"',
        f"date: {date_full}",
    ]

    if cover_path:
        front_matter_lines.append(f"cover: {cover_path}")

    if categories:
        front_matter_lines.append("categories:")
        for cat in categories:
            front_matter_lines.append(f"- {cat.strip().lower()}")

    if tags:
        front_matter_lines.append("tags:")
        for tag in tags:
            front_matter_lines.append(f"- {tag.strip().lower()}")

    front_matter_lines.append(f"slug: {slug}")
    front_matter_lines.append("---")
    front_matter_lines.append("")
    front_matter_lines.append("Write your post content here.")
    front_matter_lines.append("")

    filepath.write_text("\n".join(front_matter_lines))
    print(f"Post created at {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Create a new Hugo blog post with AI-generated cover image")
    parser.add_argument("title", help="The title of the blog post")
    parser.add_argument("--tags", default="", help="Comma-separated tags (e.g. ruby,rails,postgresql)")
    parser.add_argument("--categories", default="", help="Comma-separated categories (e.g. development,web)")
    parser.add_argument("--no-cover", action="store_true", help="Skip AI cover image generation")
    parser.add_argument("--cover-prompt", default=None, help="Custom prompt for cover image generation")
    args = parser.parse_args()

    tags = [t for t in args.tags.split(",") if t.strip()] if args.tags else []
    categories = [c for c in args.categories.split(",") if c.strip()] if args.categories else []

    filepath = create_post(
        title=args.title,
        tags=tags,
        categories=categories,
        generate_cover=not args.no_cover,
        cover_prompt=args.cover_prompt,
    )

    print(f"\nDone! Edit your post at: {filepath}")
    print(f"Preview with: hugo server -D")


if __name__ == "__main__":
    main()
