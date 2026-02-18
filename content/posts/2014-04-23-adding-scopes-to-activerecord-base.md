---
aliases:
- /posts/2014/04/23/adding-scopes-to-activerecord-base/
author: Quentin
categories:
- development
- rails
- ruby
cover: /images/covers/adding-scopes-to-activerecord-base.png
date: 2014-04-23T19:00:08-0800
slug: adding-scopes-to-activerecord-base
tags:
- activerecord
- scopes
- rails
- ruby
title: Adding scopes to ActiveRecord::Base
---

## Purpose

If you are using many times `created_at` and `updated_at` attributes and you're
playing a lot with them in you queries, you should be interesting by this
**MonkeyPatch** who is
adding useful scopes in every models who inherits from `ActiveRecord::Base`.

## MonkeyPatch

- Create `app/initializer/active_record_scopes_extension.rb` file and add the 
code below.
- Call `MyModel.created(DateTime.now)` or `MyModel.updated(3.days.ago)` or 
`MyModel.created(2.day.ago, 1.day.ago)`.

```ruby
module Scopes
  def self.included(base)
    base.class_eval do
      def self.created(date_start, date_end = nil)
          if date_start && date_end
            scoped(:conditions => ["#{table_name}.created_at >= ? AND #{table_name}.created_at <= ?", date_start, date_end])
          elsif date_start
            scoped(:conditions => ["#{table_name}.created_at >= ?", date_start])
          end
      end
      def self.updated(date_start, date_end = nil)
          if date_start && date_end
            scoped(:conditions => ["#{table_name}.updated_at >= ? AND #{table_name}.updated_at <= ?", date_start, date_end])
          elsif date_start
            scoped(:conditions => ["#{table_name}.updated_at >= ?", date_start])
          end
      end
    end
  end
end

ActiveRecord::Base.send(:include, Scopes)
```