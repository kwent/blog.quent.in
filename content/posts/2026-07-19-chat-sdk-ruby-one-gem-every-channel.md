---
aliases:
- /posts/2026/07/19/chat-sdk-ruby-one-gem-every-channel/
categories:
- development
cover: /images/covers/chat-sdk-ruby-one-gem-every-channel.png
date: 2026-07-19 12:00:00
slug: chat-sdk-ruby-one-gem-every-channel
tags:
- ruby
- open-source
- chat-sdk
- ai
- claude-code
title: 'ChatSDK Ruby: One Gem, Every Channel'
---

I just open-sourced [ChatSDK Ruby](https://github.com/rootlyhq/chat-sdk) — a unified SDK for building chat bots across Slack, Teams, Google Chat, Discord, Telegram, Mattermost, Twilio, Messenger, and WhatsApp. Write your bot logic once, deploy it everywhere.

It's inspired by [Vercel's Chat SDK](https://chat-sdk.dev) for TypeScript, but redesigned from scratch with idiomatic Ruby patterns. Not a fork — a ground-up reimplementation with a block-based cards DSL, pluggable adapters, and a streaming system that feels natural in Ruby.

## The problem

At [Rootly](https://rootly.com), we build incident management software. Our customers use Slack, Teams, Google Chat — sometimes all three. Every time we add a platform, we face the same question: how much of our bot logic do we rewrite?

The answer should be zero.

But existing Ruby chat libraries are platform-specific. `slack-ruby-client` is excellent for Slack. There's nothing equivalent for Teams or Google Chat. And there's definitely no abstraction layer that lets you write a handler once and have it work across all of them.

So we built one.

## What it looks like

Here's an incident bot that works on both Slack and Teams — the kind of thing we'd build at Rootly:

```ruby
require "chat_sdk"
require "chat_sdk/slack"
require "chat_sdk/teams"

bot = ChatSDK::Chat.new(
  user_name: "incident-bot",
  adapters: {
    slack: ChatSDK::Slack::Adapter.new,
    teams: ChatSDK::Teams::Adapter.new(
      app_id: ENV["TEAMS_APP_ID"],
      app_password: ENV["TEAMS_APP_PASSWORD"]
    )
  },
  state: ChatSDK::State::Redis.new(url: ENV["REDIS_URL"])
)

bot.on_new_mention do |thread, message|
  thread.post("Incident acknowledged. I'll track updates in this thread.")
  thread.subscribe
end

bot.on_subscribed_message do |thread, message|
  thread.post("Noted. Added to the timeline.")
end
```

That handler fires on Slack mentions and Teams @-mentions. Same code, same data structures, same `thread.post` call. The `subscribe` call means every follow-up message in that thread gets routed to `on_subscribed_message` — a natural fit for incident timelines where context accumulates over time.

## Built with AI, in days not months

Before I go deeper into features — some context on how this exists at all.

This entire SDK — 13 gems, 708 specs, a [documentation site](https://chat-sdk.ai), CI pipeline, OIDC gem publishing, Rails demo app — was built in a single extended session with [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

Not "AI-assisted" in the marketing sense. The architecture was designed collaboratively, adapters were generated in parallel by subagents, specs were written alongside the implementation, and `/simplify` passes cleaned up the code after each major feature landed.

Building nine platform adapters with proper webhook verification, card rendering, and comprehensive specs would have taken months of solo work. With Claude Code orchestrating parallel agents, it took days. The SDK exists because AI made it feasible for one person to build what would normally require a team.

## Why not just use slack-ruby-client?

Fair question. `slack-ruby-client` is great — ChatSDK actually uses it under the hood for the Slack adapter. Same for `google-apps-chat-v1` powering the Google Chat adapter.

The difference is the abstraction layer on top. If you're building a Slack-only bot, use `slack-ruby-client` directly. But if you need to support multiple platforms — or you think you might in the future — ChatSDK saves you from maintaining parallel implementations of the same bot logic.

[Lita](https://www.lita.io/) tried to solve this years ago, but it hasn't been actively maintained and doesn't cover modern platforms like Teams, Discord, or WhatsApp. ChatSDK is a fresh take with current platform APIs.

## Cards that render everywhere

Rich messages are the hardest part of cross-platform bots. Slack uses Block Kit JSON. Teams uses Adaptive Cards. Google Chat uses Card V2. Discord uses embeds. Telegram uses inline keyboards. They're all different formats expressing the same concepts.

ChatSDK has a block-based DSL that compiles to all of them:

```ruby
card = ChatSDK.card(title: "Incident INC-2847") do
  text "Payment processing is degraded. Error rate at 12%."
  fields do
    field "Severity", "SEV-1"
    field "Status", "Investigating"
    field "Commander", "Sarah Chen"
    field "Started", "14:23 UTC"
  end
  actions do
    button "Acknowledge", id: "ack"
    button "Escalate", id: "escalate"
    link_button "Status Page", url: "https://status.example.com"
  end
end

thread.post(card)
```

On Slack, that's Block Kit. On Teams, Adaptive Cards. On Discord, an embed with action rows. On Telegram, a message with inline keyboard buttons. Same Ruby object, different renderers, zero platform-specific code.

## Interactive buttons — same handler, every platform

When someone clicks "Acknowledge" or "Escalate" on that card, the handler is platform-agnostic:

```ruby
bot.on_action("ack") do |event|
  event.thread.post("Acknowledged by #{event.user.name}")
end

bot.on_action("escalate") do |event|
  event.thread.post(ChatSDK.card(title: "Escalation") do
    text "Paging on-call SRE team..."
    fields do
      field "Escalated by", event.user.name
      field "Time", Time.now.utc.strftime("%H:%M UTC")
    end
  end)
end
```

Block Kit interactive payloads, Adaptive Card action submits, Discord button clicks, Telegram callback queries — they all arrive as the same `Action` event with the same `action_id`.

## Streaming AI responses

Token-by-token streaming is table stakes for AI-powered bots. Imagine an incident bot that summarizes a thread on demand:

```ruby
bot.on_new_mention do |thread, message|
  next unless message.text.include?("summarize")

  history = thread.fetch_messages(limit: 50)

  thread.post_stream(placeholder: "Analyzing incident timeline...") do |stream|
    # Works with any OpenAI-compatible client (RubyLLM, ruby-openai, etc.)
    ai_client.chat(
      messages: [
        {role: "system", content: "Summarize this incident timeline concisely."},
        {role: "user", content: history.map(&:text).join("\n")}
      ]
    ) do |chunk|
      stream << chunk.dig("choices", 0, "delta", "content")
    end
  end
end
```

The SDK posts a placeholder message, then edits it with accumulated tokens at a throttled interval. Works on any platform that supports message editing — Slack, Teams, Google Chat, Mattermost, Discord, Telegram.

## Notifications across channels

Incidents don't live in one platform. Sometimes you need to fan out alerts to wherever your teams are:

```ruby
def broadcast_incident(bot, incident)
  card = ChatSDK.card(title: "New Incident: #{incident.title}") do
    text incident.summary
    fields do
      field "Severity", incident.severity
      field "Service", incident.service
    end
    actions do
      button "Join Response", id: "join_#{incident.id}"
      link_button "View in Rootly", url: incident.url
    end
  end

  # Same card, rendered natively on each platform
  bot.channel(slack_channel_id, adapter_name: :slack).post(card)
  bot.channel(teams_channel_id, adapter_name: :teams).post(card)
  bot.channel(gchat_space_id, adapter_name: :gchat).post(card)
end
```

One card object, three platforms, three native renderings. No if/else chains, no format conversion code.

## Nine adapters, four state backends

The SDK ships 13 gems total:

**Platform adapters** — Slack, Teams, Google Chat, Mattermost, Discord, Telegram, Twilio SMS, Facebook Messenger, WhatsApp. Each handles webhook verification, event parsing, and message formatting for its platform.

**State backends** — Memory (built-in), Redis, PostgreSQL, MySQL. State handles thread subscriptions, distributed locks, event deduplication, and key-value storage. Swap backends without changing bot logic.

Every adapter implements the same contract. Every state backend passes the same shared spec. `bundle exec rspec` runs 708 specs across all of them.

## Get started

```ruby
# Gemfile
gem "chat_sdk"
gem "chat_sdk-slack"  # pick your platform(s)
```

- **Docs**: [chat-sdk.ai](https://chat-sdk.ai)
- **Source**: [github.com/rootlyhq/chat-sdk](https://github.com/rootlyhq/chat-sdk)
- **RubyGems**: [rubygems.org/gems/chat_sdk](https://rubygems.org/gems/chat_sdk)

It's MIT-licensed, experimental, and looking for early adopters. If you're building chat bots in Ruby and tired of maintaining platform-specific code — try it, break it, [open an issue](https://github.com/rootlyhq/chat-sdk/issues).
