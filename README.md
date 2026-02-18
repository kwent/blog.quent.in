# blog.quent.in

Personal blog powered by [Octopress](http://octopress.org/) with the OctoPanel theme.

**Live site:** https://blog.quent.in

## Setup

```bash
bundle install
```

## Development

```bash
# Start local server on http://localhost:4000
rake preview

# Generate static site
rake generate

# Watch for changes (no server)
rake watch
```

## Writing

```bash
# Create new blog post
rake new_post["My Post Title"]

# Create new page
rake new_page["page-name"]

# Speed up regeneration by isolating a single post
rake isolate["post-filename"]
rake integrate  # restore all posts
```

## Deploy

```bash
rake gen_deploy
```

## Troubleshooting

If you get `YAML Exception reading` error:

```bash
export LC_ALL=en_US.UTF-8
```

See: https://github.com/jekyll/jekyll/issues/836
