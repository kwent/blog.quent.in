---
aliases:
- /blog/2026/09/24/i-still-love-ruby-i-rarely-write-it/
- /blog/2026/09/24/we-wont-all-put-our-pencils-down-at-once/
- /blog/2026/09/24/writing-code-is-dead-the-people-who-loved-it-are-still-here/
categories:
- development
cover: /images/covers/the-hardest-part-of-ai-coding-has-nothing-to-do-with-code.png
date: 2026-09-24T09:00:00-0700
draft: false
slug: the-hardest-part-of-ai-coding-has-nothing-to-do-with-code
tags:
- ai
- ruby
- rails
- engineering
- code-review
title: The Hardest Part of AI Coding Has Nothing to Do With Code
---

In his [Rails World keynote](https://www.youtube.com/watch?v=vDjW_dRyKXY), DHH said 37signals had put its pencils down. Writing code by hand is now the exception there.

I recognize that change at [Rootly](https://rootly.com). Agents now write much of our production code. Some teammates have embraced the shift completely. Others are hesitant. I've felt both reactions. The hard part is looking after each other while our work changes.

## The nights I loved

In 2015, I added a command line to [syno](https://github.com/kwent/syno), a Node.js wrapper for Synology's DSM API. I wanted to type `syno fs listFiles` and see the files on my NAS, or start a download with `syno dl createTask`. I [wrote up that first CLI](/blog/2015/02/12/simple-node-dot-js-wrapper-and-cli-for-synology-dsm-rest-api/) when it shipped.

That was the kind of project where one broken command could eat a night. Read the API docs, change a few lines, run it again. When it finally worked, I knew exactly why. Huge dopamine hit.

I loved those nights. I felt the same way writing Ruby and Rails. Someone who spent years getting good at that work can reasonably hesitate before handing it to an agent. I still love those tools, even though I write much less Ruby now.

## Ten ideas instead of one bug

The satisfaction hasn't disappeared for me. Earlier this year, I [came back to syno](/blog/2026/02/24/from-maintainers-wanted-to-three-major-releases-in-a-weekend/) after years of letting it sit. With an agent, I rewrote its CoffeeScript codebase in TypeScript, added DSM 7 support and tests, and shipped a new version over a weekend. In 2024, I had pushed a commit that said "Maintainers wanted." Getting that project moving again felt good in a different way.

Now I can try ideas that used to sit untouched on a list. An agent can get one working while I decide what the interaction should feel like, try it, and send it back when it's wrong. I can test ten ideas in the time I might once have spent on one bug. Some aren't worth shipping. Finding that out quickly is useful.

I've found myself making native apps in Rust and Swift. A few years ago, learning another language and maintaining another app would have made many of those experiments easy to dismiss. I still reach for Rails when the web fits. The user experience gets to decide, not my attachment to a framework.

## Speed changes the review

Faster implementation brings a harder question: how do we know what is safe to ship? At Rootly, a mistake in an escalation path can leave someone waiting during an incident. An agent can produce a clean-looking PR that still changes the wrong behavior.

Our [AI review assistant](/blog/2026/05/19/your-small-pr-rule-wont-survive-ai/) flags risky changes, including migrations and core incident workflows, and gives a human reviewer a place to start. We use risk labels, feature flags, scoped rollouts, and rollback plans. A reviewer can ask whether a flag covers the failure path, whether a migration can be reversed, and whether an escalation still reaches the person on call.

## We won't all move at the same speed

On the [linear view of Max Roser's technology timeline](https://ourworldindata.org/technology-long-run), almost every invention familiar to us crowds into the far right edge. Up close, those changes arrived years apart.

[![Linear timeline of technology showing recent inventions crowded at the far right of three million years of history](/images/figures/technology-long-run-linear.png)](/images/figures/technology-long-run-linear.png)

*Chart by [Max Roser, Our World in Data](https://ourworldindata.org/technology-long-run), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Unmodified. See the [full timeline](/images/figures/technology-long-run-spiral.png).*

My parents grew up with typewriters. PCs spread through homes and offices in the 1980s, the web in the 1990s, and smartphones became common in the 2010s. They had decades to adjust, and some changes are still hard for them. At Rootly, years of coding habits have changed in a much shorter span. I understand why an engineer might need time to find their footing.

When a teammate says, "I don't trust this change yet," I want to know what they see. They may know about a background job the agent missed. They may want to watch one rollout before changing their own workflow. We can share the prompts that worked and the failures we caught, then let people try them on real problems.

I want to look after the people who jumped in, too. I've written about staying up for [one more prompt](/blog/2026/03/09/one-more-prompt-the-dopamine-trap-of-agentic-coding/). The engineer excited enough to keep building all night may need a colleague who notices when it's time to close the laptop. A faster tool can make it harder to stop.

Assembly, Ruby, and now English instructions to agents ask us to work at different levels of detail. English can get us to a working first pass quickly, but it leaves plenty of room for misunderstanding. We still need engineers who know what users need, can see a bad assumption, and take responsibility for what reaches production.

I'm grateful I got to spend those nights fixing bugs by hand. I still get excited when an idea finally works for a user. The teammate who says, "Wait, this could break an escalation," is as much a part of that work as the one who started the agent. We won't all put our pencils down at once. We can still build together.
