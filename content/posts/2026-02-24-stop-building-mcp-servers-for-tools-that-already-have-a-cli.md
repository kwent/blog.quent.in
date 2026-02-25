---
aliases:
- /posts/2026/02/24/stop-building-mcp-servers-for-tools-that-already-have-a-cli/
categories:
- development
cover: /images/covers/stop-building-mcp-servers-for-tools-that-already-have-a-cli.png
date: 2026-02-24 23:27:05
slug: stop-building-mcp-servers-for-tools-that-already-have-a-cli
tags:
- ai
- mcp
- cli
- developer-tools
- claude-code
title: Stop Building MCP Servers for Tools That Already Have a CLI
---

Every week, a new MCP server shows up on GitHub that wraps a CLI tool that already existed. MCP server for GitHub? `gh` has been doing that since 2020. MCP server for AWS? The `aws` CLI covers 200+ services with `--output json`. MCP server for Datadog? They shipped a CLI instead — and it works better.

I get the excitement around [MCP](https://modelcontextprotocol.io/) (Model Context Protocol). It's a clean standard for connecting AI to external systems. Anthropic designed it well. But somewhere along the way, the community started treating MCP as the *default* way to give AI agents access to tools — even when a perfectly good CLI already exists.

That's a mistake.

## The problem with MCP-by-default

MCP requires you to build and maintain a server. That server needs to:

- Implement the MCP protocol correctly
- Handle authentication and session state
- Stay compatible with evolving MCP client versions
- Be discovered, installed, and configured by the user
- Be maintained when the underlying API changes

That's a lot of work for wrapping something that already has a CLI.

Compare that with what happens when [Claude Code](https://docs.anthropic.com/en/docs/claude-code) uses the GitHub CLI. Here's what my actual workflow looks like — no MCP server involved:

```bash
# List open PRs with specific fields
gh pr list --state open --json number,title,author

# Check PR review status and CI checks
gh pr checks 42
gh api repos/owner/repo/pulls/42/reviews --jq '.[].state'

# Create a PR with a structured body
gh pr create --title "Fix auth bug" --body "## Summary\n- Fixed token refresh\n\n## Test plan\n- [x] Unit tests pass"

# Merge Dependabot PRs after checking changelogs
gh pr merge 15 --squash --auto

# Search issues across repos
gh search issues "memory leak" --repo owner/repo --state open --json number,title,url
```

No server to run. No configuration beyond `gh auth login`. No protocol negotiation. Just text in, text out. And Claude already knows how to use it — because it's been trained on millions of shell sessions, man pages, and Stack Overflow answers that reference these tools.

In fact, the [previous blog post](/blog/2026/02/24/from-maintainers-wanted-to-three-major-releases-in-a-weekend/) on this blog was researched entirely through `gh` — pulling PR timelines, commit histories, issue data, and Dependabot PR counts across three repositories. All via CLI. No MCP server needed.

## LLMs are already fluent in CLI

This is the part that MCP advocates consistently underestimate. Large language models don't need a structured protocol to interact with well-built CLI tools. They already understand them *natively*.

Think about it:

- **`gh`** — Claude knows every subcommand, every flag, every `--jq` filter pattern. It can compose multi-step GitHub workflows by chaining `gh` calls without ever reading documentation.
- **`aws`** — 200+ services, all with `--output json`. Claude can query CloudWatch, manage S3 buckets, describe EC2 instances — all through the CLI it's been trained on.
- **`pup`** — Datadog's new CLI. 200+ commands, structured JSON output, automatic agent detection. A well-built CLI doesn't need training data — `--help` and structured output are enough.
- **`jq`**, **`curl`**, **`git`** — The foundational UNIX tools. Claude is fluent in these to a degree that no MCP server will ever match, because the training data is decades deep.

As [Sumner Evans put it](https://sumnerevans.com/posts/software-engineering/forget-mcp-write-cli-apps/): CLIs are text-based, so there are no wasted tokens from mode transformations. The input and output are plain text streams — exactly what LLMs natively consume and produce. No serialization overhead, no protocol negotiation, no schema translation. Just text.

## The token tax

Here's a concrete cost most people don't think about: MCP tool descriptions consume tokens in every conversation.

When you configure an MCP server, its tool schemas get loaded into the context window. Every tool, every parameter, every description — all of it eats tokens before you've even asked a question. Configure a few MCP servers and you're burning thousands of tokens per message just on tool definitions.

CLI tools don't have this problem. They exist in the shell. The LLM knows about them from training. It calls them when it needs them, reads the output, and moves on. Zero token overhead for tool discovery.

[Mario Zechner's benchmarks](https://mariozechner.at/posts/2025-08-15-mcp-vs-cli/) confirmed this empirically — CLI-based approaches were significantly more token-efficient than MCP equivalents for the same tasks. His memorable framing: *"Just like a lot of meetings could have been emails, a lot of MCPs could have been CLI invocations."*

## When MCP actually makes sense

I'm not saying MCP is useless. It genuinely shines in specific scenarios:

**When no CLI exists.** Some services simply don't have a CLI. Internal tools, proprietary platforms, niche SaaS products — if there's no command-line interface, MCP is a reasonable way to bridge the gap.

**When your users aren't developers.** This is [Zuplo's argument](https://zuplo.com/blog/cli-or-mcp), and it's a good one. A product manager checking deployment status, a finance team querying API usage, a legal team running compliance reports — these people will never open a terminal. MCP lets them interact with your platform through natural language in a chat interface.

**When you need persistent state.** MCP servers are stateful by default. For things like browser sessions, database connections, or long-running operations where you need to maintain context between calls, MCP's architecture makes more sense than stateless CLI invocations.

**When the client has no shell.** Some LLM interfaces — web chat, mobile apps, Claude.ai — don't provide terminal access. MCP is the only way to extend these clients with external tool access.

## Companies that got this right

### Datadog shipped a CLI while their MCP is still in beta

Datadog's MCP server is still in closed beta. But instead of making everyone wait, they shipped [pup](https://github.com/datadog-labs/pup) — an open-source CLI that gives AI agents (and humans) access to 200+ commands across 33+ Datadog products. Written in Rust. Apache 2.0 licensed. Available today.

```bash
# Query metrics
pup metrics query --query="avg:system.cpu.user{*}" --from="1h"

# List monitors in alert state
pup monitors list --output json

# Check incidents
pup incidents list

# Browse dashboards
pup dashboards list
```

The clever part: pup automatically detects when it's being invoked by an AI agent. It checks for environment variables like `CLAUDE_CODE`, `CURSOR_AGENT`, `CODEX`, and others. When agent mode is active, responses return structured JSON optimized for machine parsing, confirmation prompts auto-approve, and error messages include actionable hints.

No MCP server to configure. No protocol to negotiate. Claude Code runs `pup monitors list`, gets clean JSON back, and keeps going. The MCP server is still gated behind access requests. The CLI shipped and works today.

### We built rootly-cli after shipping an MCP server first

At [Rootly](https://rootly.com), we actually built the [MCP server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) first. It worked — but once we saw how developers actually used AI agents in terminals, we realized a CLI would reach them faster with less friction. So we built [rootly-cli](https://github.com/rootlyhq/rootly-cli), designed to be AI-agent-native from the ground up.

```bash
# List critical incidents
rootly incidents list --status=started --severity=critical

# Check who's on-call right now
rootly oncall who

# Create an incident
rootly incidents create --title "API latency spike" --severity critical

# Send a deployment pulse
rootly pulse run -- make deploy
```

We made specific design choices that make it work seamlessly with AI agents:

- **TTY-aware output**: When piped (as it would be from Claude Code), it automatically switches to JSON — no `--format` flag needed
- **Markdown output mode**: `--format=markdown` outputs data in markdown — and agents *love* markdown. It's the format LLMs are most fluent in. Tables, headers, lists — all parseable without any JSON wrangling, and compact enough to keep token usage low. We added it specifically because we noticed Claude produced better responses when given markdown input vs. raw JSON.
- **Clean stdout/stderr separation**: Pagination info goes to stderr, data goes to stdout, so agents get clean output
- **Server-side filtering**: `--status`, `--severity`, `--source`, `--limit` — the agent queries exactly what it needs instead of pulling everything and filtering locally

The result: Claude Code can manage incidents, check on-call schedules, query alerts, and track deployments — all through shell commands it already understands. No MCP configuration, no token overhead from tool schemas, no servers to maintain.

## The decision is simpler than you think

Before building an MCP server, ask one question: **Does this tool already have a CLI?**

If yes, you probably don't need an MCP server. Especially if your users are developers working in environments that have shell access (terminals, IDEs, CI/CD). The AI agent already knows how to use the CLI. You're building infrastructure for a problem that's already solved.

If no, or if your audience includes non-developers who need access through chat interfaces, then MCP is the right call.

Here's the decision tree:

| Scenario | Use CLI | Use MCP |
|----------|---------|---------|
| Developer tool with existing CLI (`gh`, `aws`, `pup`) | **Yes** | No |
| Internal service with no CLI | No | **Yes** |
| Non-developer users needing platform access | No | **Yes** |
| LLM client without shell access (web chat, mobile) | No | **Yes** |
| Stateful operations (browser sessions, DB connections) | No | **Yes** |
| Composable UNIX-style data pipelines | **Yes** | No |

## The UNIX philosophy was right all along

There's a delicious irony in all of this. The UNIX philosophy — write programs that handle text streams, expect your output to become input to another program, design for composability — was articulated in the 1970s. Fifty years later, it turns out to be the perfect interface for AI agents.

CLI tools built on UNIX principles didn't just survive the AI revolution. They became the most natural interface for it. Text in, text out. Pipes and filters. Small tools that do one thing well. It's what LLMs were born to work with.

So before you write another MCP server that wraps `gh` or `aws` — ask yourself: is this MCP solving a real problem, or is it just a meeting that could have been an email?

---

*Written with [Claude Opus 4.6](https://docs.anthropic.com/en/docs/about-claude/models) via [Claude Code](https://docs.anthropic.com/en/docs/claude-code).*