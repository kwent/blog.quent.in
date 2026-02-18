---
title: Windows Management Instrumentation (WMI) Linux Client
date: '2012-07-18T11:45:26'
author: Quentin
categories:
- development
- script
- system
tags:
- linux
- wmi
aliases:
- /index.php/2012/07/windows-management-instrumentation-wmi-linux-client/
disqus_identifier: '770344688'
slug: windows-management-instrumentation-wmi-linux-client
---
### Context

I would like query WMI interface to get logical disks spaces from differents windows clients.

But WMI is** not natively** supported in Linux, so **Samba & Zenoss Team** worked hard to build a WMI client !

Following parts were tested on a** GNU/Linux Red Hat el6 x86_64**.

### Installation

You could find RPM called **« wmic »** for (**WMI** **C**lient) at <a href="http://rpmfind.net/linux/rpm2html/search.php?query=wmic&submit=Search" target="_blank">http://rpmfind.net/linux/rpm2html/search.php?query=wmic&submit=Search</a>

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