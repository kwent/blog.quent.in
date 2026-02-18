---
aliases:
- /posts/2015/02/12/simple-node-dot-js-wrapper-and-cli-for-synology-dsm-rest-api/
author: Quentin
categories:
- development
- script
- system
cover: /images/covers/simple-node-dot-js-wrapper-and-cli-for-synology-dsm-rest-api.png
date: 2015-02-12T16:54:19+0100
slug: simple-node-dot-js-wrapper-and-cli-for-synology-dsm-rest-api
tags:
- synology
- dsm
- filestation
- downloadstation
- nodejs
- node
- npmjs
- npm
title: Simple Node.js wrapper and CLI for Synology DSM REST API
---

## Purpose

[JimRobs][1] developped a cool Node.js wrapper for the [Synology DSM REST API][4]
but no **Command Line Tool** was available.

So i decided to develop my first Node.js CLI on top of this wrapper.

It's now [available][2] with **1.0.2 version** and **below some examples how to use it**.

## CLI

### Installation

```bash
$ npm install -g syno
```

### Usage
```
$ syno --help
Usage: syno [options]

  Synology Rest API Command Line

  Options:

    -h, --help           output usage information
    -V, --version        output the version number

  Commands:

    filestation|fs [options] <method>  DSM File Station API
    downloadstation|dl [options] <method>  DSM Download Station API

  Examples:

    $ syno filestation|fs getFileStationInfo
    $ syno downloadstation|dl getDownloadStationInfo
```

```
$ syno fs --help
Usage: filestation|fs [options] <method>

  DSM File Station API

  Options:

    -h, --help               output usage information
    -c, --config <path>      DSM configuration file. Default to ~/.syno/auth.yaml
    -u, --url <url>          DSM URL. Default to https://admin:password@localhost:5001
    -p, --payload <payload>  JSON Payload
    -P, --pretty             Prettyprint JSON Output
    -d, --debug              Enabling Debugging Output

  Examples:

    $ syno filestation|fs listSharedFolders
    $ syno filestation|fs listFiles --pretty --payload '{"folder_path":"/path/to/folder"}'
```

```
$ syno dl --help
Usage: downloadstation|dl [options] <method>

  DSM Download Station API

  Options:

    -h, --help               output usage information
    -c, --config <path>      DSM configuration file. Default to ~/.syno/auth.yaml
    -u, --url <url>          DSM URL. Default to https://admin:password@localhost:5001
    -p, --payload <payload>  JSON Payload
    -P, --pretty             Prettyprint JSON Output
    -d, --debug              Enabling Debugging Output

  Examples:

    $ syno downloadstation|dl createTask --payload '{"uri":"magnet|ed2k|ftp(s)|http(s)://link"}'
    $ syno downloadstation|dl listTasks
    $ syno downloadstation|dl listTasks --payload '{"limit":10}'
    $ syno downloadstation|dl getTasksInfo --pretty --payload '{"id":"task_id"}'
```

## Examples

### Without a configuration file

```bash
$ syno fs getFileStationInfo --url https://admin:synology@demo.synology.com:5001 --pretty
```

### With a configuration file

```yaml
# Example config file, by default it should be located at:
# ~/.syno/config.conf

url:
  protocol: https
  host: localhost
  port: 5001
  account: admin
  passwd: password
```

```bash
$ syno fs getFileStationInfo --pretty
```

## In real life ?

### List Files via File Station

```bash
$ syno fs listFiles --payload '{"folder_path":"/photo"}' --pretty
```

### List Tasks via Download Station

```bash
$ syno dl listTasks --payload '{"limit":1}' --pretty
```

### Add Task HTTP file via Download Station

```bash
$ syno dl createTask --payload '{"uri":"https://download.thinkbroadband.com/5MB.zip"}'
```

### Add Task Torrent magnet link via Download Station
```bash
$ syno dl createTask --payload '{"uri":"magnet:?xt=urn:ed2k:31D6CFE0D16AE931B73C59D7E0C089C0&xl=0&dn=zero_len.fil&xt=urn:bitprint:3I42H3S6NNFQ2MSVX7XZKYAYSCX5QBYJ.LWPNACQDBZRYXW3VHJVCJ64QBZNGHOHHHZWCLNQ&xt=urn:md5:D41D8CD98F00B204E9800998ECF8427E"}'
```

## More...

- [github][2]
- [npmjs][3]
- [Synology - Development Tool][4]

[1]: https://github.com/JimRobs
[2]: https://github.com/JimRobs/syno
[3]: https://www.npmjs.com/package/syno
[4]: https://www.synology.com/en-us/support/developer#tool