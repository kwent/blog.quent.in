---
author: Quentin
categories:
- development
- ios
- mobile
cover: /images/covers/level-up-ionicons-ios-with-a-category.png
date: 2014-10-25T00:02:54-0700
slug: level-up-ionicons-ios-with-a-category
tags:
- ionicons
- icons
- category
- helper
- imageview
- button
title: Level up ionicons-iOS with a category
---

## Purpose

[Ionicons][1] is a cool icon font framework (100% free and open source) designed by
[Ionic Framework][2].

[David Sweetman][3] released an iOS library to permit iOS developers to integrate this
font with your projects via this
repository [https://github.com/sweetmandm/ionicons-iOS][4]

But you can only generate [UIImage][5] object or [UILabel][6] with this library.
I needed more like generate [UIImageView][7], [UIButton][8], add a corner radius around them [...].

So i created a category who is now adding useful functions.

## Category overview

```objective-c
+ (UIButton*) buttonWithIcon:(NSString*)icon_name
                          iconColor:(UIColor*)iconColor
                           iconSize:(CGFloat)iconSize
                          imageSize:(CGSize)imageSize;

+ (UIButton*) roundedButtonWithIcon:(NSString*)icon_name
                iconColor:(UIColor*)iconColor
                 iconSize:(CGFloat)iconSize
                imageSize:(CGSize)imageSize;

+ (UIImageView*) imageViewWithIcon:(NSString*)icon_name
                         iconColor:(UIColor*)iconColor
                          iconSize:(CGFloat)iconSize
                         imageSize:(CGSize)imageSize;

+ (UIImageView*) roundedImageViewWithIcon:(NSString*)icon_name
                                iconColor:(UIColor*)iconColor
                                fillColor:(UIColor*)fillColor
                                 iconSize:(CGFloat)iconSize
                                imageSize:(CGSize)imageSize;

+ (UIImageView*) roundedImageViewWithIcon:(NSString*)icon_name
                               iconColor:(UIColor*)iconColor
                                iconSize:(CGFloat)iconSize
                               imageSize:(CGSize)imageSize;
```

## Gist

Available [here][9]. Please feel free to improve it !

## More...

- [Ionicons][1]
- [Ionic Framework][2]
- [ionicons-iOS][4]

[1]: http://ionicons.com
[2]: http://ionicframework.com
[3]: https://github.com/sweetmandm
[4]: https://github.com/sweetmandm/ionicons-iOS
[5]: https://developer.apple.com/library/ios/documentation/uikit/Reference/UIImage_Class/index.html
[6]: https://developer.apple.com/library/ios/documentation/uikit/Reference/UILabel_Class/index.html
[7]: https://developer.apple.com/library/ios/documentation/uikit/reference/uiimageview_class/index.html
[8]: https://developer.apple.com/library/ios/documentation/uikit/Reference/UIButton_Class/index.html
[9]: https://gist.github.com/kwent/d9ba3f62e62dc4a36df8