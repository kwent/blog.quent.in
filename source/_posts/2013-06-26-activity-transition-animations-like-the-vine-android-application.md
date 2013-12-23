---
title: Activity transition animations like the Vine Android application.
author: Quentin
layout: post
permalink: /index.php/2013/06/activity-transition-animations-like-the-vine-android-application/
hl_twitter_has_auto_tweeted:
  - 'I just posted Activity transition animations like the Vine Android application., read it here: http://blog.quentinrousseau.fr/?p=622'
dsq_thread_id:
  - 1438159289
categories:
  - Développement
  - Mobile
tags:
  - android
  - animations
  - vine
---
Today, i will introduce you a cool activity transition animation which you could find in the last Vine app available on Android.

To clarify things, some screenshots of this animation.

### Screenshots

&nbsp;

<img class="size-medium wp-image-625 alignleft" alt="Screenshot_2013-06-26-14-06-54 copy" src="http://blog.quentinrousseau.fr/wp-content/uploads/2013/06/Screenshot_2013-06-26-14-06-54-copy-180x300.png" /><img class="size-medium wp-image-624 alignright" alt="Screenshot_2013-06-26-14-00-16 coy" src="http://blog.quentinrousseau.fr/wp-content/uploads/2013/06/Screenshot_2013-06-26-14-00-16-coy-180x300.png" /><img class="size-medium wp-image-623 aligncenter" alt="Screenshot_2013-06-26-14-00-16 copy" src="http://blog.quentinrousseau.fr/wp-content/uploads/2013/06/Screenshot_2013-06-26-14-00-16-copy-180x300.png" /> 
&nbsp;

### Animations XML

&nbsp;

<h4 style="text-align: left;">
  Opening transition animations.
</h4>

&nbsp;

#### Translate from right to left animation for the new activity (activity\_open\_translate.xml)

&nbsp;

<div class="codecolorer-container xml default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />
        </div>
      </td>
      
      <td>
        <div class="xml codecolorer">
          <span class="sc3"><span class="re1"><?xml</span> <span class="re0">version</span>=<span class="st0">"1.0"</span> <span class="re0">encoding</span>=<span class="st0">"utf-8"</span><span class="re2">?></span></span><br /> <br /> <span class="sc3"><span class="re1"><set</span> <span class="re0">xmlns:android</span>=<span class="st0">"http://schemas.android.com/apk/res/android"</span><span class="re2">></span></span><br /> <br />     <span class="sc3"><span class="re1"><translate</span> <span class="re0">android:fromXDelta</span>=<span class="st0">"100%"</span></span><br /> <span class="sc3">               <span class="re0">android:toXDelta</span>=<span class="st0">"0%"</span></span><br /> <span class="sc3">               <span class="re0">android:duration</span>=<span class="st0">"@android:integer/config_mediumAnimTime"</span> <span class="re2">/></span></span><br /> <br /> <span class="sc3"><span class="re1"></set<span class="re2">></span></span></span>
        </div>
      </td>
    </tr>
  </table>
</div>

*   A simple translate animation from right to left with a duration.****

#### Scale down animation for the old activity (activity\_close\_scale.xml)

&nbsp;

<div class="codecolorer-container xml default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />
        </div>
      </td>
      
      <td>
        <div class="xml codecolorer">
          <span class="sc3"><span class="re1"><?xml</span> <span class="re0">version</span>=<span class="st0">"1.0"</span> <span class="re0">encoding</span>=<span class="st0">"utf-8"</span><span class="re2">?></span></span><br /> <br /> <span class="sc3"><span class="re1"><set</span> <span class="re0">xmlns:android</span>=<span class="st0">"http://schemas.android.com/apk/res/android"</span><span class="re2">></span></span><br /> <br /> &nbsp; &nbsp; <span class="sc3"><span class="re1"><scale</span> <span class="re0">android:fromXScale</span>=<span class="st0">"100%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:toXScale</span>=<span class="st0">"80%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:fromYScale</span>=<span class="st0">"100%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:toYScale</span>=<span class="st0">"80%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:pivotX</span>=<span class="st0">"50%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:pivotY</span>=<span class="st0">"50%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:duration</span>=<span class="st0">"@android:integer/config_mediumAnimTime"</span> <span class="re2">/></span></span><br /> <br /> &nbsp; &nbsp; <span class="sc3"><span class="re1"><alpha</span> <span class="re0">android:fromAlpha</span>=<span class="st0">"1"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:toAlpha</span>=<span class="st0">"0.5"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:duration</span>=<span class="st0">"@android:integer/config_mediumAnimTime"</span><span class="re2">/></span></span><br /> <br /> <span class="sc3"><span class="re1"></set<span class="re2">></span></span></span>
        </div>
      </td>
    </tr>
  </table>
</div>

*   A scale down animation from 100% to 80% with a pivot point from the center of the activity, an alpha opacity to from 1.0 to 0.5 and a duration.

#### Closing transition animations

&nbsp;

#### Scale up animation for the new activity (activity\_open\_scale.xml)

&nbsp;

<div class="codecolorer-container xml default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />
        </div>
      </td>
      
      <td>
        <div class="xml codecolorer">
          <span class="sc3"><span class="re1"><?xml</span> <span class="re0">version</span>=<span class="st0">"1.0"</span> <span class="re0">encoding</span>=<span class="st0">"utf-8"</span><span class="re2">?></span></span><br /> <br /> <span class="sc3"><span class="re1"><set</span> <span class="re0">xmlns:android</span>=<span class="st0">"http://schemas.android.com/apk/res/android"</span><span class="re2">></span></span><br /> <br /> &nbsp; &nbsp; <span class="sc3"><span class="re1"><scale</span> <span class="re0">android:fromXScale</span>=<span class="st0">"80%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:toXScale</span>=<span class="st0">"100%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:fromYScale</span>=<span class="st0">"80%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:toYScale</span>=<span class="st0">"100%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:pivotX</span>=<span class="st0">"50%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:pivotY</span>=<span class="st0">"50%p"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:duration</span>=<span class="st0">"@android:integer/config_mediumAnimTime"</span> <span class="re2">/></span></span><br /> <br /> &nbsp; &nbsp; <span class="sc3"><span class="re1"><alpha</span> <span class="re0">android:fromAlpha</span>=<span class="st0">"0.5"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:toAlpha</span>=<span class="st0">"1.0"</span></span><br /> <span class="sc3"> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="re0">android:duration</span>=<span class="st0">"@android:integer/config_mediumAnimTime"</span><span class="re2">/></span></span><br /> <br /> <span class="sc3"><span class="re1"></set<span class="re2">></span></span></span>
        </div>
      </td>
    </tr>
  </table>
</div>

*   A scale down animation from 80% to 100% with a pivot point from the center of the activity, an alpha opacity to from 0.5 to 1.0 and a duration.

#### Translate from left to right animation for the old activity (activity\_close\_translate.xml)

&nbsp;

<div class="codecolorer-container xml default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />
        </div>
      </td>
      
      <td>
        <div class="xml codecolorer">
          <span class="sc3"><span class="re1"><?xml</span> <span class="re0">version</span>=<span class="st0">"1.0"</span> <span class="re0">encoding</span>=<span class="st0">"utf-8"</span><span class="re2">?></span></span><br /> <br /> <span class="sc3"><span class="re1"><set</span> <span class="re0">xmlns:android</span>=<span class="st0">"http://schemas.android.com/apk/res/android"</span><span class="re2">></span></span><br /> <br />     <span class="sc3"><span class="re1"><translate</span> <span class="re0">android:fromXDelta</span>=<span class="st0">"0%"</span></span><br /> <span class="sc3">               <span class="re0">android:toXDelta</span>=<span class="st0">"100%"</span></span><br /> <span class="sc3">               <span class="re0">android:duration</span>=<span class="st0">"@android:integer/config_mediumAnimTime"</span> <span class="re2">/></span></span><br /> <br /> <span class="sc3"><span class="re1"></set<span class="re2">></span></span></span>
        </div>
      </td>
    </tr>
  </table>
</div>

*   A simple translate animation from left to right with a duration.

### Activity integration

&nbsp;

In your new activity open :

<div class="codecolorer-container java default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />
        </div>
      </td>
      
      <td>
        <div class="java codecolorer">
          <span class="kw1">public</span> <span class="kw1">class</span> AnimatedActivity <span class="kw1">extends</span> Activity<br /> <span class="br0">&#123;</span><br /> &nbsp; @Override<br /> &nbsp; <span class="kw1">protected</span> <span class="kw4">void</span> onCreate<span class="br0">&#40;</span>Bundle savedInstanceState<span class="br0">&#41;</span><br /> &nbsp; <span class="br0">&#123;</span><br /> &nbsp; &nbsp; <span class="kw1">super</span>.<span class="me1">onCreate</span><span class="br0">&#40;</span>savedInstanceState<span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; <span class="co1">//opening transition animations</span><br /> &nbsp; &nbsp; overridePendingTransition<span class="br0">&#40;</span>R.<span class="me1">anim</span>.<span class="me1">activity_open_translate</span>,R.<span class="me1">anim</span>.<span class="me1">activity_close_scale</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; <span class="br0">&#125;</span><br /> <br /> &nbsp; @Override<br /> &nbsp; <span class="kw1">protected</span> <span class="kw4">void</span> onPause<span class="br0">&#40;</span><span class="br0">&#41;</span><br /> &nbsp; <span class="br0">&#123;</span><br /> &nbsp; &nbsp; <span class="kw1">super</span>.<span class="me1">onPause</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; <span class="co1">//closing transition animations</span><br /> &nbsp; &nbsp; overridePendingTransition<span class="br0">&#40;</span>R.<span class="me1">anim</span>.<span class="me1">activity_open_scale</span>,R.<span class="me1">anim</span>.<span class="me1">activity_close_translate</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; <span class="br0">&#125;</span><br /> <span class="br0">&#125;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

*    Cf. <http://developer.android.com/reference/android/app/Activity.html#overridePendingTransition%28int,%20int%29>

&nbsp;

### GIST Available

&nbsp;

<https://gist.github.com/kwent/5875749>

## <span style="color: #808080;">Compile, run and enjoy.</span>

&nbsp;