---
author: Quentin
categories:
- development
- web
cover: /images/covers/real-time-logging-for-ironworker-with-logentries.png
date: 2014-05-27T23:15:42-0700
slug: real-time-logging-for-ironworker-with-logentries
tags:
- logentries
- iron
- workers
title: Real-time Logging for IronWorker with Logentries
---

## Purpose

When you a executing a job with [Iron Worker Service][1] and writing logs on `STDOUT` you have
to wait that the job is terminated to read the log file. Not very convenient if
want to see your logs in real time right ?

Iron blog wrote a post about [how setup real time logging with papertrail][4].

This post is how setup real time logging with [logentries][2].

## Logentries

### Add a new logtype and select manual configuration

![Logentries Manual Configuration](/assets/posts/2014-05-27-real-time-logging-for-ironworker-with-logentries/logentries-manual-configuration.png)

### Select Plain UDP/TCP log type

![Logentries Manual Configuration UDP](/assets/posts/2014-05-27-real-time-logging-for-ironworker-with-logentries/logentries-udp.png)

### Copy/Paste the UDP or TCP port logentries just created for you

![Logentries Manual Configuration Port](/assets/posts/2014-05-27-real-time-logging-for-ironworker-with-logentries/logentries-port.png)

## IronWorker

### Go to your project settings and add `api.logentries.com` endpoint with the port specified above.

![IronWorker logs UDP configuration](/assets/posts/2014-05-27-real-time-logging-for-ironworker-with-logentries/iron-udp.png)

## You are all set !

It's time now to relaunch a job and see your logs in real time.

## More...

- [iron.io][1]
- [logentries.com][2]
- [logentries.com doc | Plain TCP/UDP][3]
- [real-time-logging-for-ironworker with papertrail][4]

[1]: http://www.iron.io
[2]: https://logentries.com
[3]: https://logentries.com/doc/input-plaintcpudp
[4]: http://blog.iron.io/2013/07/real-time-logging-for-ironworker.html