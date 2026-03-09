---
aliases:
- /posts/2026/03/09/from-vs-code-to-agent-orchestrators-how-multi-agent-workflows-changed-everything/
categories:
- development
cover: /images/covers/from-vs-code-to-agent-orchestrators-how-multi-agent-workflows-changed-everything.png
date: 2026-03-09 08:47:29
slug: from-vs-code-to-agent-orchestrators-how-multi-agent-workflows-changed-everything
tags:
- ai
- claude-code
- conductor
- superset
- developer-tools
- multi-agent
- t3-code
title: From Writing Code to Orchestrating Agents
---

My dev workflow has changed more in early 2026 than in the previous five years. I went from writing code in VS Code, to pair-programming with AI in Cursor, to running CLI agents like Claude Code and Codex — and now I'm orchestrating multiple agents working in parallel on different tasks at the same time.

Each step felt like a leap. But the jump to multi-agent orchestration is the one that fundamentally changed how I think about shipping software.

## The evolution

### Phase 1: VS Code — the manual era

For years, VS Code was the center of my workflow. Extensions, keybindings, snippets — I had it dialed in. But every line of code was mine to write, every refactor mine to execute. Context switching between files, debugging, and testing was all sequential. One brain, one cursor, one task at a time.

### Phase 2: Cursor — AI as copilot

[Cursor](https://cursor.com/) changed the game by embedding AI directly into the editor. Tab completions that actually understood my codebase. Inline chat for quick questions. Agent mode that could edit files directly. It felt like having a junior dev sitting next to me.

But it was still one conversation, one task. If I asked Cursor to refactor a module, I was blocked until it finished. And for complex multi-file changes, the context window was the bottleneck — the AI would lose track of what it was doing halfway through.

### Phase 3: CLI agents — AI as executor

Then came [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [OpenAI Codex](https://openai.com/index/codex/). Running AI agents directly in the terminal unlocked something Cursor couldn't: deep, autonomous execution. Claude Code could explore my entire codebase, run tests, fix failures, and iterate — all without me hovering over every edit.

I'd fire off a task, go grab coffee, come back to a working PR. That was powerful. But I was still running one agent at a time. While Claude Code was refactoring my auth module, I was sitting there waiting — or context-switching to something else manually.

### Phase 4: Multi-agent orchestration — the multiplier

This is where tools like [Conductor](https://conductor.build/), [Superset](https://superset.sh/), and [T3 Code](https://t3.codes/) come in. They solve the obvious next problem: **why run one agent when you can run ten?**

The idea is simple. Instead of giving one AI agent one task and waiting, you spin up multiple agents in isolated workspaces — each working on a different task, in parallel, on the same codebase. Each agent gets its own isolated environment, so there are no merge conflicts. You see all their progress in a single dashboard. When they're done, you review the diffs and merge.

It's the difference between having one employee and having a team.

## What this looks like in practice

Here's a real example. I had four things to do on a project:

1. Add a new API endpoint
2. Write tests for an existing module
3. Fix a CSS layout bug
4. Update documentation

Old workflow: I'd do these sequentially. Maybe 3-4 hours total, with context-switching overhead between each task.

New workflow with Conductor: I opened four workspaces, gave each agent a clear prompt, and let them run. I reviewed diffs as they came in. Total wall-clock time: about 40 minutes — mostly spent reviewing.

That's not a marginal improvement. That's a fundamentally different way of working.

## The orchestration tools

A new category of tools has emerged to solve this exact problem. Here are the three I've been exploring.

**[Conductor](https://conductor.build/)** is a native macOS app built specifically for orchestrating Claude Code agents. It gives you isolated workspaces, a built-in diff viewer, MCP integrations, and slash commands. It feels polished and opinionated — you open it, create workspaces, and start shipping. The tight integration with Claude Code means things like context files (`.context/` directories) and branch management just work.

**[Superset](https://superset.sh/)** takes a more agent-agnostic approach. It's open-source and works with any CLI-based agent — Claude Code, Codex, OpenCode, Gemini CLI, whatever. It uses Git worktrees for isolation and lets you open any workspace in your IDE of choice (VS Code, Cursor, JetBrains). If you want flexibility across different AI providers, Superset is the more universal option.

**[T3 Code](https://t3.codes/)** is an open-source desktop app built by [Theo Browne](https://t3.gg/) that acts as a purpose-built UI layer on top of coding agents. It gives you multi-repo, multi-agent parallelism with Git worktree integration, a task-oriented chat UI with full reasoning and tool call visibility, and Git actions built into the workflow. It currently runs on Codex with Claude Code support coming soon. If you want a clean GUI that brings visibility into what your agents are actually doing, T3 Code is worth a look.

I've been using Conductor as my daily driver because the Claude Code integration is seamless. But the space is moving fast — Superset and T3 Code both bring something different to the table, and I expect to keep bouncing between them as they evolve.

## The dirty secret: Git worktrees are painful

Under the hood, most of these tools rely on [Git worktrees](https://git-scm.com/docs/git-worktree) — a Git feature that lets you check out multiple branches of the same repo into separate directories simultaneously. In theory, it's perfect for parallel agents: each agent gets its own working directory and branch, but they all share the same Git history and object store. No duplicated `.git` folders, no divergent state.

In practice? Worktrees are a pain to manage manually. You have to create them, name them, track which branch maps to which directory, remember to clean them up when you're done, and deal with edge cases like shared lockfiles or ports. Most developers I know have never used `git worktree` directly — it's one of those powerful Git features that nobody touches because the UX is terrible.

And that's exactly the abstraction layer these orchestration tools provide. When I create a workspace in Conductor, I don't think about worktrees at all. I just click "new workspace," point it at my repo, and start an agent. Conductor handles the worktree creation, branch naming, isolation, and cleanup behind the scenes. Superset does the same — its entire architecture is built on worktrees, but the complexity is hidden behind a clean terminal UI.

Some tools don't even bother with worktrees. They just do a raw copy of the project directory. It's less elegant — you're duplicating the entire `.git` folder and history — but it's simpler and avoids some of the worktree edge cases around submodules, lockfiles, and tools that don't play well with shared Git state. For smaller repos, the tradeoff is barely noticeable.

The point is: **you shouldn't have to think about the isolation mechanism.** Whether it's worktrees, copies, or containers — that's a plumbing detail. The orchestrator should handle it. And the best ones do.

## Why orchestration matters more than the model

Here's the counterintuitive insight: **the orchestration layer matters more than which AI model you're using.**

A single Claude Opus agent is incredibly capable. But one agent working on one task is still one agent working on one task. Five agents — even running a slightly less capable model — working in parallel on five well-scoped tasks will outperform a single genius agent every time.

The bottleneck in AI-assisted development was never intelligence. It was parallelism. These orchestration tools remove that bottleneck.

## The new skill: prompt decomposition

The most important skill in this workflow isn't prompt engineering for a single agent — it's **task decomposition**. Breaking a large piece of work into independent, well-scoped tasks that can run in parallel without stepping on each other.

This is essentially what a good engineering manager does: break down a project into parallelizable work items, assign them to team members, and review the output. Except now the team members boot up in seconds and work 24/7.

Some principles I've learned:

- **Scope tightly.** Each agent should have a single, clear objective. "Add the `/users` endpoint with tests" beats "work on the API."
- **Isolate dependencies.** If task B depends on task A's output, don't parallelize them. Run A first, then fan out.
- **Front-load context.** Write good `CLAUDE.md` files and keep your codebase well-organized. Agents that understand the project structure produce better results.
- **Review aggressively.** More agents means more diffs to review. Don't rubber-stamp. The speed gain is meaningless if you're merging broken code.

## What I miss (and what's coming)

This workflow isn't perfect yet. A few rough edges:

- **Inter-agent communication is limited.** If agent A discovers something that agent B needs to know, there's no great way to share that mid-task. You end up being the router.
- **Cost adds up.** Running five Claude Opus agents in parallel isn't cheap. You need to be intentional about when parallelism is worth the spend.
- **Review becomes the bottleneck.** Ironically, the faster agents produce code, the more time you spend reviewing. This is a good problem to have, but it's real.

I expect all of these to improve quickly. VS Code already [announced multi-agent support](https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development) in early 2026. Claude Code shipped Agent Teams with inter-agent communication. The ecosystem is converging on orchestration as the next layer of the stack.

## The bottom line

My workflow evolution:

| Phase | Tool | Parallelism | My role |
|-------|------|------------|---------|
| 1 | VS Code | None | Writer |
| 2 | Cursor | None | Pair programmer |
| 3 | Claude Code CLI | None | Delegator |
| 4 | Conductor / Superset | Full | Orchestrator |

Each phase didn't replace the previous one — it absorbed it. I still use VS Code (through Cursor). I still use Claude Code (through Conductor). But the way I think about work has shifted from "how do I write this code?" to "how do I decompose this project into parallel streams and review the output?"

If you're still running one AI agent at a time, try spinning up a multi-agent workflow. The first time you see four agents shipping four features simultaneously while you sip coffee, you'll wonder how you ever worked any other way.