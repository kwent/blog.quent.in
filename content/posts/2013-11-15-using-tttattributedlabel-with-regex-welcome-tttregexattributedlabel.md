---
title: 'Using TTTAttributedLabel with Regex : Welcome TTTRegexAttributedLabel'
date: '2013-11-15T02:03:37'
author: Quentin
categories:
- development
- ios
- mobile
tags:
- ios
- regex
- tttattributedlabel
- tttregexattributedlabel
- uilabel
aliases:
- /index.php/2013/11/using-tttattributedlabel-with-regex-welcome-tttregexattributedlabel/
disqus_identifier: '1967095620'
slug: using-tttattributedlabel-with-regex-welcome-tttregexattributedlabel
---
Hi there !

If you are looking a easy library to use to apply Regex with **[TTTAttributedLabel][1] **from [Mattt Thompson][2], i build a lib called [**TTTRegexAttributedLabel**][3].

## Example

![Screenshot](/assets/wp-content/uploads/2013/11/screenshot.jpg)

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
