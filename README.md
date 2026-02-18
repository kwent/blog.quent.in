# blog.quent.in

Personal blog powered by [Hugo](https://gohugo.io/) with the [Hugo Narrow](https://github.com/tom2almighty/hugo-narrow) theme.

**Live site:** https://blog.quent.in

## Setup

```bash
mise install
uv sync
```

## Development

```bash
# Start local server on http://localhost:1313
hugo server -D
```

## Writing

```bash
# Create new blog post with AI-generated cover image
uv run scripts/new_post.py "My Post Title" --tags tag1,tag2 --categories dev,web

# Create new post without cover
uv run scripts/new_post.py "My Post Title" --no-cover
```

## Scripts

```bash
# Backfill cover images for posts missing them
uv run scripts/generate_covers.py

# Check for broken links
uv run scripts/check_links.py
```

## Deploy

Deployed automatically via GitHub Actions on push to `master`.
