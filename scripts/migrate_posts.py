#!/usr/bin/env python3
"""
Migration script: Octopress to Hugo
Converts posts from source/_posts/*.markdown to content/posts/*.md
"""

import os
import re
import html
from pathlib import Path
from datetime import datetime
import yaml

# Paths
SOURCE_DIR = Path("source/_posts")
DEST_DIR = Path("content/posts")

# HTML entities to clean
HTML_ENTITIES = {
    "&rsquo;": "'",
    "&lsquo;": "'",
    "&rdquo;": '"',
    "&ldquo;": '"',
    "&ndash;": "-",
    "&mdash;": "--",
    "&hellip;": "...",
    "&amp;": "&",
    "&nbsp;": " ",
    "&#8211;": "-",
    "&#8212;": "--",
    "&#8216;": "'",
    "&#8217;": "'",
    "&#8220;": '"',
    "&#8221;": '"',
    "&#8230;": "...",
}


def clean_html_entities(text):
    """Replace HTML entities with their character equivalents."""
    for entity, char in HTML_ENTITIES.items():
        text = text.replace(entity, char)
    # Also decode any remaining numeric entities
    text = html.unescape(text)
    return text


def parse_date(date_str):
    """Parse various date formats and return ISO 8601 format."""
    if not date_str:
        return None

    date_str = str(date_str).strip()

    # Try various formats
    formats = [
        "%Y-%m-%d %H:%M:%S %z",      # 2017-02-06 10:00:00 -0700
        "%Y-%m-%d %H:%M:%S",          # 2017-02-06 10:00:00
        "%a, %d %b %Y %H:%M:%S",      # Sat, 07 Apr 2012 10:13:44
        "%Y-%m-%d",                    # 2017-02-06
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            # Return in Hugo-compatible format
            if dt.tzinfo:
                return dt.strftime("%Y-%m-%dT%H:%M:%S%z")
            else:
                return dt.strftime("%Y-%m-%dT%H:%M:%S")
        except ValueError:
            continue

    # If no format matches, return as-is
    print(f"  Warning: Could not parse date '{date_str}'")
    return date_str


def extract_slug_from_filename(filename):
    """Extract slug from Octopress filename format: YYYY-MM-DD-slug.markdown"""
    match = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.markdown$", filename)
    if match:
        return match.group(1)
    return filename.replace(".markdown", "")


def convert_vimeo_tags(content):
    """Convert {% vimeo ID WIDTH HEIGHT %} to Hugo shortcode."""
    pattern = r'\{%\s*vimeo\s+(\d+)(?:\s+\d+)?(?:\s+\d+)?\s*%\}'
    return re.sub(pattern, r'{{< vimeo \1 >}}', content)


def convert_youtube_tags(content):
    """Convert {% youtube ID %} to Hugo shortcode."""
    pattern = r'\{%\s*youtube\s+([^\s%]+)\s*%\}'
    return re.sub(pattern, r'{{< youtube \1 >}}', content)


def process_categories_tags(items):
    """Lowercase and deduplicate categories/tags."""
    if not items:
        return []
    if isinstance(items, str):
        items = [items]
    return list(dict.fromkeys([item.lower() for item in items]))


def migrate_post(source_path):
    """Migrate a single post from Octopress to Hugo format."""
    print(f"Processing: {source_path.name}")

    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split front matter and content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            front_matter_str = parts[1]
            body = parts[2]
        else:
            print(f"  Warning: Could not parse front matter")
            return None
    else:
        print(f"  Warning: No front matter found")
        return None

    # Parse YAML front matter
    try:
        front_matter = yaml.safe_load(front_matter_str)
    except yaml.YAMLError as e:
        print(f"  Error parsing YAML: {e}")
        return None

    if not front_matter:
        front_matter = {}

    # Build new front matter
    new_fm = {}

    # Title - clean HTML entities
    title = front_matter.get("title", "")
    new_fm["title"] = clean_html_entities(str(title))

    # Date - standardize format
    date = front_matter.get("date")
    if date:
        new_fm["date"] = parse_date(date)

    # Author
    author = front_matter.get("author")
    if author:
        new_fm["author"] = author

    # Draft status
    if front_matter.get("published") == False:
        new_fm["draft"] = True

    # Categories and tags - merge and lowercase
    categories = process_categories_tags(front_matter.get("categories", []))
    tags = process_categories_tags(front_matter.get("tags", []))

    if categories:
        new_fm["categories"] = categories
    if tags:
        new_fm["tags"] = tags

    # WordPress legacy URL alias
    permalink = front_matter.get("permalink")
    if permalink and "/index.php/" in permalink:
        new_fm["aliases"] = [permalink]

    # Preserve Disqus thread ID for potential comment migration
    dsq_thread_id = front_matter.get("dsq_thread_id")
    if dsq_thread_id:
        if isinstance(dsq_thread_id, list):
            dsq_thread_id = dsq_thread_id[0] if dsq_thread_id else None
        if dsq_thread_id:
            new_fm["disqus_identifier"] = str(dsq_thread_id)

    # Slug from filename
    slug = extract_slug_from_filename(source_path.name)
    new_fm["slug"] = slug

    # Convert content
    body = clean_html_entities(body)
    body = convert_vimeo_tags(body)
    body = convert_youtube_tags(body)

    # Build output
    output = "---\n"
    output += yaml.dump(new_fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
    output += "---"
    output += body

    return output


def main():
    """Main migration function."""
    print("Starting Octopress to Hugo migration...")
    print(f"Source: {SOURCE_DIR}")
    print(f"Destination: {DEST_DIR}")
    print()

    # Create destination directory
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # Get all posts
    posts = sorted(SOURCE_DIR.glob("*.markdown"))
    print(f"Found {len(posts)} posts to migrate\n")

    migrated = 0
    failed = 0

    for source_path in posts:
        result = migrate_post(source_path)

        if result:
            # Output filename: same as input but with .md extension
            dest_filename = source_path.name.replace(".markdown", ".md")
            dest_path = DEST_DIR / dest_filename

            with open(dest_path, "w", encoding="utf-8") as f:
                f.write(result)

            print(f"  -> {dest_path}")
            migrated += 1
        else:
            failed += 1
        print()

    print(f"Migration complete: {migrated} posts migrated, {failed} failed")


if __name__ == "__main__":
    main()
