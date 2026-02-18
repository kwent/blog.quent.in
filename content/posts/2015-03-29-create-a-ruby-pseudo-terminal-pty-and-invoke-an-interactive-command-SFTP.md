---
title: Create a ruby pseudo terminal (PTY) and invoke an interactive command (SFTP)
date: 2015-03-29T22:37:51-0700
categories:
- development
- ruby
- system
tags:
- pty
- ruby
- sftp
- cli
slug: create-a-ruby-pseudo-terminal-pty-and-invoke-an-interactive-command-sftp
aliases:
  - /blog/2015/03/29/create-a-ruby-pseudo-terminal-pty-and-invoke-an-interactive-command-SFTP/
---

## Purpose

I needed to upload files on a **SFTP server** **programmatically** and **automatically** in
a RoR Enviroment. SFTP ruby library wrapper are very limited (I only found
[this one][2] actually) and is in **maintenance (not more maintained)**
and I had some troubles uploading large files.

Anyway I decided to come back to use the old [SFTP Command Line Interface][3]
who is perfectly working.

Unlucky this one is an **Interactive** CLI.

The trick is to use a [Ruby Pseudo Terminal (PTY)][1], listen to the console
input for some patterns and write in the console output according this pattern
as a real user would do.

Here is a code snippet who doing the job and working perfectly.

## Code

```ruby
require 'pty'
require 'expect'

PTY.spawn('sftp username@sftp.domain.com:/uploads') do |input, output|

  # Say yes to SSH fingerprint
  input.expect(/fingerprint/, 2) do |r|

    output.puts "yes" if !r.nil?

    # Enter SFTP password
    input.expect(/password/, 2) do |r|

      output.puts 'your_sftp_password' if !r.nil?

      input.expect(/sftp/) do

        # List folders and files in `/uploads`
        output.puts 'ls'

        # Check if folder named `foo` exist
        input.expect(/foo/, 1) do |result|

          is_folder_exist = result.nil? ? false : true
          # Create `foo` folder if does'nt exist
          output.puts "mkdir foo" if !is_folder_exist
          # Change directory to `foo`
          output.puts "cd foo"
          # Upload `/path/to/local/foo.txt` in `foo` folder as `foo.txt`
          output.puts "put /path/to/local/foo.txt foo.txt"
          # Exit SFTP
          output.puts "exit"

        end

      end

    end

  end

end
```

## Gist

Available [here][4]. Please feel free to improve it !

## More...

- [PTY][1]
- [Net::SFTP][2]
- [man SFTP][3]

[1]: http://ruby-doc.org/stdlib-2.2.0/libdoc/pty/rdoc/PTY.html
[2]: https://github.com/net-ssh/net-sftp
[3]: http://linux.die.net/man/1/sftp
[4]: https://gist.github.com/kwent/e2c34c2dfd01a194a49a