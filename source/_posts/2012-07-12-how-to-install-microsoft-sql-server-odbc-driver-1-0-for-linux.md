---
title: How to install Microsoft® SQL Server® ODBC Driver 1.0 for Linux
author: Quentin
layout: post
comments: true
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
date: Thu, 12 Jul 2012 15:10:37 -8000
---
Hello,

This manipulation was tested on **Linux RedHat EL 5/6 x86_64**

### 1 | Download sqlncli for Linux

Download sqlncli on the official Microsoft website : <http://www.microsoft.com/en-us/download/details.aspx?id=28160>

### 2 | Unzip and download unixODBC-2.3.0

```bash
tar xvzf sqlcli-11.0.1790.0.tar.gz && cd sqlcli-11.0.1790.0

./build_dm.sh #Script to download unixODBC-2.3.0, configure and compile it.

#Get into the tempory folder where unixODBC-2.3.0 was compiled and execute make install

#Before you install the driver, you may run a verify step to check if your computer has the required software to support the Microsoft SQL Server ODBC Driver 1.0 for Linux:

./install.sh verify

#When you are ready to install the Microsoft SQL Server ODBC Driver 1.0 for Linux, run the install script:

./install.sh install
```

### 2.bis  | Unzip and download unixODBC-2.3.1 [hack]

**UnixODBC-2.3.1** is available at <ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.1.tar.gz> but actually not supported by **Microsoft sqlncli install scripts.**

To proceed installation of **sqlncli** with the **latest version of UnixODBC**, we have to modify these install scripts with :

```bash
cd sqlcli-11.0.1790.0

wget ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.1.tar.gz

find *.sh -exec sed -i ’s/2.3.0/2.3.1/g’ {} \;

./build_dm.sh –download-url=file://unixODBC-2.3.1.tar.gz #Script to unzip unixODBC-2.3.1 (local), configure and compile it.
```

### 3 | Repair libraries paths

Now, normally you can find in /etc/odbcinst.ini

```plain
[SQL Server Native Client 11.0]
Description=Microsoft SQL Server ODBC Driver V1.0 for Linux
Driver=/opt/microsoft/sqlncli/lib64/libsqlncli-11.0.so.1790.0
Threading=1
UsageCount=1
```

But if you tried isql or sqlcmd commands, you should have some surprises with this kind of problem :

```bash
isql -v DN user password #DN located in you /etc/odbc.ini

[01000][unixODBC][Driver Manager]Can‘t open lib ’/opt/microsoft/sqlncli/lib64/libsqlncli-11.0.so.1790.0’ : file not found
[ISQL]ERROR: Could not SQLConnect
```

To fix this issue, we have to find which libraries is missing for **libsqlncli-11.0.so.1790.0**

```bash
ldd /opt/microsoft/sqlncli/lib64/libsqlncli-11.0.so.1790.0
        linux-vdso.so.1 =>  (0x00007fffce3ff000)
        libcrypto.so.10 => /usr/lib64/libcrypto.so.10 (0x00007f90405a1000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f904039d000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f9040194000)
        libssl.so.10 => /usr/lib64/libssl.so.10 (0x00007f903ff39000)
        libuuid.so.1 => /lib64/libuuid.so.1 (0x00007f903fd35000)
        libodbcinst.so.1 => not found
        libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007f903fa55000)
        libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007f903f813000)
        libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00007f903f50c000)
```

Now we found it, we have to fix it !

```bash
ln -s /usr/lib64/libodbcinst.so.2 /usr/lib64/libodbcinst.so.1
```

Same problem with **sqlcmd**, you have to search missing libraries and fix correct paths with** symbolic links**

```bash
ldd `which sqlcmd`
```
### <span style="color: #008000;">Now everything should be OK</span>

## More...

*   <a href="http://www.microsoft.com/en-us/download/details.aspx?id=28160" title="No Title" rel="nofollow">No Title</a> ![][1]
*   <a href="http://www.unixodbc.org/" title="unixODBC" rel="nofollow">unixODBC</a> ![][1]

 [1]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png