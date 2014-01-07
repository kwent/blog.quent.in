# Title: Twitter mention Plugin For Octopress
# Author: Quentin Rousseau http://quentinrousseau.com
# Description: Convert all twitter mention with an url.
#
# Syntax {% twitter_text "You string with mention" %}
#
# Example:
# {% twitter_text "Hello world @quentinrousseau" %}
#
# Output:
# <a href="https://twitter.com/quentinrousseau" alt="@quentinrousseau">@quentinrousseau</a>
#

module Jekyll

  class TwitterText < Liquid::Tag

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

Liquid::Template.register_tag('twitter_text', Jekyll::TwitterText)

