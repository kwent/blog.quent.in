# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Octopress 2.0 blog (Ruby-based static site generator built on Jekyll) for blog.quent.in. It uses Sass/Compass for styling, Sinatra for local preview, and Rake for build automation.

## Common Commands

```bash
# Install dependencies
bundle install

# Local development - starts Jekyll, Compass, and Rack server on port 4000
rake preview

# Generate static site
rake generate

# Create new blog post
rake new_post["My Post Title"]

# Create new page
rake new_page["page-name"]

# Watch for changes (no server)
rake watch

# Speed up regeneration by isolating a single post
rake isolate["post-filename"]
rake integrate  # restore all posts

# Clear caches
rake clean

# Deploy (generates and pushes)
rake gen_deploy
```

## Architecture

- **source/**: Blog content and templates
  - `_posts/`: Markdown blog posts with YAML front matter
  - `_layouts/`: HTML layouts (default, post, page)
  - `_includes/`: Reusable template snippets and sidebar widgets
- **sass/**: Sass stylesheets compiled by Compass
- **plugins/**: Ruby plugins extending Jekyll (code blocks, gist embedding, categories, pagination)
- **docs/**: Generated static site output (configured as Jekyll destination)
- **.themes/**: Available themes (OctoPanel installed)

## Key Configuration

- `_config.yml`: Jekyll/Octopress settings, social integrations, permalink structure
- `Rakefile`: All build and deploy tasks
- `config.rb`: Compass CSS compilation settings
- `config.ru`: Rack/Sinatra development server

## Post Format

Posts use YAML front matter:
```yaml
---
layout: post
title: "Post Title"
date: 2024-01-01 12:00:00 -0800
comments: true
categories: [category1, category2]
---
```

## Known Issue

If you get `YAML Exception reading` error, run:
```bash
export LC_ALL=en_US.UTF-8
```
