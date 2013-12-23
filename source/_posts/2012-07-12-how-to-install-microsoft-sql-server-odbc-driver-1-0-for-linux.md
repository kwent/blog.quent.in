---
title: How to install Microsoft® SQL Server® ODBC Driver 1.0 for Linux
author: Quentin
layout: post
permalink: /index.php/2012/07/how-to-install-microsoft-sql-server-odbc-driver-1-0-for-linux/
hl_twitter_has_auto_tweeted:
  - 'I just posted How to install Microsoft® SQL Server® ODBC Driver 1.0 for Linux, read it here: http://blog.quentinrousseau.fr/?p=541'
dsq_thread_id:
  - 762175272
categories:
  - Développement
  - Script
  - Système
tags:
  - linux
  - microsoft
  - odbc
  - redhat
  - sqlserver
---
Hello,

This manipulation was tested on **Linux RedHat EL 5/6 x86_64**

### 1 | Download sqlncli for Linux

&nbsp;

Download sqlncli on the official Microsoft website : <http://www.microsoft.com/en-us/download/details.aspx?id=28160>

&nbsp;

### 2 | Unzip and download unixODBC-2.3.0

&nbsp;

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="kw2">tar</span> xvzf sqlcli-11.0.1790.0.tar.gz <span class="sy0">&&</span> <span class="kw3">cd</span> sqlcli-11.0.1790.0<br /> <br /> .<span class="sy0">/</span>build_dm.sh <span class="co0">#Script to download unixODBC-2.3.0, configure and compile it.</span><br /> <br /> <span class="co0">#Get into the tempory folder where unixODBC-2.3.0 was compiled and execute <strong>make install</strong></span><br /> <br /> <span class="co0">#Before you install the driver, you may run a verify step to check if your computer has the required software to support the Microsoft SQL Server ODBC Driver 1.0 for Linux:</span><br /> <br /> .<span class="sy0">/</span>install.sh verify<br /> <br /> <span class="co0">#When you are ready to install the Microsoft SQL Server ODBC Driver 1.0 for Linux, run the install script:</span><br /> <br /> .<span class="sy0">/</span>install.sh <span class="kw2">install</span>
        </div>
      </td>
    </tr>
  </table>
</div>

### 2.bis  | Unzip and download unixODBC-2.3.1 [hack]

&nbsp;

**UnixODBC-2.3.1** is available at <ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.1.tar.gz> but actually not supported by **Microsoft sqlncli install scripts.**

To proceed installation of **sqlncli** with the **latest version of UnixODBC**, we have to modify these install scripts with :

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="kw3">cd</span> sqlcli-11.0.1790.0<br /> <br /> <span class="kw2">wget</span> ftp:<span class="sy0">//</span>ftp.unixodbc.org<span class="sy0">/</span>pub<span class="sy0">/</span>unixODBC<span class="sy0">/</span>unixODBC-2.3.1.tar.gz<br /> <br /> <span class="kw2">find</span> <span class="sy0">*</span>.sh <span class="re5">-exec</span> <span class="kw2">sed</span> <span class="re5">-i</span> <span class="st_h">'s/2.3.0/2.3.1/g'</span> <span class="br0">&#123;</span><span class="br0">&#125;</span> \;<br /> <br /> .<span class="sy0">/</span>build_dm.sh --download-url=file:<span class="sy0">//</span>unixODBC-2.3.1.tar.gz <span class="co0">#Script to unzip unixODBC-2.3.1 (local), configure and compile it.</span>
        </div>
      </td>
    </tr>
  </table>
</div>

### 3 | Repair libraries paths

&nbsp;

Now, normally you can find in /etc/odbcinst.ini

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="br0">&#91;</span>SQL Server Native Client <span class="nu0">11.0</span><span class="br0">&#93;</span><br /> <span class="re2">Description</span>=Microsoft SQL Server ODBC Driver V1.0 <span class="kw1">for</span> Linux<br /> <span class="re2">Driver</span>=<span class="sy0">/</span>opt<span class="sy0">/</span>microsoft<span class="sy0">/</span>sqlncli<span class="sy0">/</span>lib64<span class="sy0">/</span>libsqlncli-<span class="nu0">11.0</span>.so.1790.0<br /> <span class="re2">Threading</span>=<span class="nu0">1</span><br /> <span class="re2">UsageCount</span>=<span class="nu0">1</span>
        </div>
      </td>
    </tr>
  </table>
</div>

But if you tried isql or sqlcmd commands, you should have some surprises with this kind of problem :

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          isql <span class="re5">-v</span> DN user password <span class="co0">#DN located in you /etc/odbc.ini</span><br /> <br /> <span class="br0">&#91;</span>01000<span class="br0">&#93;</span><span class="br0">&#91;</span>unixODBC<span class="br0">&#93;</span><span class="br0">&#91;</span>Driver Manager<span class="br0">&#93;</span>Can<span class="st_h">'t open lib '</span><span class="sy0">/</span>opt<span class="sy0">/</span>microsoft<span class="sy0">/</span>sqlncli<span class="sy0">/</span>lib64<span class="sy0">/</span>libsqlncli-<span class="nu0">11.0</span>.so.1790.0<span class="st_h">' : file not found<br /> [ISQL]ERROR: Could not SQLConnect</span>
        </div>
      </td>
    </tr>
  </table>
</div>

To fix this issue, we have to find which libraries is missing for **libsqlncli-11.0.so.1790.0**

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;height:300px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />20<br />21<br />22<br />23<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="kw2">ldd</span> <span class="sy0">/</span>opt<span class="sy0">/</span>microsoft<span class="sy0">/</span>sqlncli<span class="sy0">/</span>lib64<span class="sy0">/</span>libsqlncli-<span class="nu0">11.0</span>.so.1790.0<br /> &nbsp; &nbsp; &nbsp; &nbsp; linux-vdso.so.1 =<span class="sy0">></span> &nbsp;<span class="br0">&#40;</span>0x00007fffce3ff000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libcrypto.so.10 =<span class="sy0">></span> <span class="sy0">/</span>usr<span class="sy0">/</span>lib64<span class="sy0">/</span>libcrypto.so.10 <span class="br0">&#40;</span>0x00007f90405a1000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libdl.so.2 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libdl.so.2 <span class="br0">&#40;</span>0x00007f904039d000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; librt.so.1 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>librt.so.1 <span class="br0">&#40;</span>0x00007f9040194000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libssl.so.10 =<span class="sy0">></span> <span class="sy0">/</span>usr<span class="sy0">/</span>lib64<span class="sy0">/</span>libssl.so.10 <span class="br0">&#40;</span>0x00007f903ff39000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libuuid.so.1 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libuuid.so.1 <span class="br0">&#40;</span>0x00007f903fd35000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libodbcinst.so.1 =<span class="sy0">></span> not found<br /> &nbsp; &nbsp; &nbsp; &nbsp; libkrb5.so.3 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libkrb5.so.3 <span class="br0">&#40;</span>0x00007f903fa55000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libgssapi_krb5.so.2 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libgssapi_krb5.so.2 <span class="br0">&#40;</span>0x00007f903f813000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libstdc++.so.6 =<span class="sy0">></span> <span class="sy0">/</span>usr<span class="sy0">/</span>lib64<span class="sy0">/</span>libstdc++.so.6 <span class="br0">&#40;</span>0x00007f903f50c000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libm.so.6 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libm.so.6 <span class="br0">&#40;</span>0x00007f903f288000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libgcc_s.so.1 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libgcc_s.so.1 <span class="br0">&#40;</span>0x00007f903f072000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libpthread.so.0 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libpthread.so.0 <span class="br0">&#40;</span>0x00007f903ee55000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libc.so.6 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libc.so.6 <span class="br0">&#40;</span>0x00007f903eac5000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libz.so.1 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libz.so.1 <span class="br0">&#40;</span>0x00007f903e8af000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="sy0">/</span>lib64<span class="sy0">/</span>ld-linux-x86-<span class="nu0">64</span>.so.2 <span class="br0">&#40;</span>0x0000003169600000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libcom_err.so.2 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libcom_err.so.2 <span class="br0">&#40;</span>0x00007f903e6aa000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libk5crypto.so.3 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libk5crypto.so.3 <span class="br0">&#40;</span>0x00007f903e47e000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libkrb5support.so.0 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libkrb5support.so.0 <span class="br0">&#40;</span>0x00007f903e273000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libkeyutils.so.1 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libkeyutils.so.1 <span class="br0">&#40;</span>0x00007f903e06f000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libresolv.so.2 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libresolv.so.2 <span class="br0">&#40;</span>0x00007f903de55000<span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; libselinux.so.1 =<span class="sy0">></span> <span class="sy0">/</span>lib64<span class="sy0">/</span>libselinux.so.1 <span class="br0">&#40;</span>0x00007f903dc35000<span class="br0">&#41;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

Now we found it, we have to fix it !

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
          <span class="kw2">ln</span> <span class="re5">-s</span> <span class="sy0">/</span>usr<span class="sy0">/</span>lib64<span class="sy0">/</span>libodbcinst.so.2 <span class="sy0">/</span>usr<span class="sy0">/</span>lib64<span class="sy0">/</span>libodbcinst.so.1
        </div>
      </td>
    </tr>
  </table>
</div>

Same problem with **sqlcmd**, you have to search missing libraries and fix correct paths with** symbolic links**

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
          <span class="kw2">ldd</span> <span class="sy0">`</span><span class="kw2">which</span> sqlcmd<span class="sy0">`</span>
        </div>
      </td>
    </tr>
  </table>
</div>

&nbsp;

### <span style="color: #008000;">Now everything should be OK</span>



## En savoir plus&#8230;

*   <a href="http://www.microsoft.com/en-us/download/details.aspx?id=28160" title="No Title" rel="nofollow">No Title</a> ![][1]
*   <a href="http://www.unixodbc.org/" title="unixODBC" rel="nofollow">unixODBC</a> ![][1]

 [1]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png