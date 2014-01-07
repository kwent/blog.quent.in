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

