---
title: Windows Management Instrumentation (WMI) Linux Client
author: Quentin
layout: post
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
---
### Context

&nbsp;

I would like query WMI interface to get logical disks spaces from differents windows clients.

But WMI is** not natively** supported in Linux, so **Samba & Zenoss Team** worked hard to build a WMI client !

Following parts were tested on a** GNU/Linux Red Hat el6 x86_64**.

&nbsp;

### Installation

&nbsp;

You could find RPM called **&laquo;&nbsp;wmic&nbsp;&raquo;** for (**WMI** **C**lient) at <a href="http://rpmfind.net/linux/rpm2html/search.php?query=wmic&submit=Search" target="_blank">http://rpmfind.net/linux/rpm2html/search.php?query=wmic&submit=Search</a>

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="kw2">wget</span> ftp:<span class="sy0">//</span>rpmfind.net<span class="sy0">/</span>linux<span class="sy0">/</span>sourceforge<span class="sy0">/</span>p<span class="sy0">/</span>pa<span class="sy0">/</span>pandora<span class="sy0">/</span>Tools<span class="sy0">%</span>20and<span class="sy0">%</span>20dependencies<span class="sy0">%</span>20<span class="br0">&#40;</span>All<span class="sy0">%</span>20versions<span class="br0">&#41;</span><span class="sy0">/</span>RPM<span class="sy0">%</span>20SUSE<span class="sy0">/</span>wmic-4.0.0tp4-<span class="nu0"></span>.x86_64.rpm<br /> <br /> rpm <span class="re5">-ivh</span> wmic-4.0.0tp4-<span class="nu0"></span>.x86_64.rpm
        </div>
      </td>
    </tr>
  </table>
</div>

&nbsp;

### Usage

&nbsp;

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          wmic<br /> Usage: <span class="br0">&#91;</span>-?<span class="sy0">|</span>--help<span class="br0">&#93;</span> <span class="br0">&#91;</span>--usage<span class="br0">&#93;</span> <span class="br0">&#91;</span>-d<span class="sy0">|</span>--debuglevel DEBUGLEVEL<span class="br0">&#93;</span> <span class="br0">&#91;</span>--debug-stderr<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-s<span class="sy0">|</span>--configfile CONFIGFILE<span class="br0">&#93;</span> <span class="br0">&#91;</span>--option=<span class="re2">name</span>=value<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-l<span class="sy0">|</span>--log-basename LOGFILEBASE<span class="br0">&#93;</span> <span class="br0">&#91;</span>--leak-report<span class="br0">&#93;</span> <span class="br0">&#91;</span>--leak-report-full<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-R<span class="sy0">|</span>--name-resolve NAME-RESOLVE-ORDER<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-O<span class="sy0">|</span>--socket-options SOCKETOPTIONS<span class="br0">&#93;</span> <span class="br0">&#91;</span>-n<span class="sy0">|</span>--netbiosname NETBIOSNAME<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-W<span class="sy0">|</span>--workgroup WORKGROUP<span class="br0">&#93;</span> <span class="br0">&#91;</span>--realm=REALM<span class="br0">&#93;</span> <span class="br0">&#91;</span>-i<span class="sy0">|</span>--scope SCOPE<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-m<span class="sy0">|</span>--maxprotocol MAXPROTOCOL<span class="br0">&#93;</span> <span class="br0">&#91;</span>-U<span class="sy0">|</span>--user <span class="br0">&#91;</span>DOMAIN\<span class="br0">&#93;</span>USERNAME<span class="br0">&#91;</span><span class="sy0">%</span>PASSWORD<span class="br0">&#93;</span><span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-N<span class="sy0">|</span>--no-pass<span class="br0">&#93;</span> <span class="br0">&#91;</span>--password=STRING<span class="br0">&#93;</span> <span class="br0">&#91;</span>-A<span class="sy0">|</span>--authentication-file FILE<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>-S<span class="sy0">|</span>--signing on<span class="sy0">|</span>off<span class="sy0">|</span>required<span class="br0">&#93;</span> <span class="br0">&#91;</span>-P<span class="sy0">|</span>--machine-pass<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>--simple-bind-dn=STRING<span class="br0">&#93;</span> <span class="br0">&#91;</span>-k<span class="sy0">|</span>--kerberos STRING<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>--use-security-mechanisms=STRING<span class="br0">&#93;</span> <span class="br0">&#91;</span>-V<span class="sy0">|</span>--version<span class="br0">&#93;</span> <span class="br0">&#91;</span>--namespace=STRING<span class="br0">&#93;</span><br /> <span class="br0">&#91;</span>--delimiter=STRING<span class="br0">&#93;</span><br /> <span class="sy0">//</span>host query<br /> <br /> Example: wmic <span class="re5">-U</span> <span class="br0">&#91;</span>domain<span class="sy0">/</span><span class="br0">&#93;</span>adminuser<span class="sy0">%</span>password <span class="sy0">//</span>host <span class="st0">"select * from Win32_ComputerSystem"</span>
        </div>
      </td>
    </tr>
  </table>
</div>

In my case to get logical disks spaces, i used:

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          wmic <span class="re5">-U</span> <span class="br0">&#91;</span>domain<span class="sy0">/</span><span class="br0">&#93;</span>adminuser<span class="sy0">%</span>password <span class="sy0">//</span>host <span class="st0">"select VolumeName,FreeSpace from Win32_LogicalDisk"</span>
        </div>
      </td>
    </tr>
  </table>
</div>

&nbsp;

<h4 style="text-align: center;">
  <span style="color: #008000;">All is done !</span> Enjoy <img src="http://blog.quentinrousseau.fr/wp-includes/images/smilies/icon_smile.gif" alt=":)" class="wp-smiley" />
</h4>