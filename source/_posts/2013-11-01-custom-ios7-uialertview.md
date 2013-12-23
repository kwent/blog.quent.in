---
title: Custom iOS7 UIAlertView
author: Quentin
layout: post
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
---
I forked &laquo;&nbsp;ios-custom-alertview&nbsp;&raquo; from [@wimagguc][1] and added a different design button this week.

You can just [grab the open source code from Github now][2].

[<img class="aligncenter size-full wp-image-658" alt="Ios Custom AlertView" src="http://blog.quentinrousseau.fr/wp-content/uploads/2013/11/screen.png" />][3] 
&nbsp;

Implementation of this alert view is :

<div class="codecolorer-container objc default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />
        </div>
      </td>
      
      <td>
        <div class="objc codecolorer">
          CustomIOS7AlertView <span class="sy0">*</span>alertView <span class="sy0">=</span> <span class="br0">&#91;</span>CustomIOS7AlertView alertWithTitle<span class="sy0">:</span><span class="co3">@</span><span class="st0">"Thank you for trying this demo"</span> message<span class="sy0">:</span><span class="co3">@</span><span class="st0">"If you liked what you saw,<span class="es0">\n</span>and are interesting in seeing<span class="es0">\n</span>what we can do together,<span class="es0">\n</span>please shoot us a mail by tapping the button below."</span><span class="br0">&#93;</span>;<br /> <span class="br0">&#91;</span>alertView setButtonTitles<span class="sy0">:</span><span class="br0">&#91;</span><a href="http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSMutableArray_Class/"><span class="kw5">NSMutableArray</span></a> arrayWithObjects<span class="sy0">:</span><span class="co3">@</span><span class="st0">"Shoot us a mail!"</span>, <span class="co3">@</span><span class="st0">"Try another demo!"</span>, <span class="co3">@</span><span class="st0">"Close"</span>, <span class="kw2">nil</span><span class="br0">&#93;</span><span class="br0">&#93;</span>;<br /> <span class="br0">&#91;</span>alertView setButtonColors<span class="sy0">:</span><span class="br0">&#91;</span><a href="http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSMutableArray_Class/"><span class="kw5">NSMutableArray</span></a> arrayWithObjects<span class="sy0">:</span><span class="br0">&#91;</span>UIColor colorWithRed<span class="sy0">:</span>255.0f<span class="sy0">/</span>255.0f green<span class="sy0">:</span>77.0f<span class="sy0">/</span>255.0f blue<span class="sy0">:</span>94.0f<span class="sy0">/</span>255.0f alpha<span class="sy0">:</span>1.0f<span class="br0">&#93;</span>,<span class="br0">&#91;</span>UIColor colorWithRed<span class="sy0">:</span>0.0f green<span class="sy0">:</span>0.5f blue<span class="sy0">:</span>1.0f alpha<span class="sy0">:</span>1.0f<span class="br0">&#93;</span>,<span class="kw2">nil</span><span class="br0">&#93;</span><span class="br0">&#93;</span>;<br /> <span class="br0">&#91;</span>alertView setDelegate<span class="sy0">:</span>self<span class="br0">&#93;</span>;<br /> <span class="br0">&#91;</span>alertView setOnButtonTouchUpInside<span class="sy0">:^</span><span class="br0">&#40;</span>CustomIOS7AlertView <span class="sy0">*</span>alertView, <span class="kw4">int</span> buttonIndex<span class="br0">&#41;</span> <span class="br0">&#123;</span><br /> NSLog<span class="br0">&#40;</span><span class="co3">@</span><span class="st0">"Block: Button at position %d is clicked on alertView %d."</span>, buttonIndex, <span class="br0">&#91;</span>alertView tag<span class="br0">&#93;</span><span class="br0">&#41;</span>;<br /> <span class="br0">&#91;</span>alertView close<span class="br0">&#93;</span>;<br /> <span class="br0">&#125;</span><span class="br0">&#93;</span>;<br /> <span class="br0">&#91;</span>alertView show<span class="br0">&#93;</span>;
        </div>
      </td>
    </tr>
  </table>
</div>



## En savoir plus&#8230;

*   <a href="http://www.wimagguc.com/2013/10/custom-ios7-uialertview/" title="Custom iOS7 UIAlertView" rel="nofollow">Custom iOS7 UIAlertView</a> ![][4]
*   <a href="https://github.com/kwent/ios-custom-alertview" title="kwent/ios-custom-alertview · GitHub" rel="nofollow">kwent/ios-custom-alertview · GitHub</a> ![][4]
*   <a href="https://github.com/wimagguc" title="wimagguc (Richard Dancsi) · GitHub" rel="nofollow">wimagguc (Richard Dancsi) · GitHub</a> ![][4]

 [1]: https://github.com/wimagguc
 [2]: https://github.com/kwent/ios-custom-alertview
 [3]: http://blog.quentinrousseau.fr/wp-content/uploads/2013/11/screen.png
 [4]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png