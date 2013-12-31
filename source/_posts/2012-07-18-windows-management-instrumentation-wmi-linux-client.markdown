---
title: Windows Management Instrumentation (WMI) Linux Client
author: Quentin
layout: post
comments: true
permalink: /index.php/2012/07/windows-management-instrumentation-wmi-linux-client/
hl_twitter_has_auto_tweeted:
  - 'I just posted Windows Management Instrumentation (WMI) Linux Client, read it here: http://blog.quentinrousseau.fr/?p=555'
dsq_thread_id:
  - 770344688
categories:
  - Développement
  - Script
  - Système
tags:
  - linux
  - wmi
date: Wed, 18 Jul 2012 11:45:26 -8000
---
### Context

I would like query WMI interface to get logical disks spaces from differents windows clients.

But WMI is** not natively** supported in Linux, so **Samba & Zenoss Team** worked hard to build a WMI client !

Following parts were tested on a** GNU/Linux Red Hat el6 x86_64**.

### Installation

You could find RPM called **&laquo;&nbsp;wmic&nbsp;&raquo;** for (**WMI** **C**lient) at <a href="http://rpmfind.net/linux/rpm2html/search.php?query=wmic&submit=Search" target="_blank">http://rpmfind.net/linux/rpm2html/search.php?query=wmic&submit=Search</a>

```bash
wget ftp://rpmfind.net/linux/sourceforge/p/pa/pandora/Tools%20and%20dependencies%20(All%20versions)/RPM%20SUSE/wmic-4.0.0tp4-.x86_64.rpm

rpm -ivh wmic-4.0.0tp4-.x86_64.rpm
```

### Usage

```bash
wmic
Usage: [-?|–help] [–usage] [-d|–debuglevel DEBUGLEVEL] [–debug-stderr]
[-s|–configfile CONFIGFILE] [–option=name=value]
[-l|–log-basename LOGFILEBASE] [–leak-report] [–leak-report-full]
[-R|–name-resolve NAME-RESOLVE-ORDER]
[-O|–socket-options SOCKETOPTIONS] [-n|–netbiosname NETBIOSNAME]
[-W|–workgroup WORKGROUP] [–realm=REALM] [-i|–scope SCOPE]
[-m|–maxprotocol MAXPROTOCOL] [-U|–user [DOMAIN\]USERNAME[%PASSWORD]]
[-N|–no-pass] [–password=STRING] [-A|–authentication-file FILE]
[-S|–signing on|off|required] [-P|–machine-pass]
[–simple-bind-dn=STRING] [-k|–kerberos STRING]
[–use-security-mechanisms=STRING] [-V|–version] [–namespace=STRING]
[–delimiter=STRING]
//host query

Example: wmic -U [domain/]adminuser%password //host “select * from Win32_ComputerSystem”
```

In my case to get logical disks spaces, i used:

```bash
wmic -U [domain/]adminuser%password //host “select VolumeName,FreeSpace from Win32_LogicalDisk”
```

Congrats you are done !