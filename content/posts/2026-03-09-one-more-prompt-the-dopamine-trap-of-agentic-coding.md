---
aliases:
- /posts/2026/03/09/one-more-prompt-the-dopamine-trap-of-agentic-coding/
categories:
- development
cover: /images/covers/the-slot-machine-in-your-terminal-ai-coding-addiction.png
date: 2026-03-09 14:00:00
slug: one-more-prompt-the-dopamine-trap-of-agentic-coding
tags:
- ai
- claude-code
- developer-tools
- productivity
title: 'One More Prompt: The Dopamine Trap of Agentic Coding'
---

It's 2:47 AM on a Tuesday. I'm not debugging a production outage. There's no deadline. I'm just watching Claude Code refactor a module — and I can't stop. One more prompt. One more agent run. One more hit.

If this sounds familiar, you're not alone. Something strange is happening to developers in 2026: **AI coding tools may be triggering the same dopamine loops as slot machines**, and the tech industry is sleepwalking into it.

## The dopamine trap

Steve Yegge nailed it in his recent piece ["The Brute Squad"](https://sourcegraph.com/blog/the-brute-squad):

> Agentic coding is addictive. You will hear it more and more often, because it bewitches people once they've got the hang of it.

He describes the mechanism with uncomfortable precision: every time an agent succeeds — a test passes, a refactor lands clean, a whole feature materializes from a prompt — you get a dopamine hit. When it fails spectacularly, you get adrenaline. Both are reinforcing.

> The intermittent reinforcement of those dopamine and adrenaline hits creates the core addictive pull. It can become near-impossible to tear yourself away.

This is textbook [variable ratio reinforcement](https://en.wikipedia.org/wiki/Reinforcement#Schedules_of_reinforcement) — the same psychological mechanism that makes slot machines the most addictive form of gambling. You never know if the next pull will be a jackpot or a dud, so you keep pulling.

## The sleep crisis nobody talks about

Yegge's confession hit home for me:

> I have to run a practiced escape plan every night to get my computer closed by 2am... I leap up, run out of the room, slam the door, jam my fingers in my ears, and sprint away.

This is a senior engineer — someone who's been in the industry for decades — describing what is essentially a compulsive behavior ritual. And he's *self-aware* about it. Most of us aren't.

I'm not writing about this from a distance. I lived it.

For months, my nights looked the same: close the laptop at midnight, lie in bed, and feel my brain *refuse to stop*. Not from stress — from excitement. The prompts kept composing themselves behind my eyelids. I'd think of a better way to structure a module, a new feature to try, a refactor that would take "just five minutes." My body was in bed but my mind was still in the terminal, still pulling the lever.

It got bad enough that I went to see a doctor. Not for anxiety, not for depression — for the inability to shut my brain off. My cerebral activity was simply not downshifting at night. The wakefulness signals that are supposed to fade when you close your eyes? Mine were stuck on, fired up by hours of agentic dopamine loops. The doctor prescribed a newer class of sleep medication — not a sedative, but something that blocks orexin receptors to selectively turn down the wake drive. My brain wasn't broken. It was just stuck in go mode, and it needed chemical help to stand down.

That was my wake-up call — ironic phrasing aside. When you need pharmaceutical help to undo what your dev workflow is doing to your brain, something has gone seriously wrong.

The pattern isn't unique to me. Developers who used to close their laptops at a reasonable hour are now routinely coding until 2, 3, 4 AM. Not because the work demands it, but because the loop demands it.

## The vibe coding gold rush

Meanwhile, the industry is pouring gasoline on the fire. Garry Tan, Y Combinator's CEO, has been one of the loudest evangelists for what Andrej Karpathy coined "vibe coding" — and he's also been remarkably candid about what it's doing to his sleep.

Here's Tan [on X](https://x.com/garrytan/status/2014762616917524516):

> Claude Code this week has awakened my 25 year old self: the one that chugged red bulls and stayed up til dawn coding. WE ARE SO BACK

And [again](https://x.com/garrytan/status/2015542234180092400):

> So addicted to Claude Code, I stayed up 19 hours yesterday and didn't sleep til 5AM

He even [named the mechanism](https://x.com/garrytan/status/2023770335682666649) explicitly:

> Spending hours with Claude Code is illuminating here. Reading the traces is absolutely fascinating. The machines can search the space and sometimes it has a Eureka moment. It is dopamine-wise as rewarding as finding it yourself manually sometimes!

To his credit, Tan eventually [acknowledged the problem](https://x.com/garrytan/status/2020346258410598574):

> This is unhealthy by the way (speaking from experience) Try to get at least 6 hours of sleep per night when deeply addicted to Claude Code

But here's what's striking: the CEO of the most influential startup accelerator in the world is using the word "addicted" *unironically* — and the tech community treats it as a flex, not a warning. According to TechCrunch, roughly a quarter of YC's recent batch has codebases that are *almost entirely AI-generated*. Tan has called this a superpower for startups, describing "20x companies" where tiny teams automate everything internally with AI agents.

He's not wrong about the productivity gains. But when the person leading the charge is publicly documenting his own sleep deprivation, maybe we should pay attention to what that signals about where this is heading.

## Why this is different from regular workaholism

Developers have always had a complicated relationship with overwork. But AI coding addiction has a different texture:

**1. Zero friction.** Writing code is mentally taxing. Prompting an agent isn't. You can keep going long past the point where your judgment has degraded.

**2. The spectator effect.** Watching an agent work is more like watching a game than playing one. It's passive enough to feel like rest, active enough to keep you engaged. You never feel "done."

**3. Infinite branching.** Every successful output suggests three more things to try. Manual coding has natural scope limits — you get tired, you lose context. With agents, the context is the agent's problem, not yours.

**4. Social reinforcement.** Leaderboards, token counts, commits-per-day metrics — the culture around AI coding tools gamifies the behavior. Shipping 50 commits in a weekend isn't a red flag; it's a flex.

## What I'm trying (and failing at)

I don't have this figured out. Honestly, I still break my own rules more often than I follow them.

I tell myself I'll close the laptop at 11 PM. Some nights I do. Most nights I don't — there's always one more thing the agent is *almost* done with. I've tried batching agent runs instead of watching them in real time, which helps break the reinforcement loop when I actually stick with it. I've tried tracking hours instead of output, because "I shipped six features" sounds productive until you realize it was between midnight and 4 AM with degraded judgment.

The thing that's helped most is just being honest about it — with myself, with other developers. When someone says they "couldn't stop coding all night," I've started asking if they're okay instead of congratulating them. The line between passion and compulsion is thinner than we like to admit.

## The uncomfortable question

The tech industry loves to celebrate intensity. "I shipped an entire app in one weekend with Claude Code" gets mass engagement on X. Nobody asks whether that person slept, whether the code is maintainable, or whether the pattern is sustainable.

We learned — painfully, over decades — that crunch culture in game development destroys people. We're watching the same dynamic emerge with AI coding, except this time the crunch is self-inflicted and disguised as fun.

Garry Tan is right that AI is transforming what small teams can build. Steve Yegge is right that agentic coding is bewitching. But we need a third voice in the conversation — one that asks: **at what cost?**

The terminal will always be there tomorrow, waiting for one more prompt. The question is whether you will be.