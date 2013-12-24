---
title: 'Using TTTAttributedLabel with Regex : Welcome TTTRegexAttributedLabel'
author: Quentin
layout: post
comments: true
permalink: /index.php/2013/11/using-tttattributedlabel-with-regex-welcome-tttregexattributedlabel/
hl_twitter_has_auto_tweeted:
  - 'I just posted Using TTTAttributedLabel with Regex : Welcome TTTRegexAttributedLabel, read it here: http://blog.quentinrousseau.fr/?p=662'
dsq_thread_id:
  - 1967095620
categories:
  - Développement
  - iOS
  - Mobile
tags:
  - ios
  - Regex
  - TTTAttributedLabel
  - TTTRegexAttributedLabel
  - UILabel
date: Fri, 15 Nov 2013 02:03:37 -8000
---
Hi there !

If you are looking a easy library to use to apply Regex with **[TTTAttributedLabel][1] **from [Mattt Thompson][2], i build a lib called [**TTTRegexAttributedLabel**][3].

## Example

![Screenshot](/assets/wp-content/uploads/2013/11/screenshot.jpg)[4]

## Usage

**Below a quick example hot to use it ( First example in the Screenshot)**

```objective-c
TTTRegexAttributedLabel *label1 = [[TTTRegexAttributedLabel alloc] initWithFrame:CGRectMake(25, 20, self.view.bounds.size.width - 50, 160)];
label1.numberOfLines = ;
label1.textAlignment = NSTextAlignmentCenter;
NSString *s1 = @“Soft kitty,\nWarm kitty,\nLittle ball of fur.\nHappy kitty,\nSleepy kitty,\nPurr, purr, purr.”;
[label1 setText:s1 withFirstMatchRegex:@“kitty” withFont:[UIFont boldSystemFontOfSize:20] withColor:[UIColor redColor]];
```

Enjoy it !

## More...

*   <a href="https://github.com/kwent/TTTRegexAttributedLabel" title="kwent/TTTRegexAttributedLabel · GitHub" rel="nofollow">kwent/TTTRegexAttributedLabel · GitHub</a>
*   <a href="https://github.com/mattt/TTTAttributedLabel?source=c" title="mattt/TTTAttributedLabel · GitHub" rel="nofollow">mattt/TTTAttributedLabel · GitHub</a>

 [1]: https://github.com/mattt/TTTAttributedLabel
 [2]: http://github.com/mattt
 [3]: https://github.com/kwent/TTTRegexAttributedLabel
