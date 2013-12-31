---
title: Activity transition animations like the Vine Android application.
author: Quentin
layout: post
comments: true
permalink: /index.php/2013/06/activity-transition-animations-like-the-vine-android-application/
hl_twitter_has_auto_tweeted:
  - 'I just posted Activity transition animations like the Vine Android application., read it here: http://blog.quentinrousseau.fr/?p=622'
dsq_thread_id:
  - 1438159289
categories:
  - development
  - mobile
tags:
  - android
  - animations
  - vine
date: Wed, 26 Jun 2013 13:05:09 -8000
---
Today, i will introduce you a cool activity transition animation which you could find in the last Vine app available on Android.

To clarify things, some screenshots of this animation.

### Screenshots

![Screenshot1](/assets/wp-content/uploads/2013/06/Screenshot_2013-06-26-14-06-54-copy-180x300.png)
![Screenshot2](/assets/wp-content/uploads/2013/06/Screenshot_2013-06-26-14-00-16-coy-180x300.png)
![Screenshot3](/assets/wp-content/uploads/2013/06/Screenshot_2013-06-26-14-00-16-copy-180x300.png)

### Animations XML

<h4 style="text-align: left;">
  Opening transition animations.
</h4>

#### Translate from right to left animation for the new activity (activity\_open\_translate.xml)

```xml
<?xml version="1.0" encoding="utf-8"?>
 
<set xmlns:android="http://schemas.android.com/apk/res/android">
 
    <translate android:fromXDelta="100%"
               android:toXDelta="0%"
               android:duration="@android:integer/config_mediumAnimTime" />
 
</set>
```

*   A simple translate animation from right to left with a duration.****

#### Scale down animation for the old activity (activity\_close\_scale.xml)

```xml
<?xml version="1.0" encoding="utf-8"?>
 
<set xmlns:android="http://schemas.android.com/apk/res/android">
 
    <scale android:fromXScale="100%p"
          android:toXScale="80%p"
          android:fromYScale="100%p"
          android:toYScale="80%p"
          android:pivotX="50%p"
          android:pivotY="50%p"
          android:duration="@android:integer/config_mediumAnimTime" />
 
    <alpha android:fromAlpha="1"
          android:toAlpha="0.5"
          android:duration="@android:integer/config_mediumAnimTime"/>
 
</set>
```

*   A scale down animation from 100% to 80% with a pivot point from the center of the activity, an alpha opacity to from 1.0 to 0.5 and a duration.

#### Closing transition animations

#### Scale up animation for the new activity (activity\_open\_scale.xml)

```xml
<?xml version="1.0" encoding="utf-8"?>
 
<set xmlns:android="http://schemas.android.com/apk/res/android">
 
    <scale android:fromXScale="80%p"
          android:toXScale="100%p"
          android:fromYScale="80%p"
          android:toYScale="100%p"
          android:pivotX="50%p"
          android:pivotY="50%p"
          android:duration="@android:integer/config_mediumAnimTime" />
 
    <alpha android:fromAlpha="0.5"
          android:toAlpha="1.0"
          android:duration="@android:integer/config_mediumAnimTime"/>
 
</set>
```

*   A scale down animation from 80% to 100% with a pivot point from the center of the activity, an alpha opacity to from 0.5 to 1.0 and a duration.

#### Translate from left to right animation for the old activity (activity\_close\_translate.xml)

```xml
<?xml version="1.0" encoding="utf-8"?>
 
<set xmlns:android="http://schemas.android.com/apk/res/android">
 
    <translate android:fromXDelta="0%"
               android:toXDelta="100%"
               android:duration="@android:integer/config_mediumAnimTime" />
 
</set>
```

*   A simple translate animation from left to right with a duration.

### Activity integration

In your new activity open :

```java
public class AnimatedActivity extends Activity
{
  @Override
  protected void onCreate(Bundle savedInstanceState)
  {
    super.onCreate(savedInstanceState);
    //opening transition animations
    overridePendingTransition(R.anim.activity_open_translate,R.anim.activity_close_scale);
  }
 
  @Override
  protected void onPause()
  {
    super.onPause();
    //closing transition animations
    overridePendingTransition(R.anim.activity_open_scale,R.anim.activity_close_translate);
  }
}
```

*    Cf. <http://developer.android.com/reference/android/app/Activity.html#overridePendingTransition%28int,%20int%29>

### GIST Available

<https://gist.github.com/kwent/5875749>

## <span style="color: #808080;">Compile, run and enjoy.</span>