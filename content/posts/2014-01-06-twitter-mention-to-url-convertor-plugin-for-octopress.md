---
title: Twitter mention to url convertor plugin for Octopress
date: 2014-01-06T23:28:42-0800
categories:
- development
- web
- octopress
- script
tags:
- octopress
- jekyll
- plugin
- twitter
- mention
slug: twitter-mention-to-url-convertor-plugin-for-octopress
---

Today i needed to convert a string like ``"Hello world @quentinrousseau"`` to an **html** string like with the **Twitter mention** decoded with a real link for **Octopress**.

There is a gem called **twitter_text** who is already doing this stuff available here : [https://github.com/twitter/twitter-text-rb][1].

But it was too **overkilled** for my decoding in my case only the mention.

So i developped this little **plugin** for **Octopress** who is doing the stuff well and simple.

**Gist** available here : [https://gist.github.com/kwent/8295854][2]

```ruby
# Title: Twitter mention to url convertor plugin for Octopress
# Author: Quentin Rousseau http://quentinrousseau.com
# Description: Convert all twitter mentions with an url.
#
# Syntax {% twitter_mention_convertor "You string with @mention1 @mention2" %}
#
# Example:
# {% twitter_mention_convertor "Hello world @quentinrousseau" %}
#
# Output:
# <a href="https://twitter.com/quentinrousseau" alt="@quentinrousseau">@quentinrousseau</a>
#

module Jekyll

  class TwitterMentionConvertor < Liquid::Tag

    @twitter_base_uri = nil

    def initialize(tag_name, markup, tokens)
      super
      @twitter_base_uri = "https://twitter.com/"
    end

    def render(context)
      "#{context[@markup.strip]}".gsub(/@([a-z0-9_]+)/i) do |mention|
        "<a href=\"#{@twitter_base_uri}#{mention[1..-1]}\" alt=\"#{mention}\">#{mention}</a>"
      end
    end

  end

end

Liquid::Template.register_tag('twitter_mention_convertor', Jekyll::TwitterMentionConvertor)
```

Enjoy !

## More...

- [twitter_text Gem][1]
- [Gist Code][2]

[1]: https://github.com/twitter/twitter-text-rb
[2]: https://gist.github.com/kwent/8295854