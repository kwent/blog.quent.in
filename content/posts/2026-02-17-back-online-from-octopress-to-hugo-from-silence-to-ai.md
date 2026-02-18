---
aliases:
- /posts/2026/02/17/back-online-from-octopress-to-hugo-from-silence-to-ai/
categories:
- development
- web
cover: /images/covers/back-online-from-octopress-to-hugo-from-silence-to-ai.png
date: 2026-02-17 23:32:48
slug: back-online-from-octopress-to-hugo-from-silence-to-ai
tags:
- blogging
- hugo
- ai
- llm
- octopress
title: 'Back Online: From Octopress to Hugo, From Silence to AI'
---

My last blog post was in February 2017. Nine years ago.

It wasn't intentional. I didn't wake up one day and decide to stop writing. I just... didn't start the next post. Then a month passed, then a year, then almost a decade. The classic `// TODO: write blog post` that never gets resolved.

## What happened

Life happened — and it was a busy one.

When I wrote that last post about [PgBouncerHero](/blog/2017/02/06/pgbouncerhero-dashboard-for-your-pgbouncers/) in 2017, I was at [Instacart](https://www.instacart.com/) as one of their early SREs, building the infrastructure that took the platform from thousands of orders a week to millions.

After that came [PopSQL](https://popsql.com/) (YC S19). Then in 2021, I co-founded [Rootly](https://rootly.com) (YC S21) with [JJ Tang](https://x.com/jjrichardtang) — an AI-native incident management platform now used by teams at NVIDIA, Squarespace, Canva, and Figma. I've been serving as [CTO & CISO](https://rootly.com), and we've raised [$15.2M](https://rootly.com/blog/rootly-raises-12-million-from-renegade-partners-google-gradient-ventures-xyz-ventures) from Renegade Partners, Google Gradient Ventures, and XYZ Ventures.

So I wasn't idle. I just wasn't writing.

Part of it was simply not having the bandwidth. But part of it was friction: the blog ran on [Octopress 2.0](https://github.com/imathis/octopress), which itself ran on Jekyll 0.12 and Ruby 2.7. Every time I thought about writing, I'd first think about the `bundle install` that would inevitably fail, the outdated gems, the Rakefile I'd have to debug. When you spend your days firefighting production incidents for a living, the last thing you want is to debug your own blog's build system.

So the blog sat there. Gathering dust. Still serving pages from a `docs/` folder committed to the repo like it was 2012.

## What changed

LLMs.

Not as a topic to write about (though there's plenty to say), but as a way to work. The thing that brought this blog back to life wasn't inspiration — it was capability.

I'd been wanting to migrate off Octopress for years. The checklist was long and tedious — converting posts, cleaning up legacy HTML, fixing broken links, setting up a new theme, configuring deployment. The kind of work that's not hard, just endless. And that's exactly why it never got done.

With [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models) as a collaborator that didn't mind the tedious parts, together we:

- **Migrated 31 posts** from Octopress (Jekyll + Liquid) to Hugo with clean Markdown
- **Converted legacy HTML** to proper Markdown in 17 older posts that were full of raw `<div>` tags
- **Set up [Hugo Narrow](https://github.com/tom2almighty/hugo-narrow)** with the Dracula color scheme and dark/light mode
- **Built Python tooling** for creating new posts with AI-generated cover images
- **Added CI/CD** with GitHub Actions — linting, link checking, Hugo builds, automated deployment
- **Generated cover art** for every post using [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash)'s image generation
- **Cleaned up everything** — removed 166 unused WordPress thumbnails, normalized image paths, upgraded links to HTTPS, losslessly compressed all images

Work that would have taken weeks of evenings — done through conversation.

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

The way I write code today looks nothing like 2017. At Rootly, we've been building AI into our product from the start — AI SRE agents, automated postmortems, intelligent incident routing. I pair with AI models daily. I build things in hours that would have taken weeks. And I have *opinions* about all of it — about what works, what doesn't, what people get wrong about AI-assisted development.

Nine years of not writing means nine years of accumulated things to say.

## On writing in a language that isn't yours

There's another reason I stopped writing that I haven't mentioned yet: English isn't my first language. I'm French. And while I can debug a production outage in English at 3am without thinking twice, writing a blog post always felt different. There's a self-consciousness that kicks in — am I using the right word, does this sentence sound natural, is this idiom actually a thing?

That friction was real, and LLMs removed it entirely. I can think in my own way, express what I mean, and let the model handle the prose. My intent, my ideas, my experience — just sharper prose and no second-guessing.

And honestly, I plan to keep writing this way. Every future post on this blog will likely be prompted and shaped through an LLM. Which raises a question I find genuinely interesting: does it matter?

If you're reading this through an AI-powered feed reader or summarizer — and statistically, some of you are — then it's already agent-to-agent. I write with an AI, you read with an AI. The ideas still travel from my brain to yours.

It's a question of time before this is just how content works. I'd rather be transparent about it now than pretend otherwise.

## What's next

I don't know the cadence yet, and I won't promise a schedule I won't keep. But I want to write about the things I deal with daily — how we use AI in incident management at Rootly, the reality of AI-assisted development beyond the hype, infrastructure patterns that actually scale, and the lessons from nearly five years of building a startup.

The blog is alive, the stack is modern, and the friction is gone. That's enough to start.

If you've read any of my old posts — about [PgBouncerHero](/blog/2017/02/06/pgbouncerhero-dashboard-for-your-pgbouncers/), or [real-time logging with IronWorker](/blog/2014/05/27/real-time-logging-for-ironworker-with-logentries/), or that time I wrote about [backing up Neo4j to S3](/blog/2014/07/11/backup-neo4j-database-to-aws-s3/) — thanks for sticking around. There's more coming.

Welcome back. Let's go.

---

*Written with [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models) via [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Cover images generated by [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash).*