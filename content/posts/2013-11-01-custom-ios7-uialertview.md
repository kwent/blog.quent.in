---
aliases:
- /index.php/2013/11/custom-ios7-uialertview/
- /posts/2013/11/01/custom-ios7-uialertview/
author: Quentin
categories:
- development
- ios
- mobile
cover: /images/covers/custom-ios7-uialertview.png
date: '2013-11-01T17:11:50'
disqus_identifier: '1927300841'
slug: custom-ios7-uialertview
tags:
- alertview
- custom
- dialog
- flat
- ios
- ios7
title: Custom iOS7 UIAlertView
---

I forked « ios-custom-alertview » from [@wimagguc][1] and added a different design button this week.

You can just [grab the open source code from Github now][2].

![Ios Custom AlertView](/images/posts/screen.png)

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

*   [Custom iOS7 UIAlertView](https://www.wimagguc.com/2013/10/custom-ios7-uialertview/)
*   [kwent/ios-custom-alertview](https://github.com/kwent/ios-custom-alertview)
*   [wimagguc (Richard Dancsi)](https://github.com/wimagguc)

 [1]: https://github.com/wimagguc
 [2]: https://github.com/kwent/ios-custom-alertview