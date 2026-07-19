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

At [Rootly](https://rootly.com), we've been building incident management bots for years. Slack first, then Teams, then Google Chat. Every time a customer asked for a new platform, we'd look at the handler code we'd already written and think: this logic is identical. The only thing that changes is how the platform wants it formatted.

That got old fast.

So I built [ChatSDK Ruby](https://github.com/rootlyhq/chat-sdk) — a unified SDK that lets you write one bot and deploy it across nine platforms. It's open-source as of today.

## The thing that finally pushed me

Last month, a customer asked for Google Chat support. I opened our Slack bot codebase, looked at the incident acknowledgment handler, the escalation flow, the status card — and realized I was about to copy-paste 400 lines of Ruby into a new file, swap out the API calls, and maintain two parallel implementations forever.

I'd done this before. Slack to Teams was painful enough. Each platform has its own webhook format, its own card schema, its own way of handling buttons. The bot logic — "when someone mentions me, acknowledge the incident and subscribe to the thread" — was the same every time. The plumbing was different.

I knew about [Vercel's Chat SDK](https://chat-sdk.dev) for TypeScript. I liked the API design. But we're a Ruby shop, and there was nothing equivalent in the Ruby ecosystem.

## What it actually looks like

Here's the incident bot I described above, working on both Slack and Teams simultaneously:

```ruby
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

Same handler, both platforms. The `subscribe` call means every follow-up message in that thread gets routed to `on_subscribed_message` — which is exactly how incident timelines work. Context accumulates in the thread, and the bot follows along.

## How this was built

I'll be honest — this project exists because of [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

13 gems. 708 specs. A [documentation site](https://chat-sdk.ai). CI pipeline. OIDC publishing for all gems. A Rails demo app. Nine adapters with proper webhook verification, card rendering, and comprehensive tests. I built this in days, not months.

The architecture was designed collaboratively. Adapters were generated in parallel by subagents — one agent building the Discord adapter while another was writing the Telegram one. Specs were written alongside the implementation. `/simplify` passes cleaned up the code after each feature landed.

It's still experimental — there are edge cases I haven't hit yet and platform quirks waiting to be discovered. That's why it's marked beta. But the sheer volume — nine platforms, each with their own webhook format, card schema, event structure, and auth mechanism — would have been months of solo work without AI. I know because I've done this work manually before at Rootly, one platform at a time.

## The cards DSL is the thing I'm most proud of

This is where the abstraction really earns its keep. Slack uses Block Kit. Teams uses Adaptive Cards. Google Chat uses Card V2. Discord uses embeds. Telegram uses inline keyboards. Five completely different JSON formats expressing the same concepts: title, fields, buttons.

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

One Ruby object. Nine renderers. Each produces the platform's native card format. No one sees generic markup — Slack users get Block Kit, Teams users get Adaptive Cards, Discord users get embeds. And when someone clicks "Acknowledge":

```ruby
bot.on_action("ack") do |event|
  event.thread.post("Acknowledged by #{event.user.name}")
end
```

Block Kit interactive payloads, Adaptive Card action submits, Discord button clicks, Telegram callback queries — they all arrive as the same `Action` event with the same `action_id`. I don't have to care where the click came from.

## Streaming AI summaries

We're increasingly using LLMs in incident workflows — summarizing threads, suggesting runbooks, drafting postmortems. Streaming those responses token-by-token is a much better experience than waiting 10 seconds for a wall of text:

```ruby
bot.on_new_mention do |thread, message|
  next unless message.text.include?("summarize")

  history = thread.fetch_messages(limit: 50)
  timeline = history.map { |m| "#{m.author.name}: #{m.text}" }.join("\n")

  thread.post_stream(placeholder: "Analyzing incident timeline...") do |stream|
    RubyLLM.chat(model: "claude-sonnet-5")
      .ask("Summarize this incident timeline concisely:\n\n#{timeline}") do |chunk|
        stream << chunk.content
      end
  end
end
```

The SDK posts a placeholder, then edits it with accumulated tokens at a throttled interval. Works on any platform that supports message editing.

## Broadcasting across platforms

Most of our customers use one primary chat tool — Slack or Teams or Google Chat. But incidents often need to reach people outside of chat. The on-call engineer who's away from their laptop. The VP who needs a heads-up via SMS.

ChatSDK makes this natural because Twilio is just another adapter:

```ruby
def notify_incident(bot, incident, on_call_phone:)
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

  # Rich card in Slack, plain text fallback via SMS
  bot.channel(slack_channel_id, adapter_name: :slack).post(card)
  bot.channel(on_call_phone, adapter_name: :twilio).post(card)
end
```

The card renders as Block Kit in Slack. The same card object hits Twilio and falls back to a clean text summary — severity, service, a link to the status page. One card, two channels, zero format conversion code.

## Why not slack-ruby-client or Lita?

If you're building a Slack-only bot, use `slack-ruby-client` directly — it's excellent. ChatSDK actually uses it under the hood for the Slack adapter.

The value is the abstraction layer. When you need to support multiple platforms — or you suspect you will — ChatSDK saves you from maintaining parallel implementations of the same bot logic.

[Lita](https://github.com/litaio/lita) tried to solve this years ago, but it hasn't seen a release since 2018 and its website is gone. It also doesn't cover modern platforms like Teams, Discord, or WhatsApp. ChatSDK is a fresh take with current APIs.

## What ships today

13 gems, all on RubyGems:

- **9 platform adapters**: Slack, Teams, Google Chat, Mattermost, Discord, Telegram, Twilio SMS, Messenger, WhatsApp
- **4 state backends**: Memory, Redis, PostgreSQL, MySQL
- 708 specs across all gems, multi-Ruby CI (3.3, 3.4, 4.0)
- Full docs at [chat-sdk.ai](https://chat-sdk.ai)

Every adapter implements the same contract. Every state backend passes the same shared spec. Every card renders natively on every platform.

## Try it

```ruby
gem "chat_sdk"
gem "chat_sdk-slack"  # pick your platform(s)
```

- **Docs**: [chat-sdk.ai](https://chat-sdk.ai)
- **Source**: [github.com/rootlyhq/chat-sdk](https://github.com/rootlyhq/chat-sdk)
- **RubyGems**: [rubygems.org/gems/chat_sdk](https://rubygems.org/gems/chat_sdk)

It's MIT-licensed and experimental. I'm looking for people who are building multi-platform bots in Ruby and are tired of the copy-paste-adapt cycle. Try it, break it, [open an issue](https://github.com/rootlyhq/chat-sdk/issues). I'll be reading every one.
