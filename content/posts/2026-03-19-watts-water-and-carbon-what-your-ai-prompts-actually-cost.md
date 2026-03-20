---
aliases:
- /posts/2026/03/19/watts-water-and-carbon-what-your-ai-prompts-actually-cost/
categories:
- technology
cover: /images/covers/watts-water-and-carbon-what-your-ai-prompts-actually-cost.png
date: 2026-03-19 12:00:00
slug: watts-water-and-carbon-what-your-ai-prompts-actually-cost
tags:
- ai
- energy
- data-centers
- sustainability
title: 'Watts, Water, and Carbon: What Your AI Prompts Actually Cost'
---

Every time you ask an AI to summarize a document, generate an image, or write code, a GPU somewhere lights up — and a power meter ticks upward. As someone who runs AI agents all day, I started wondering: what's the actual energy footprint of this revolution I'm participating in?

The answer is more nuanced than the headlines suggest.

## What a single prompt actually costs

Let's start small. You've probably seen the stat that a ChatGPT query uses "10x more energy than a Google search." [The reality is more complicated](https://technical.ly/civics/chatgpt-vs-google-energy-use/). Google's traditional search uses about **0.3 watt-hours**. The Electric Power Research Institute estimated a ChatGPT request at **2.9 Wh** — roughly 10x.

But in August 2025, [Google published actual data](https://www.technologyreview.com/2025/08/21/1122288/google-gemini-ai-energy/) for the first time: a median Gemini query consumes just **0.24 Wh**, and efficiency improved **33x** between May 2024 and May 2025. [More recent analysis from Epoch AI](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) puts a typical GPT-4o query around **0.3 Wh** — nearly comparable to a Google search. These estimates are directional, not perfectly apples-to-apples: model architecture, hardware, traffic patterns, and accounting boundaries all differ.

Not all AI workloads are equal, though. [Research from Hugging Face](https://arxiv.org/abs/2311.16863) found that image generation consumes **5 to 50x more energy** than a text query of comparable length. A single Stable Diffusion image clocks in around 0.7 Wh. Video generation is even hungrier. As multimodal AI explodes, the per-query averages will shift upward even as text gets cheaper.

The per-query cost for text is shrinking fast. But that doesn't mean the total cost is shrinking. This is where it gets interesting.

## Training vs. inference: two different beasts

To understand why energy demand is growing so fast, you need to understand the two fundamentally different ways AI consumes power.

Training a large model — the months-long process of feeding it data — is a sustained, predictable load. It runs 24/7 and benefits from steady baseload power like nuclear. Training GPT-4 consumed an estimated [~50 GWh total](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use).

Inference — actually using the model when you send it a prompt — is bursty. Millions of requests create intense, unpredictable spikes. As [Tom's Hardware noted](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-datacenters-in-the-us-arent-running-on-coal-but-this-dirty-fuel-has-found-favor-for-feeding-demand-spikes-due-to-increased-gas-prices), these spikes stress grid infrastructure and require flexible power sources to absorb.

This distinction matters because inference is growing much faster than training. Every new AI product, every chatbot, every agent running in the background is an inference workload. Training happens once; inference happens millions of times per day.

## The global demand surge

Now let's zoom out. According to [Deloitte](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2025/genai-power-consumption-creates-need-for-more-sustainable-data-centers.html), data centers consumed about **536 TWh globally in 2025** — roughly **2% of the world's electricity**. That sounds manageable until you zoom into the U.S.

[Pew Research](https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/) found that data centers already account for **4% of total U.S. electricity use** in 2024, and that number is **expected to more than double by 2030**. The [IEA projects](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) global data center electricity demand will exceed **1,000 TWh by 2030**, with AI-optimized facilities quadrupling their share. The largest individual data centers now under construction will each consume as much electricity as **2 million households**.

A third of U.S. data centers are concentrated in just three states: Virginia, Texas, and California. In Virginia alone, data centers consumed **26% of the state's total electricity** in 2023.

## Why efficiency won't save us

Here's the counterintuitive part. Per-query costs are plummeting — so shouldn't total energy use be falling too?

In the 1860s, economist William Stanley Jevons observed that as coal engines became more efficient, total coal consumption *increased* — because efficiency made coal cheaper, which drove more usage. [NPR covered how the AI world is now obsessed with this paradox](https://www.npr.org/sections/planet-money/2025/02/04/g-s1-46018/ai-deepseek-economics-jevons-paradox) after DeepSeek showed that cheaper models just mean more people using AI.

A [2025 paper published at ACM FAccT](https://arxiv.org/abs/2501.16548) makes this explicit: efficiency gains in AI hardware lower costs, which spurs demand for new AI functionalities, which drives further hardware upgrades, which increases total energy consumption. As [SIGARCH noted](https://www.sigarch.org/the-jevons-paradox-why-efficiency-alone-wont-solve-our-data-center-carbon-challenge/), efficiency alone won't solve the data center carbon challenge without policy and behavioral changes alongside it.

Each query is getting cheaper. We're just making exponentially more of them.

## The hidden cost: water

Energy gets the headlines, but AI data centers are also incredibly thirsty.

Google published that an average Gemini query consumes **0.26 mL of water**. OpenAI's Sam Altman said a ChatGPT query uses "roughly one fifteenth of a teaspoon." But these numbers are not directly comparable to older estimates. Earlier [research from UC Riverside](https://undark.org/2025/12/16/ai-data-centers-water/) estimated that, depending on location and cooling assumptions, generating **10 to 50 GPT-3 responses** could indirectly consume about **one 500 mL bottle of water**. The range is wide because water use depends heavily on where and when the model is served.

At scale, [Brookings reports](https://www.brookings.edu/articles/ai-data-centers-and-water/) that annual U.S. data center water consumption could **double or quadruple by 2028** compared to 2023 levels — reaching 150-280 billion liters per year. Microsoft's water use already jumped **34% year-over-year** in 2023, driven by AI infrastructure. These facilities are increasingly being built [in water-stressed regions of the American West](https://andthewest.stanford.edu/2025/thirsty-for-power-and-water-ai-crunching-data-centers-sprout-across-the-west/), competing with agriculture and residential use.

## Big Tech's broken climate promises

According to [UN data reported by Al Jazeera](https://www.aljazeera.com/news/2025/6/6/tech-giants-see-emissions-surge-150-percent-in-3-years-amid-ai-boom-un), tech giants saw emissions **surge 150% in three years** amid the AI boom. The breakdown: Amazon's operational emissions grew **182%** since 2020, Microsoft **155%**, Meta **145%**, and Google **138%**.

These are the same companies that pledged to be carbon neutral or carbon negative by 2030. Microsoft's own sustainability report acknowledged the 2030 carbon-negative goal is now [significantly harder to meet](https://energy.policyplatform.news/environment/microsoft-carbon-emissions-jump-ai-and-cloud-demand-rises). Google, which had been carbon neutral since 2007, admitted its 24/7 carbon-free energy target is [increasingly difficult](https://greentechlead.com/sustainability/google-2025-environmental-report-ai-driven-growth-raises-emissions-as-company-accelerates-clean-energy-and-net-zero-strategy-52687).

The response? More carbon credit purchases — [up 181% to 68.4 million carbon credits in 2025](https://www.cnbc.com/2026/03/16/microsoft-carbon-credits-ai-tech-google-meta.html) — while simultaneously spending a combined **$320 billion on AI infrastructure** that same year. As [Accenture warned](https://fortune.com/2025/07/03/accenture-warns-ais-carbon-emissions-could-surge-11-fold-but-big-techs-still-racing-to-build-and-not-slow-down-for-sustainability/), AI's carbon emissions could surge **11-fold** if the industry doesn't change course.

## The nuclear gold rush

To their credit, Big Tech is betting big on nuclear:

- **Microsoft** signed a [20-year deal with Constellation Energy](https://www.technologyreview.com/2024/09/20/1104516/microsoft-three-mile-island-nuclear-energy/) to **restart Three Mile Island Unit 1** (~835 MW), targeting 2028.
- **Google** signed the [world's first corporate PPA](https://blog.google/outreach-initiatives/sustainability/google-kairos-power-nuclear-energy/) for small modular reactors with **Kairos Power** (~500 MW by 2035).
- **Amazon** purchased a data center campus adjacent to the Susquehanna nuclear plant for [~$650 million](https://www.datacenterdynamics.com/en/news/amazon-buys-960mw-nuclear-powered-data-center-campus-from-talen-energy-for-650m/) and invested in **X-energy** for 5+ GW of SMR capacity by 2039.
- **Meta** issued an RFP seeking [1-4 GW of new nuclear generation](https://www.reuters.com/technology/metas-nuclear-ambitions-request-proposals-up-4-gigawatts-power-2024-12-03/).

But as [Goldman Sachs Research](https://www.goldmansachs.com/insights/articles/is-nuclear-energy-the-answer-to-ai-data-centers-power-consumption) notes, nuclear can't meet all the demand alone. And the timelines don't match: these SMRs are years away, while demand is growing now. As [CSIS frames it](https://www.csis.org/analysis/electricity-supply-bottleneck-us-ai-dominance), the central challenge is **speed-to-power** — how fast new sites can access electricity. That urgency favors whatever fuel is available *today*, which often means gas or even coal.

Coal generation in the U.S. rose **nearly 20%** as elevated gas prices pushed utilities back toward dirtier fuels, according to the Jefferies analysis [cited by Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-datacenters-in-the-us-arent-running-on-coal-but-this-dirty-fuel-has-found-favor-for-feeding-demand-spikes-due-to-increased-gas-prices). Even if that proves temporary, it shows how quickly short-term power constraints can push the grid toward dirtier fallback options.

## What this means for us

I think about all of this when I spin up multi-agent workflows that orchestrate half a dozen Claude instances in parallel. Each prompt has a real, if tiny, energy cost. Multiply that across millions of users, and those tiny costs compound into the electricity consumption of small countries.

Does that mean we should stop using AI? No. But we should be honest about the tradeoffs:

- **Transparency matters.** Google publishing Gemini's energy data was a good start. Every AI provider should follow suit.
- **Efficiency is necessary but not sufficient.** Per-query costs are dropping, but Jevons paradox means total consumption keeps rising. We need systemic solutions, not just better chips.
- **The nuclear timeline is too slow.** We need bridge solutions that aren't just "burn more gas and buy carbon credits."
- **As developers, our choices have energy consequences.** Running an agent loop that makes 50 LLM calls when 5 would suffice isn't just wasteful of tokens — it's wasteful of watts and water.

[MIT researchers](https://news.mit.edu/2025/multifaceted-challenge-of-powering-ai-0121) describe powering AI as a "multifaceted challenge" spanning technology, energy, government policy, and consumer impact. The [IEA](https://www.iea.org/reports/energy-and-ai/executive-summary) paints a picture of an industry building demand far faster than it's building supply. The optimistic view is that AI will eventually help optimize the very energy systems it's straining — better grid management, materials science breakthroughs, more efficient chips. The realistic view is that for the next decade, the AI boom will lean on fossil fuels more than anyone wants to admit, and create real tensions between tech growth and climate commitments.

The least we can do is stop pretending the cloud runs on magic. Every inference has a cost — in watts, in water, in carbon. The question is whether we'll be intentional about paying it.
