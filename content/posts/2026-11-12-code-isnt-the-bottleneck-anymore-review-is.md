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

Nine in ten PRs on our main repo were approved without a single human review comment. In almost half, the last approval was attached to an earlier commit than the PR's final head.

A year ago that repo at [Rootly](https://rootly.com) merged 356 pull requests in October. This October it merged 2,053. Across the whole GitHub org, the number went from 530 to 4,187.

The number of people giving approvals barely moved. It was about 25 a month in August and 27 in October. Each of them went from roughly 28 approvals a month to 70.

Agents write most of that code now. The approval step was sized for a team that typed its own code, and it shows.

We already use an AI reviewer. I'm proposing that it approve a defined set of low-risk changes too. We haven't run shadow mode yet.

## What the wait costs

I pulled every PR merged into master between August 1 and November 5: 3,661 of them, written by people (or by agents on their behalf) and approved by someone other than the author.

Median time from ready for review to first human approval is 1.7 weekday hours. The tail is the problem. The slowest tenth waited more than 39 weekday hours. Added across PRs, the wait totals 2,316 weekday PR-days.

When a PR stalls, people ask in chat. I found 570 merged PRs that someone asked about in public channels. A quarter of those were approved within five minutes of the ask, almost always with no comment. The asks usually mention size and speed. Risk rarely comes up.

## What approval leaves behind

- 1.1% of PRs got a change request from a human.
- 90.5% were approved without a single human review comment.
- 24.4% were approved with no human comment in less time than a 500-line-an-hour read-through would take. That interval starts at ready for review and includes queue time. SmartBear's [study of a Cisco team](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) recommends inspecting fewer than 500 lines an hour.
- 43.3% were approved on an earlier commit than the PR's final head.

That last one bothers me most. We compared the latest approval's commit with the final PR head before the squash merge. We don't dismiss stale approvals after a push, so a new commit can reach master without an approval attached to it.

The fast approvals included high-risk PRs. And PRs that got a written review needed a follow-up fix within seven days about as often as those that didn't. Those signals raise doubts about review depth. They don't tell us how carefully someone read a particular diff.

We ran the same numbers on a second, much smaller repo with 178 PRs in the window. 91% of approvals had no human comment. Human change requests were three times as common and the approval wait twice as long, but silent approvals still dominated.

## We're not the only ones

Researchers at Carnegie Mellon and Stanford followed 802 developers and about 196,000 PRs at one company that told its engineers to double their output with AI ([paper](https://arxiv.org/abs/2607.01904), [Semgrep's summary](https://semgrep.dev/blog/2026/end-is-nigh-for-code-review/)). PR volume grew 3.1x. The pool of reviewers grew 1.5x. The share of PRs with a human-written review comment fell from 39% to 21%, and the median reviewer's silent approvals roughly doubled. Most of the extra load showed up as approvals without comments.

One detail from that paper stuck with me: revert rates didn't rise as written human feedback declined. Watching reverts alone wouldn't reveal that shift in the review process.

[Faros AI](https://www.faros.ai/blog/ai-productivity-paradox-report-2025) found a similar bottleneck across more than 10,000 developers in 2025. Teams with high AI adoption merged 98% more PRs and had 91% longer review times.

## An AI reviewer already in the loop

We already run an AI reviewer on every PR to the main app. It scores each PR from 1 to 5, states a risk level, and comments on lines. 98% of PRs carry a score.

Median time from ready to first score is 6 minutes, against 1.7 weekday hours to the first human approval.

552 PRs that the reviewer first scored 3 or lower reached 4 or 5 after further pushes. Humans left review comments on roughly 350 PRs and formally requested changes on about 40. A score increase and a human comment measure different things. Neither count tells us how many defects were fixed.

The bot also scores again after every push. Our human approvals stay valid after new commits.

In our workflow, I think AI reviewers are now far better than us at this job.

## Who sets the risk label

The proposed rule leans on risk:low, so I checked who sets it. 69% of risk labels are applied under the author's account, mostly by the coding agent that opened the PR, seconds after opening it. The agent is grading its own homework.

On the 1,865 PRs where both the author and the reviewer stated a level, they agreed about 77% of the time. The reviewer rated higher about 22% of the time and lower about 2%. When the reviewer raised a risk:low PR to medium, that PR needed a follow-up fix more often. One reverted PR that would have qualified on the author's low-risk label alone sits in that group.

The proposed policy would keep the higher assessment. A label a person set would never be lowered. A label the reviewer set on an earlier commit would be replaced when it re-reviews. A mistaken escalation costs another human review; a mistaken low-risk classification can let a defect through.

## The approval rule I'm proposing

The initial proposal would let the reviewer approve a PR when all of these hold:

- risk:low, confirmed by the reviewer
- review score 5 on the head commit
- no sensitive path, including migrations

Everything else would wait for a human. A score of 4 would be a later expansion, after evaluation.

I'd start without a fixed size cap. I argued in May that [the small PR rule won't survive AI](/blog/2026/05/19/your-small-pr-rule-wont-survive-ai/), and line count is a poor proxy for risk when an agent writes the diff. [Rewind](https://rewind.com/blog/ai-approve-pull-requests-safely/) also grades by risk, but sends diffs over roughly 10,000 lines to a human because of review capacity. Our proposal would require a complete review: a truncated diff, failed review or incomplete result would go to a person.

## What the historical check missed

The historical analysis tested a broader version of the rule: a score of 4 or 5, without the sensitive-path exclusions. Nineteen PRs qualified under that version despite human pushback. The AI fully raised the same issue once and partly raised four. It missed three substantive issues. The other eleven were style, preference, or not about code.

Two of the three substantive misses touched a migration or authentication code, so the proposed path exclusions would send them to a human. The third was large and wasn't excluded by those paths. A size cap would have kept it with a human. Keeping no size cap means accepting that this kind of miss may recur. The historical check doesn't establish how the narrower score-5 rule would perform.

Two PRs in the window were traced as the cause of an incident. Both were risk:high, touched sign-in code, and had a human approval with no comment. The proposed path exclusions would have sent both to a human. Two cases give us a limited check on those exclusions.

## Reliability is the job

We build incident management. When our customers are down, Rootly is how they page their on-call and run the response. If we break, we break during someone else's worst hour. So shipping faster only counts if reliability doesn't move.

The approval record leaves little evidence of what reviewers checked. Tests, staged deploys and feature flags remain necessary, whichever reviewer approves a change. These are the safeguards I'd require before enabling automatic approval:

**Humans own the policy.** The model supplies a risk assessment, score and findings. A deterministic rule checks eligibility, but still depends on the model's judgment. Changes to the policy and review instructions would require human review.

**Sensitive paths require a person.** Migrations, authentication and permissions, billing, CI and deploy config, dependency changes. No score would override those exclusions.

**Approval belongs to a commit.** A new push would invalidate the bot's approval and require a fresh, complete review.

**The deploy path keeps its existing gates.** An auto-approved PR would go through the same CI, staged rollout and feature flags as any other.

**Misses get counted.** We'd track reverts, follow-up fixes within seven days, incidents linked to auto-approved PRs, and human disagreements found through monthly sampling. A human-review label and a single off-switch would be requirements. A serious incident linked to an auto-approved PR would suspend the policy until we understood why.

The hoped-for benefit is fewer routine approvals, leaving more human attention for changes to sensitive code and findings the reviewer escalates. We haven't measured that benefit yet.

## What other teams have tried

[Rewind](https://rewind.com/blog/ai-approve-pull-requests-safely/) set 90% human agreement as its threshold for going live. Its early results were about 99% agreement on bot approvals that also received human review, with around 40% of PRs classified for auto-approval. It calls those numbers directional. [Ona](https://ona.com/stories/auto-approving-low-risk-prs) saw median time to first approval drop from almost three hours to under four minutes, though it changed two other things at the same time.

[Intercom](https://ideas.fin.ai/p/ai-is-approving-our-pull-requests) reports over 19% of PRs auto-approved without a human reviewer. Its AI-authored backend code had a 0.53% revert rate, against 5.39% for human-authored code. Those authorship figures don't isolate the effect of automatic approval.

Ona keeps a human clicking merge, and Rewind requires one for agent-authored PRs. Our proposal would allow a qualifying PR to go through the deploy pipeline without a human merge step. That needs evaluation beyond whether the bot writes a useful review.

## Where we are

The setting that would record the bot's would-be decisions isn't live. The first step is to record those decisions in shadow mode while keeping human approval required.

We need the PR count, eligible share, human disagreements and substantive misses for the score-5 rule before enabling it. A score of 4 and expansion to other repos would come later, after evaluation.

## The compliance question

Can a bot approve a change and still pass a SOC 2 audit?

The change management criterion, [CC8.1](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022), covers authorization, development, documentation, testing, approval and implementation of changes. Our current process calls for review by someone other than the author. Automatic approval would change that control, so the policy needs to be documented and assessed before it runs.

Every one of the 3,661 PRs in this dataset has an approval from someone other than the author. That record establishes who approved. It says much less about what they checked.

A report built from GitHub events could answer four questions for each merged PR:

1. Was it approved by someone other than the author?
2. Was the approval attached to the PR's final head before merge?
3. Did required checks pass for the change that shipped?
4. If it bypassed review, who did it and why?

For an auto-approved PR, we'd also need the policy version, reviewer identity, score, findings and risk reasoning. The coding agent that wrote a PR couldn't approve it. The policy would need named owners for the classification rules, overrides and monthly human sampling.

We haven't taken this proposal through an audit. Rewind published its own control mapping, which is useful input, but its human merge requirement matters. We'd need an assessment of our proposed control and the evidence it produces.

## What I don't know yet

Whether the reviewer's agreement with the author holds outside the 51% of PRs where we could measure both.

Whether people trust an approval they didn't give. Sparse written feedback doesn't tell us how people will feel about handing approval to a bot.

Whether the no-size-cap policy holds up. The historical check found a substantive miss that the path exclusions wouldn't catch. We need to count those misses in shadow mode and keep looking for them after any rollout.
