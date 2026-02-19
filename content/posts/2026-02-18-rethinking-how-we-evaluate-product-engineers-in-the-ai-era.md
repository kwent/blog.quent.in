---
aliases:
- /posts/2026/02/18/rethinking-how-we-evaluate-product-engineers-in-the-ai-era/
categories:
- engineering
- leadership
cover: /images/covers/rethinking-how-we-evaluate-product-engineers-in-the-ai-era.png
date: 2026-02-18 12:24:08
slug: rethinking-how-we-evaluate-product-engineers-in-the-ai-era
tags:
- ai
- engineering
- product-engineering
- hiring
- leadership
title: Rethinking How We Evaluate Product Engineers in the AI Era
---

Over the past few years as CTO at [Rootly](https://rootly.com), I've had to fundamentally rethink how we evaluate product engineers. The skills that used to separate great candidates from good ones have shifted — not because the bar is lower, but because AI has changed what "doing the work" actually looks like.

## What we used to look for

Before AI-assisted coding became mainstream, our take-home evaluation leaned heavily on the code itself. We'd look for:

- **Common pitfalls** — Did the candidate handle edge cases? Did they avoid obvious anti-patterns? Were there SQL N+1 queries, missing error handling, or security oversights?
- **Going beyond the requirements** — Did they just meet the spec, or did they push further? Maybe they added input validation we didn't ask for, wrote tests, or thought about accessibility.
- **Code quality as signal** — Naming conventions, file structure, separation of concerns. The code was the primary artifact, and we read it line by line.

The code told us a story about how someone thinks. And for a long time, that was enough.

## What changed

AI didn't lower the bar — it moved it.

When candidates have access to tools like Claude Code, Cursor, or Copilot, the raw code output stops being the main differentiator. Someone with solid prompting skills can produce code that's clean, well-structured, and passes tests — regardless of their seniority level.

So if the code alone doesn't tell the full story anymore, what does?

**How someone works with AI is now as revealing as the code they produce.**

This is where the shift happened for us. We started caring less about whether someone wrote every line themselves and more about:

- **Decision-making and tradeoffs** — Why did they choose this architecture? What did they consider and reject? Can they articulate why they went with approach A over approach B?
- **Editing and taste** — Did they blindly accept AI output, or did they shape it? Did they refactor what the AI gave them? Did they spot when the AI was wrong?
- **Systems thinking** — Do they understand how the pieces fit together, or are they just stitching together generated snippets?
- **Behavioral signals** — When they hit a wall, did they change approach or just re-prompt the same thing 15 times? How did they break down the problem?

## A concrete example: how our submission instructions evolved

For context, our take-home challenge asks candidates to build a simplified version of Rootly's core workflow — a Ruby on Rails app with a Slack bot for managing incidents and a Web UI to view them. It's intentionally open-ended: we give the basic requirements but leave room for candidates to make product and design decisions on their own.

Here's a real before-and-after from our submission instructions that illustrates the shift.

**Before:** two deliverables — code and a Loom.

> - Share a private GitHub repo with a clear README and instructions on how to run your app
> - Record a Loom demo of what you've built:
>   - Show the Slack bot and Web UI, and talk through your design and your decision making
>   - Show the code paths, how it works, and talking through your design and decision making

**After:** three deliverables — code, **AI transcripts**, and a Loom.

> 1. **GitHub Repo** — Share a private repo with a clear README and instructions on how to run your app.
> 2. **AI Transcripts** — Include your AI session transcripts in the repo. This helps us understand how you work with AI.
> 3. **Loom Demo** (under 5 minutes) — Walk us through what you built:
>    - Demo the Slack bot and Web UI end-to-end.
>    - Show key code paths and talk through your design decisions and tradeoffs.

Notice what changed: **AI transcripts went from not existing to being the second deliverable** — right between the code and the demo. Not buried in a footnote. Not an optional "nice to have." It's a first-class submission artifact because, frankly, it tells us more about how someone engineers than the code itself does.

We also explicitly tell candidates in the challenge notes: *"Using AI is expected and strongly encouraged."* We're not testing whether they can code without AI — we're testing whether they can build great software *with* it.

## Why AI transcripts matter

Reading someone's AI transcript is like watching them think out loud. You learn more from it than you might expect:

- **Problem decomposition** — Did they break the problem into clear steps, or did they dump the entire spec into a prompt and hope for the best?
- **Course correction** — When the AI went in the wrong direction, how quickly did they catch it? Did they course-correct with precision, or did they start over?
- **Domain understanding** — Do their prompts show they understand what they're building, or are they just relaying instructions they don't fully grasp?
- **Iteration quality** — Are they refining and improving, or are they stuck in a loop?

A candidate who produces great code but whose transcript shows they didn't understand what the AI was doing is a very different signal from someone whose transcript shows deliberate, thoughtful collaboration with AI.

To give a concrete example: we recently reviewed two submissions that were remarkably similar in terms of code quality. Both had clean Rails code, good test coverage, and a working Slack integration. If we'd evaluated them the old way — just reading the code — it would have been a coin flip.

But the transcripts told a completely different story. One candidate started by breaking the problem into clear phases, asked the AI targeted questions about Slack's API edge cases, and course-corrected when the generated code didn't handle webhook retries properly. The other pasted the entire spec into a single prompt, accepted the output mostly as-is, and when something broke, just re-prompted with "fix it" until it worked.

Same output. Completely different engineering signal.

## We're not the only ones thinking this way

In a recent [Y Combinator Light Cone episode](https://www.youtube.com/watch?v=PQU9o_5rHC4), Boris Cherny — the creator of Claude Code — was asked if he'd ever hire someone based on their AI coding transcript. His answer resonated with exactly what we've been seeing:

> *"You can figure out how someone thinks — whether they're looking at the logs or not, can they correct the agent if it goes off the rails, do they use plan mode, when they use plan mode do they make sure that there are tests... do they think about systems? Do they even understand systems? There's just so much embedded in that."*

The conversation surfaced the idea of a spider chart — like the ones in NBA 2K — mapping someone's AI-assisted engineering skills: systems thinking, testing, user behavior, product sense, automation. I love that framing.

Boris also shared an example that stuck with me: an engineer on his team, instead of just implementing a new feature, first built a tool that lets the AI test arbitrary tools — then had the AI write its own tool using it. That kind of out-of-the-box thinking, leveraging AI as a force multiplier rather than just a code generator, is exactly the type of signal we're now looking for.

He made a broader point about hiring that applies well beyond AI tooling:

> *"The biggest skill is people that can think scientifically and think from first principles... I sometimes ask 'what's an example of when you were wrong?' You can see if people can recognize their mistake in hindsight, if they can claim credit for the mistake, and if they learned something from it."*

This mirrors our own evolution. The behavioral dimension — how someone approaches problems, handles failure, and iterates — has always mattered. AI just made it directly observable.

## The new scorecard

Here's roughly how our evaluation emphasis has shifted:

| Dimension | Before | Now |
|-----------|--------|-----|
| Code correctness | High weight | Still matters, but table stakes |
| Code style/structure | High weight | Medium — AI normalizes this |
| Going beyond requirements | High signal | Still high signal |
| Architecture decisions | Evaluated in code review | Evaluated in Loom + transcript |
| Problem-solving approach | Inferred from code | **Directly observed in transcript** |
| AI fluency | N/A | **New dimension — high weight** |
| Debugging & resilience | Inferred from code | **Directly observed in transcript** |
| Speed / velocity | Hard to measure in take-home | **Observable in transcript timestamps** |
| Scope management | Did they over/under-build? | **Can see exactly when they chose to stop or expand** |
| Testing strategy | Did tests exist? | **Did they drive testing or just let AI generate them?** |
| Error recovery | Only saw the final result | **Can see how they reacted when things broke** |
| Product instinct | Inferred from UI/UX polish | **Visible in prompts — did they think about the user?** |

The weightings haven't just shifted — we've added entirely new dimensions that didn't exist before.

## What hasn't changed

Some things are timeless regardless of tooling:

- **Product thinking** — Does the candidate care about the user experience, or did they just build what the spec said? Do they think about the "why" behind the feature?
- **Communication** — Can they explain their decisions clearly in the Loom? Do they anticipate questions?
- **Taste** — This one's hard to quantify, but you know it when you see it. Does the solution feel considered and polished, or does it feel like the first thing that worked?

## Looking ahead

I think we're still in the early innings of figuring this out. The industry hasn't converged on how to evaluate engineers who work with AI, and most interview processes are either pretending AI doesn't exist or banning it entirely.

Neither approach makes sense. AI is how engineers work now. The question isn't whether candidates use it — it's whether they use it well.

At Rootly, we'd rather see a candidate who uses AI thoughtfully and ships something great than one who writes every line by hand but ships something mediocre. The craft isn't gone — it's just evolved. And our evaluation has to evolve with it.