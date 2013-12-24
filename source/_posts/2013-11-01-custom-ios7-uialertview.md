---
title: Custom iOS7 UIAlertView
author: Quentin
layout: post
comments: true
permalink: /index.php/2013/11/custom-ios7-uialertview/
hl_twitter_has_auto_tweeted:
  - 'I just posted Custom iOS7 UIAlertView, read it here: http://blog.quentinrousseau.fr/?p=657'
dsq_thread_id:
  - 1927300841
categories:
  - Développement
  - iOS
  - Mobile
tags:
  - alertview
  - custom
  - dialog
  - flat
  - ios
  - ios7
date: Fri, 01 Nov 2013 17:11:50 -8000
---
I forked &laquo;&nbsp;ios-custom-alertview&nbsp;&raquo; from [@wimagguc][1] and added a different design button this week.

You can just [grab the open source code from Github now][2].

[<img class="aligncenter size-full wp-image-658" alt="Ios Custom AlertView" src="http://blog.quentinrousseau.fr/wp-content/uploads/2013/11/screen.png" />][3] 
&nbsp;

Implementation of this alert view is :

```objective-c
CustomIOS7AlertView *alertView = [CustomIOS7AlertView alertWithTitle:@“Thank you for trying this demo” message:@“If you liked what you saw,\nand are interesting in seeing\nwhat we can do together,\nplease shoot us a mail by tapping the button below.”];
[alertView setButtonTitles:[NSMutableArray arrayWithObjects:@“Shoot us a mail!”, @“Try another demo!”, @“Close”, nil]];
[alertView setButtonColors:[NSMutableArray arrayWithObjects:[UIColor colorWithRed:255.0f/255.0f green:77.0f/255.0f blue:94.0f/255.0f alpha:1.0f],[UIColor colorWithRed:0.0f green:0.5f blue:1.0f alpha:1.0f],nil]];
[alertView setDelegate:self];
[alertView setOnButtonTouchUpInside:^(CustomIOS7AlertView *alertView, int buttonIndex) {
NSLog(@“Block: Button at position %d is clicked on alertView %d.”, buttonIndex, [alertView tag]);
[alertView close];
}];
[alertView show];
```

## More...

*   <a href="http://www.wimagguc.com/2013/10/custom-ios7-uialertview/" title="Custom iOS7 UIAlertView" rel="nofollow">Custom iOS7 UIAlertView</a> ![][4]
*   <a href="https://github.com/kwent/ios-custom-alertview" title="kwent/ios-custom-alertview · GitHub" rel="nofollow">kwent/ios-custom-alertview · GitHub</a> ![][4]
*   <a href="https://github.com/wimagguc" title="wimagguc (Richard Dancsi) · GitHub" rel="nofollow">wimagguc (Richard Dancsi) · GitHub</a> ![][4]

 [1]: https://github.com/wimagguc
 [2]: https://github.com/kwent/ios-custom-alertview
 [3]: http://blog.quentinrousseau.fr/wp-content/uploads/2013/11/screen.png
 [4]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png