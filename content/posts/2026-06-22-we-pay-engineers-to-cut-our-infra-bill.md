---
aliases:
- /posts/2026/06/22/we-pay-engineers-to-cut-our-infra-bill/
categories:
- development
cover: /images/covers/we-pay-engineers-to-cut-our-infra-bill.png
date: 2026-06-22T08:00:00-0700
slug: we-pay-engineers-to-cut-our-infra-bill
tags:
- finops
- cost-optimization
- engineering-culture
- infrastructure
title: We Pay Engineers to Cut Our Infra Bill
---

One engineer at [Rootly](https://rootly.com) added lifecycle policies to our ECR repositories. 95% of them had no cleanup policy. Container image storage was trending from $3K to $7.6K per month. A few PRs later, we were saving roughly $44K a year.

Their reward? A thumbs-up emoji in Slack.

This bothered me. Not because the recognition was bad. People genuinely appreciated the work. But the incentive structure was broken. Finding and shipping cost savings requires initiative, cross-team coordination, and real engineering work. It carries risk. And at most companies, it's treated like volunteer work.

## The side-quest problem

Engineers notice waste constantly. An S3 bucket with no expiration policy. CI pipelines running on oversized instances. NAT gateway costs that nobody's looked at since the initial setup.

Most of the time, nothing happens. The engineer files a ticket, maybe mentions it in a retro, and moves on. The ticket sits in a backlog behind feature work because feature work has deadlines, stakeholders, and OKRs attached to it. Cost optimization has none of those things.

The few engineers who do push through, who build the case, write the PR, coordinate the rollout, get a "nice catch" in standup. Maybe a shoutout in the next all-hands. Then they go back to sprint work.

The message is clear even if nobody says it out loud: shipping features is real work. Saving money is extra credit.

## What others have tried

The [FinOps Foundation](https://www.finops.org/wg/encouraging-engineers-to-take-action/) found that 40% of organizations say getting engineers to act on cost optimization is their number one FinOps challenge. The industry has answers. None of them felt right for us.

Amazon has "Frugality" as a leadership principle and hands out the [Door Desk Award](https://www.aboutamazon.com/news/workplace/how-a-door-became-a-desk-and-a-symbol-of-amazon) for ideas that create significant savings. Cultural, but no cash tied to the savings themselves.

Spotify built [Cost Insights into Backstage](https://backstage.io/blog/2020/10/22/cost-insights-plugin/) so engineers could see cloud spend in their normal workflow. They cut cloud spend by millions. But the reward is visibility, not a paycheck.

GitLab ran a contest with visible team rankings and [cut Kubernetes costs by 10%](https://www.cloudzero.com/blog/gamified-finops/). General Mills launched a monthly "FinOps Allstar" recognition and went from one team caring about costs to twenty.

Gamification gets attention. But the next sprint starts, priorities shift, and cost optimization goes back to being a side-quest. We wanted something more durable.

## We decided to pay people

We created a program called **Save & Share**. Save Rootly money on infrastructure or SaaS, get a cash bounty based on a percentage of the annualized savings.

No special role required. Anyone at the company can submit. Engineers, SREs, EMs, ops, finance. If you find the savings and ship the fix, you get paid.

## How it works

The bounty is a tiered percentage of verified annualized savings:

| Annualized Savings | Bounty % | Example Payout |
|---|---|---|
| $5K – $25K | 5% | $250 – $1,250 |
| $25K – $100K | 7% | $1,750 – $7,000 |
| $100K – $250K | 10% | $10K – $25K |
| $250K+ | 12% | $30K+ |

There's a floor: savings must hit at least $5K annualized to qualify. And a cap: the lesser of 15% of your base salary or $50K per year.

Co-authors split the bounty. Default is 70/30, but submitters can configure the split however they want.

**What counts:** AWS spend (ECR, S3, RDS, EC2, NAT, CloudWatch, data transfer, Lambda), SaaS line items (Datadog, Sentry, Heroku, third-party APIs), CI/build minutes, per-customer infra waste.

**What doesn't:** savings from churn or product sunset, vendor renegotiations owned by procurement, naturally decaying usage, or "saved by not building it." No baseline means no bounty.

## Verification

This is the part that makes it real and not just a poster on the wall.

1. **Submit before you merge.** File a submission with your hypothesis, baseline cost, implementation PRs, expected savings, and co-authors. No retro claims.
2. **Baseline lock.** Trailing 90-day average of the affected line items at submission time.
3. **Realization window.** 90 days post-deploy. We watch the actual numbers.
4. **Sign-off.** CTO and Finance jointly verify the realized delta against AWS Cost Explorer or the vendor invoice.
5. **Payout.** Next payroll cycle after sign-off.

Annualized savings = realized 90-day post-deploy delta × 4.

## Anti-gaming

We thought about the ways this could go wrong.

- **No retro claims.** Submission must happen before the optimization PR merges.
- **No double-dip.** Same line item can't be re-claimed within 12 months.
- **Reversal clause.** Bounty reversed if the optimization gets rolled back within 90 days.
- **Quality bar.** Bounty forfeited if the change causes a Sev-2+ incident within 90 days.
- **No artificial inflation.** You can't over-provision something on purpose and then "save" it. Manager and Finance review every submission.

If cost optimization is already your explicit job duty, your manager has to confirm the work is above and beyond normal scope.

## The first payout

We backdated the ECR lifecycle policy win as the inaugural bounty. ~$44K annualized savings at the 7% tier comes out to roughly $3,080.

This was intentional. The fastest way to kill a program like this is to launch it with a memo and no money. We wanted the first signal to be clear: this is real. Someone did the work, the numbers checked out, they got paid.

## The point isn't the money

The bounty matters. But what we're building is a culture where cost optimization carries the same weight as feature work. Where finding $44K in annual savings isn't a footnote in a retro. It's something you submitted, verified, and got recognized for through a process that treats it as legitimate engineering output.

Most companies say they care about costs. Few make it worth anyone's time to act on that.

The full program spec is open. Steal it. Adjust the tiers, change the cap, adapt the verification process to your stack. The specific numbers matter less than the principle: if you want engineers to optimize costs, make it worth their while.
