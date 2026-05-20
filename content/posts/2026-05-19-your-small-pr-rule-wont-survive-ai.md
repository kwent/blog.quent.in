---
aliases:
- /posts/2026/05/19/your-small-pr-rule-wont-survive-ai/
categories:
- development
cover: /images/covers/your-small-pr-rule-wont-survive-ai.png
date: 2026-05-19 08:00:00
slug: your-small-pr-rule-wont-survive-ai
tags:
- ai
- code-review
- engineering-culture
- feature-flags
- developer-tools
title: Your Small PR Rule Won't Survive AI
---

For two years, we enforced a strict small-PR culture at [Rootly](https://rootly.com). Stacked PRs, atomic changes, never more than a couple hundred lines. The logic was sound: smaller diffs are easier to review, easier to revert, easier to reason about.

Then AI started writing most of our code.

## What broke

When a human writes code, small PRs make sense. You think in increments. You build a data model, wire up an endpoint, add a frontend component. Each step is a natural review boundary.

AI agents don't work that way. They think in features. You describe what you want, and they produce the whole thing: migration, model, service, controller, tests, frontend. Splitting that output into a stack of five PRs creates busywork with no upside. The reviewer still needs to understand the full feature to evaluate any single piece. And now they're doing it across five tabs instead of one.

We tried making it work. We asked agents to produce stacked PRs. The results were technically correct but contextually worse. Each PR referenced code that didn't exist yet in the base branch. Review comments on PR #2 often depended on decisions made in PR #4. Reviewers were doing more mental gymnastics, not less.

The small-PR rule was optimized for human writing speed. AI removed that constraint, and the rule became overhead.

## What we do instead

We stopped reviewing AI code the way we reviewed human code. Line-by-line review of a 2,000-line AI-generated PR is rarely the best use of time. The syntax is usually fine. The patterns are usually consistent. The variable names are usually reasonable. The harder bugs hide in context, shared boundaries, and rollout paths.

AI bugs are context bugs. The code works, but it's applied to the wrong thing. A migration that drops a column still in use by a background job. A service that writes to a table another team reads from. A feature flag check that gates the happy path but not the error path.

So we shifted the review mindset: read the risky paths closely, then ask what could go wrong.

### AI reviewing AI

We built an internal AI code reviewer. It reads every PR against our engineering standards and produces a structured review: a risk assessment, a standardization score, a confidence score, and specific findings grouped by severity.

The key design choice: it doesn't try to be a human reviewer. It doesn't bikeshed variable names or suggest refactors. It answers one question per PR: "If this change has a bug, what user-facing behavior breaks?" That answer drives the risk classification, which tells the human reviewer how much time to spend.

It flags database migrations, security-sensitive changes, and modifications to core workflows like paging and incident creation. It distinguishes between changes that alter what the system does versus changes that affect how fast or how something looks. A N+1 query fix on an index page and a change to escalation policy execution logic both touch core code, but they carry very different risk profiles.

The human reviewer gets a structured starting point instead of a raw diff. For a `risk:low` PR that scores 5/5 on standards compliance, the review is a quick sanity check. For a `risk:high` PR with a 3/5 confidence score, the reviewer knows exactly which findings to dig into and where the AI reviewer wasn't sure.

### Feature flags as the real review gate

The most important shift: we moved the safety boundary from "merge" to "rollout."

Every significant feature ships behind a flag. The PR gets merged. The code exists in production. But it's off. The real review happens during progressive rollout: enable for the team first, then a handful of customers, then 10%, then everyone.

If something breaks at 10%, you kill the flag first. Often that means no immediate rollback, no revert, no hotfix. The blast radius was scoped from the start. Stateful changes still need a real rollback plan.

This changes how you think about risk. A PR with a subtle bug in a gated feature is low-stakes. A one-line config change that's live immediately is high-stakes. The size of the diff stopped being the useful signal. The blast radius is.

### Risk labels over line counts

Every PR at Rootly gets a risk label: `risk:low`, `risk:medium`, or `risk:high`. This replaced the old proxy of "is the PR small enough?" with a direct question: what happens if this breaks?

A 3,000-line PR behind a feature flag, with no migration, no shared contract changes, shipping to internal users first? `risk:low`. Ship it.

A 12-line PR that alters a database index on a table with 50 million rows? `risk:high`. That gets the careful review, the off-hours deploy window, the monitoring dashboard open on a second screen.

The label forces the author to think about blast radius at PR creation time, not during review. And it gives reviewers an immediate signal for how much scrutiny a PR actually needs. A `risk:low` PR from an AI agent that passes CI? Skim the migration check, confirm the flag boundary, approve, move on. A `risk:high` PR? That's where you spend your review budget.

## The PR template that replaced line counts

Our PR template encodes this whole philosophy. It doesn't ask "is this PR small enough?" It asks the questions that actually predict production incidents:

**Why** and **What** sections force the author to explain motivation and scope of impact. For AI-authored PRs, the human who prompted the agent fills these in. We explicitly instruct AI assistants not to generate these sections, because the whole point is capturing context the AI doesn't have: why this change, why now, what's the business reason.

**Rollback/Revert Plan** is a required field. Every PR needs to describe how to safely undo itself, including any data fixes. This is the single most useful thing in the template. When something goes wrong at 2 AM, nobody wants to reverse-engineer a rollback from a diff.

The **Standard Checklist** asks the questions that catch real production issues:

- Risk level label added?
- Revertible? Are migrations reversible? Up and down tested?
- Access control verified?
- Exceptions logged with context?

Then there's a full **Deployment Process Checklist**: document the rollout plan in Linear, document the rollback plan in the PR, validate on staging, get the deploy queue bot, validate in production. Each step has a template to fill out so nothing gets skipped.

None of these items care about PR size. They care about whether the change can be safely deployed and safely reverted. A 200-line PR with an irreversible migration and no rollback plan fails this template harder than a 3,000-line feature behind a flag with a clean revert path.

## What we learned

Killing the small-PR rule felt uncomfortable at first. It was one of those engineering practices that felt virtuous. But practices exist to serve outcomes, and the outcome we cared about was shipping reliable software quickly.

I wrote more about this shift toward production-side safety in [Stop Trying to Review AI's Code Faster: Bet on Rollbacks Instead](https://rootly.com/blog/stop-trying-to-review-ais-code-faster-bet-on-rollbacks-instead). The short version: at Rootly, when 80%+ of PRs by count are AI-authored, your investment in review has diminishing returns. Your investment in rollback infrastructure has compounding ones.

Small PRs were the right answer for a team of humans writing code by hand. They're the wrong answer for a team orchestrating AI agents that ship complete features. The discipline didn't disappear. It moved downstream, to flags, scoped rollouts, and systems that make it safe to be wrong.
