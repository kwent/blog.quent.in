# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hugo blog for blog.quent.in using the [Hugo Narrow](https://github.com/tom2almighty/hugo-narrow) theme (Tailwind CSS 4.0) with Dracula color scheme. Deployed via GitHub Actions to GitHub Pages.

## Tools

- **Hugo** - Static site generator
- **uv** - Python package manager (for scripts)
- **mise** - Tool version manager (`mise.toml`)

## Common Commands

```bash
# Install tools
mise install

# Install Python dependencies
uv sync

# Local development - starts Hugo server on port 1313
hugo server -D

# Generate static site
hugo

# Create new blog post with AI-generated cover image
uv run scripts/new_post.py "My Post Title" --tags tag1,tag2 --categories dev,web

# Create new post without cover image
uv run scripts/new_post.py "My Post Title" --no-cover

# Create new post with custom cover image prompt
uv run scripts/new_post.py "My Post Title" --cover-prompt "A futuristic cityscape"

# Backfill cover images for all posts missing them
uv run scripts/generate_covers.py

# Backfill dry run (preview what would be generated)
uv run scripts/generate_covers.py --dry-run

# Backfill a specific post
uv run scripts/generate_covers.py --post "slug-name"

# Backfill with limit
uv run scripts/generate_covers.py --limit 5

# Check for broken links (internal + external)
uv run scripts/check_links.py

# Check only internal links
uv run scripts/check_links.py --internal-only

# Check only external links
uv run scripts/check_links.py --external-only

# Check a specific post
uv run scripts/check_links.py --post "slug-name"
```

## Architecture

- **content/posts/**: Markdown blog posts with YAML front matter
- **layouts/**: Custom template overrides (header, Disqus)
- **static/images/**: Static images (avatar, covers)
- **config/_default/**: Hugo YAML configuration
  - `hugo.yaml` - Main Hugo config
  - `params.yaml` - Theme parameters, author info, comments
  - `menus.yaml` - Navigation and social links
- **themes/hugo-narrow/**: Theme (git submodule)
- **scripts/**: Python utility scripts

## Post Format

Posts use YAML front matter:
```yaml
---
title: "Post Title"
date: 2024-01-01T12:00:00-0800
cover: /images/covers/post-slug.png
categories:
- development
tags:
- ruby
- rails
slug: post-slug
---
```

## Cover Image Generation

Scripts use the Gemini API to generate cover images. Requires `GEMINI_API_KEY` environment variable.

- `scripts/new_post.py` - Create new post with auto-generated cover
- `scripts/generate_covers.py` - Backfill covers for existing posts
- `scripts/check_links.py` - Detect broken internal and external links
