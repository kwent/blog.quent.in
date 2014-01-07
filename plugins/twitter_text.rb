# Title: Simple Video tag for Jekyll
# Author: Brandon Mathis http://brandonmathis.com
# Description: Easily output MPEG4 HTML5 video with a flash backup.
#
# Syntax {% video url/to/video [width height] [url/to/poster] %}
#
# Example:
# {% video http://site.com/video.mp4 720 480 http://site.com/poster-frame.jpg %}
#
# Output:
# <video width='720' height='480' preload='none' controls poster='http://site.com/poster-frame.jpg'>
#   <source src='http://site.com/video.mp4' type='video/mp4; codecs=\"avc1.42E01E, mp4a.40.2\"'/>
# </video>
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

