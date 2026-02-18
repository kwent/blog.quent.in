---
title: "Back Online: From Octopress to Hugo, From Silence to AI"
date: 2026-02-17T23:32:48
categories:
- development
- web
tags:
- blogging
- hugo
- ai
- llm
- octopress
slug: back-online-from-octopress-to-hugo-from-silence-to-ai
---

My last blog post was in February 2017. Nine years ago.

It wasn't intentional. I didn't wake up one day and decide to stop writing. I just... didn't start the next post. Then a month passed, then a year, then almost a decade. The classic `// TODO: write blog post` that never gets resolved.

## What happened

Life happened — and it was a busy one.

When I wrote that last post about [PgBouncerHero](/blog/2017/02/06/pgbouncerhero-dashboard-for-your-pgbouncers/) in 2017, I was deep in the trenches at [Instacart](https://www.instacart.com/) as one of their early SREs, building the infrastructure that took the platform from processing thousands of orders a week to millions. After that, I co-founded [PopSQL](https://popsql.com/) (YC S19), then in 2021 co-founded [Rootly](https://rootly.com) (YC S21) with [JJ Tang](https://x.com/jjrichardtang) — an AI-native incident management platform that helps engineering teams at companies like NVIDIA, Squarespace, Canva, and Figma detect, manage, and resolve incidents faster. I've been serving as CTO & CISO, and we've raised $15.2M from investors including Renegade Partners, Google Gradient Ventures, and XYZ Ventures.

So I wasn't idle. I just wasn't writing.

Part of it was simply not having the bandwidth. But part of it was friction: the blog ran on [Octopress 2.0](https://github.com/imathis/octopress), which itself ran on Jekyll 0.12 and Ruby 2.7. Every time I thought about writing, I'd first think about the `bundle install` that would inevitably fail, the outdated gems, the Rakefile I'd have to debug. When you spend your days firefighting production incidents for a living, the last thing you want is to debug your own blog's build system.

So the blog sat there. Gathering dust. Still serving pages from a `docs/` folder committed to the repo like it was 2012.

## What changed

LLMs.

Not as a topic to write about (though there's plenty to say), but as a way to work. The thing that brought this blog back to life wasn't inspiration — it was capability.

I'd been wanting to migrate off Octopress for years. The checklist was long and tedious: convert 31 posts from Jekyll/Liquid to Hugo, clean up legacy HTML baked into old Markdown files, fix broken links, set up a new theme, configure deployment, handle comment migration. The kind of work that's not hard, just endless — and that's exactly why it never got done.

With [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models) as a collaborator that didn't mind the tedious parts, together we:

- **Migrated 31 posts** from Octopress (Jekyll + Liquid) to Hugo with clean Markdown
- **Converted legacy HTML** to proper Markdown in 17 older posts that were full of raw `<div>` tags
- **Set up [Hugo Narrow](https://github.com/tom2almighty/hugo-narrow)** with the Dracula color scheme and dark/light mode
- **Built Python tooling** for creating new posts with AI-generated cover images
- **Added CI/CD** with GitHub Actions — linting, link checking, Hugo builds, automated deployment
- **Generated cover art** for every post using [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash)'s image generation
- **Cleaned up everything** — removed 166 unused WordPress thumbnails, normalized image paths, upgraded links to HTTPS, losslessly compressed all images

29 commits. A mass of work that would have taken weeks of evenings — done through conversation.

## The stack now

| Before | After |
|--------|-------|
| Octopress 2.0 (Jekyll 0.12) | Hugo 0.155 |
| Ruby 2.7 + Bundler | Hugo + uv (Python scripts) |
| Rake tasks | `hugo server -D` |
| Manual deployment to `docs/` | GitHub Actions → GitHub Pages |
| No cover images | AI-generated covers via Gemini 2.5 Flash |
| Liquid templates | Hugo shortcodes |

The writing workflow is now: run a script, write Markdown, push. No dependency hell. No debugging a static site generator just to preview a draft.

## Why now, really

I'm not going to pretend this is purely about tooling. The tools removed the friction, but the spark is something else.

We're living through the most interesting shift in software engineering since the internet went mainstream. The way I write code today looks nothing like 2017. At Rootly, we've been building AI into our product from the start — AI SRE agents, automated postmortems, intelligent incident routing. I pair with AI models daily. I build things in hours that would have taken weeks. And I have *opinions* about all of it — about what works, what doesn't, what people get wrong about AI-assisted development.

Nine years of not writing means nine years of accumulated things to say.

## What's next

I don't know the cadence yet, and I won't promise a schedule I won't keep. But the blog is alive, the stack is modern, and the friction is gone. That's enough to start.

If you've read any of my old posts — about [PgBouncerHero](/blog/2017/02/06/pgbouncerhero-dashboard-for-your-pgbouncers/), or [real-time logging with IronWorker](/blog/2014/05/27/real-time-logging-for-ironworker-with-logentries/), or that time I wrote about [backing up Neo4j to S3](/blog/2014/07/11/backup-neo4j-database-to-aws-s3/) — thanks for sticking around. There's more coming.

Welcome back. Let's go.

---

*Meta note: this entire post — from outline to final draft — was written in conversation with [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models) via [Claude Code](https://docs.anthropic.com/en/docs/claude-code). The blog migration, the Python tooling, the CI/CD pipeline, and yes, this article itself — all prompted and steered through Claude Code. The cover images were generated by [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash). I prompted, steered, and edited, but the words you just read were produced by AI. That's not a disclaimer — it's the point. This is how I work now, and I think it's worth being transparent about it.*
