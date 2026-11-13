---
categories:
- development
cover: /images/covers/code-isnt-the-bottleneck-anymore-review-is.png
date: 2026-11-12T09:00:00-0800
draft: true
slug: code-isnt-the-bottleneck-anymore-review-is
tags:
- ai
- code-review
- engineering
- reliability
- compliance
- soc2
title: "Code Isn't the Bottleneck Anymore. Review Is."
---

Nine in ten approvals on our main repo came without a single comment. Almost half were for a commit we didn't end up shipping.

A year ago that repo at [Rootly](https://rootly.com) merged 356 pull requests in October. This October it merged 2,053. Across the whole GitHub org, the number went from 530 to 4,187.

The number of people giving approvals barely moved. It was about 25 a month in August and 27 in October. Each of them went from roughly 28 approvals a month to 70.

Agents write most of that code now. The approval step was sized for a team that typed its own code, and it shows.

## What the wait costs

I pulled every PR merged into master between August 1 and November 5: 3,661 of them, written by people (or by agents on their behalf) and approved by someone other than the author.

The typical PR is fine. Median wait for a first approval is 1.7 weekday hours. The tail is the problem. The slowest tenth waited more than 39 working hours. Add up every PR's wait and you get 2,316 weekday PR-days spent sitting in a queue.

When a PR stalls, people ask in chat. I found 570 merged PRs that someone asked about in public channels. A quarter of those were approved within five minutes of the ask, almost always with no comment. The asks sell size and speed. Nobody sells risk.

## What the approval checks

This was the uncomfortable part.

- 1.1% of PRs got a change request from a human.
- 90.5% were approved without a single review comment.
- 24.4% were approved faster than 500 lines an hour, with no comment. SmartBear's [study of a Cisco team](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) puts the useful inspection rate below 500 lines an hour.
- 43.3% were approved on a commit that wasn't the one we merged.

That last one bothers me most. Almost half the time, the code changed after the approval. The approval was for a different diff than the one we shipped.

The fast approvals didn't spare high-risk PRs either. And PRs that got a written review needed a follow-up fix about as often as those that didn't.

We ran the same numbers on a second, much smaller repo with 178 PRs in the window. 91% of approvals had no comment. It asks for changes three times as often and waits twice as long per PR, but the pattern holds.

## We're not the only ones

Researchers at Carnegie Mellon and Stanford followed 802 developers and about 196,000 PRs at one company that told its engineers to double their output with AI ([paper](https://arxiv.org/abs/2607.01904), [Semgrep's summary](https://semgrep.dev/blog/2026/end-is-nigh-for-code-review/)). PR volume grew 3.1x. The pool of reviewers grew 1.5x. The share of PRs with a human-written review comment fell from 39% to 21%, and the median reviewer's silent approvals roughly doubled. People didn't review harder. They approved more and said less.

One detail from that paper stuck with me: reverts stayed flat the whole time. If you only watch reverts, you'd never notice that review had quietly stopped happening.

[Faros AI](https://www.faros.ai/blog/ai-productivity-paradox-report-2025) saw the same thing across more than 10,000 developers in 2025. Teams with high AI adoption merged 98% more PRs, and review time went up 91%.

Nobody hired their way out of this. The reviewers are the same people, with more PRs each.

## A reviewer that reads every diff

We already run an AI reviewer on every PR to the main app. It scores each PR from 1 to 5, states a risk level, and comments on lines. 98% of PRs carry a score.

Three things set it apart from the human stamp:

It's fast. Median time from ready to first score is 6 minutes, against 1.7 weekday hours to the first human approval.

It changes code. 552 PRs that the reviewer first scored 3 or lower reached 4 or 5 after the author pushed fixes. Humans requested changes on 1.1% of PRs, about 40 in the window. That's roughly 14 times as many PRs where a review made the code better. AI reviewers are now far better than us at this job.

It re-reads. Push a new commit and it scores again. A human approval is a one-time stamp on whatever commit was there.

So the rule is short. The reviewer approves a PR when all of these hold:

- risk:low, confirmed by the reviewer
- review score 4 or 5 on the head commit
- no sensitive path and no risky migration

Everything else waits for a human, as it does today.

There's no size cap. I argued in May that [the small PR rule won't survive AI](/blog/2026/05/19/your-small-pr-rule-wont-survive-ai/), and a line count is a poor proxy for risk when an agent writes the diff. [Rewind](https://rewind.com/blog/ai-approve-pull-requests-safely/) came to the same conclusion: risk has almost nothing to do with line count. Risk and paths are the signals.

## What it would miss

It still doesn't catch everything a person does. On the 19 PRs where a human did push back and the rule above (minus the path guardrails) would have skipped them, it fully raised the same issue once and partly raised four. It missed three substantive ones. The other eleven were style, preference, or not about code.

The guardrails do the real work. Two of the three substantive misses touched a migration or authentication code, so the sensitive-path rule sends them to a human. The third would get through. It was large, and only a size cap would have stopped it. I'd rather tune the risk check than bring back a line limit that blocks every big, boring agent PR.

The PRs in the window that later caused an incident were all high-risk and touched sensitive code. None would qualify. Every one of them had a human approval with no comment.

## Who sets the risk label

The rule leans on risk:low, so I checked who sets it. 69% of risk labels are applied under the author's account, mostly by the coding agent that opened the PR, seconds after opening it. The agent is grading its own homework.

On the 1,865 PRs where both the author and the reviewer stated a level, they agreed 77% of the time. The reviewer rated higher 22% of the time and lower only 2%. When the reviewer raised a risk:low PR to medium, that PR needed a follow-up fix more often. The one reverted PR the rule would have let through on the label alone sits in that group.

The asymmetry decided it. If the reviewer is wrongly cautious, a human reviews the PR, same as today. If the author is wrongly optimistic, it ships without anyone reading it.

So the reviewer combines the two: the higher level wins. A label a person set is never lowered. A label the reviewer set on an earlier commit gets replaced when it re-reviews.

## Reliability is the job

We build incident management. When our customers are down, Rootly is how they page their on-call and run the response. If we break, we break during someone else's worst hour. So shipping faster only counts if reliability doesn't move.

Here's the part that took me a while to see. The human approval wasn't protecting reliability much. The PRs that caused our incidents all had one, with no comment. What protected us was everything around the approval: tests, staged deploys, feature flags, and people who knew which parts of the system were dangerous.

So we didn't trade review for speed. We moved the review to where it matters.

**The gate is code, not a model.** The AI reviewer produces a score, a risk level and findings. A small, deterministic rule turns those into a decision, and humans own that rule. The model never decides on its own that something is safe enough, and it can't edit its own policy.

**Sensitive paths always go to a person.** Migrations, authentication and permissions, billing, CI and deploy config, dependency changes. No score gets those through.

**Approval is pinned to a commit.** A new push means a new review. The old human stamp covered the shipped code only 57% of the time.

**The deploy path doesn't change.** An auto-approved PR goes through the same CI, the same staged rollout and the same flags as any other. Approval was never our last line of defense, and we didn't make it one.

**Humans get their attention back.** This is the reliability argument I care about most. Every low-risk PR the bot takes is one less silent thumbs-up from a tired reviewer. Those reviewers now see fewer PRs, and the ones they see are the risky ones: the migrations, the auth changes, the PRs the reviewer itself flagged. That's where our incidents came from.

**We watch more than reverts.** Reverts, follow-up fixes within seven days, and incidents traced to an auto-approved PR. We also track the review-quality signals, since the CMU paper showed reverts can stay flat while review quietly disappears.

**It's easy to stop.** One flag turns it off. Anyone can ask for a human with a label. Any serious incident traced to an auto-approved PR turns it off until we understand why. A miss adds a path to the list; it doesn't end the policy.

## Where we are

We ran in shadow mode for two weeks. The reviewer marked "would approve" on every PR it would have approved, approved nothing, and we compared its calls with what humans did.

Now we're in phase one. The reviewer approves PRs that are risk:low, score 4 or 5, and stay off the sensitive paths. Everything else still goes to a person. Next is widening it carefully, repo by repo.

Others went first. [Rewind](https://rewind.com/blog/ai-approve-pull-requests-safely/) only went live after humans agreed with their bot at least 90% of the time in shadow mode. They landed at about 99% agreement with around 40% of PRs auto-approved, and they're careful to call their numbers directional. [Ona](https://ona.com/stories/auto-approving-low-risk-prs) saw median time to first approval drop from almost three hours to under four minutes, though they changed two other things at the same time. [Intercom](https://ideas.fin.ai/p/ai-is-approving-our-pull-requests) auto-approves over 19% of PRs with no human in the loop, and says it makes them safer. Their AI-authored backend code gets reverted 0.53% of the time, against 5.39% for human-authored.

Rewind and Ona keep a person clicking merge. We go one step further: the bot's approval is enough for a PR to go out through the deploy pipeline. That's the part I'm watching closest.

## The compliance question

Can a bot approve a change and still pass a SOC 2 audit?

SOC 2 doesn't say "a human must click Approve." The change management criterion, CC8.1, asks that changes are authorized, tested, approved and implemented under a process you define. Most companies, us included, describe that process as "every change is reviewed by someone other than the author before it reaches production." The auditor then samples merged PRs and checks for an approval from a second account.

Here's the awkward bit. By that test, our old process passes. Every one of those 3,661 PRs has an approval from someone other than the author. The sample wouldn't show that 90% carry no comment, or that 43% of approvals were for an earlier commit. The control works on paper and much less in practice.

The evidence side is the easy part to automate. A script against the GitHub API can list every merged PR in the audit period and answer four questions for each one:

1. Was it approved by someone other than the author?
2. Was the approval on the commit that was merged?
3. Did required checks pass on that commit?
4. If it bypassed review, who did it and why?

We already had most of this from the data behind the numbers above. Producing it per audit period is a cron job, not a project.

What doesn't automate is the judgment: what counts as a reviewer, and what you wrote down. An auto-approval changes the control description, so it needs to be written as policy before it runs, not discovered by the auditor. The way I'd describe ours:

- The approver is a separate system from the author. The coding agent that wrote the PR can't approve it, and its own risk label can only be raised, never trusted on its own.
- The approval is pinned to a commit. Any new push needs a fresh review. That's stricter than the human control it replaces.
- Eligibility is defined in advance and checked from the diff: risk level, score and paths.
- Everything outside that set goes to a human, and a human can always ask for one.
- Every auto-approval leaves a written review with findings, score and risk reasoning. That's more evidence per change than a silent thumbs-up.
- Someone samples auto-approved PRs every month and reports misses, reverts and follow-up fixes.

We haven't been through an audit with this yet. Rewind published the control mapping they wrote for theirs, down to the CC8.1 sub-points, which is a good template. I expect the auditors to move too.

Their sampling test was built for a world where people wrote the code and a teammate read it. That world is going away. When agents open most of the PRs and each approver is asked for 70 a month, "a second account clicked Approve" stops telling you anything. Our numbers show it already doesn't.

The questions that still matter are different. Did something independent read the exact code that shipped? Was the rule for skipping a human written down before it ran? Do the misses get counted and fed back? An AI reviewer answers those with a record for every change. A silent thumbs-up answers none of them.

Teams will move first, because the queue forces them to. I think the frameworks and the people who apply them will follow. They already accept a green CI run as evidence that a change was tested, and nobody asks who watched the tests run. Until then, write the policy down and keep the evidence, so you're ready for the auditor who asks.

## What I don't know yet

Whether the reviewer's agreement with the author holds outside the 51% of PRs where we could measure both.

Whether people trust an approval they didn't give. The numbers say the old approval rarely read the diff. That doesn't mean everyone feels fine handing it to a bot.

Whether dropping the size cap holds up. One of the three substantive misses would have gone through without it. The monthly review will show whether that was a one-off.
