---
author: Quentin
categories:
- development
- script
- system
cover: /images/covers/export-all-mixpanel-people-to-a-json-file.png
date: 2014-07-15T13:32:01-0700
slug: export-all-mixpanel-people-to-a-json-file
tags:
- mixpanel
- database
- backup
- export
- api
title: Export all Mixpanel People to a JSON file
---

## Purpose

I needed to backup all my people data available in [Mixpanel][1] to a JSON file via the [Mixpanel Export API][2].

## Script

```ruby
#==========================================================================================
#title           :mixpanel_people_export.rb
#description     :This ruby script is exporting mixpanel people json data to a file
#author          :Quentin Rousseau <contact@quent.in>
#date            :2014-07-15
#version         :1.0
#usage           :ruby mixpanel_people_export.rb
#dependencies    :gem install 'mixpanel_client'
#moreinfo        :https://mixpanel.com/docs/api-documentation/data-export-api#engage-default
#===========================================================================================

require 'rubygems'
require 'mixpanel_client'

API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
NAME_FILE = 'mixpanel_people_export.json'

$client = Mixpanel::Client.new(api_key: API_KEY, api_secret: API_SECRET)
json_file = File.open(NAME_FILE, 'a')

# Open json array
json_file.write('[')

def query_api(page = 0, session_id = nil)
  if(session_id)
    data = $client.request('engage', page: page, session_id: session_id)
  else
    data = $client.request('engage', page: page)
  end
end

# Get the first page of data associated with our selector expression
# this_page = query_api(page=NEXT_PAGE)
# do_something_with_response(this_page)

this_page = query_api(0)
json_file.write(this_page.to_json)

# If we get fewer records than the page_sized returned with our results,
# then there are no more records to get. Otherwise, keep querying for additional pages.
# while (length of this_page.results) >= this_page.page_size:
#     next_page_number = this_page.page + 1
#     this_page = query_api(page=next_page_number, session_id=this_page.session_id)
#     do_something_with_response(this_page)

while (this_page and this_page['results'].size > 0)
  next_page_number = this_page['page'].to_i + 1
  puts "Fetching next_page : #{next_page_number}"
  this_page = query_api(next_page_number, this_page['session_id'])
  json_file.write("," + this_page.to_json)
end

# Close json array
json_file.write(']')

puts "Export done"
```

## Gist

Available [here](https://gist.github.com/kwent/4cc0ca8cf0c682bcef4e). Please feel free to improve it !

## More...

- [Mixpanel][1]
- [Mixpanel Engage API][2]

[1]: http://www.mixpanel.com
[2]: https://mixpanel.com/docs/api-documentation/data-export-api#engage-default