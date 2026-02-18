---
title: Backup Neo4j Database to AWS S3
date: 2014-07-11T14:05:00-0700
author: Quentin
categories:
- development
- script
- system
tags:
- neo4j
- database
- backup
- aws
- amazon
- s3
slug: backup-neo4j-database-to-aws-s3
---

### Update (2014-07-28)

I got some issues using `tar` with big folder size. I fixed it by using
using [7zip](http://www.7-zip.org/download.html) using [LZMA2](http://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm) compression algorithm instead [LZO][3].

New **Gist** available [here](https://gist.github.com/kwent/82f544dd0488619fd596). Please feel free to improve it !

## Purpose

I needed to daily backup a [Neo4j Database][6] on [AWS S3][5] via a cron task so i
developed a shell script doing the job.

## Script

### Steps

1. `neo4j-backup` is doing a backup of the database to a local target folder
given. Be sure to have the available space in local.
**Binary** :  [neo4j-backup][1]

2. `tar` is archiving all files into one. No gzip or bzip compression here
since it was too slow for my file (> 100 Go).
**Binary** : [tar][7]

3. `lzop` is a very fast compression algorithm who compressing the file in few
minutes and is saving file size to upload on [AWS S3][5]. 
**Binary** : [lzop][3]

4. `aws s3 cp` is uploading our file to S3 using [Amazon S3 Multipart Upload][4] if
the file size is big. It's uploading a file faster.
**Binary** : [aws][2]

## Cron task

Add a file into `/etc/cron.d/neo4j-backup` with:

```bash
# Run a daily backup at 4:00 AM.
0 4 * * * root /bin/sh /opt/neo4j-enterprise-1.9.8/backup_neo4j_to_s3.sh 127.0.0.1 6362 /mnt/datadisk/backup
```

## Gist

Available [here](https://gist.github.com/kwent/82f544dd0488619fd596/d4a87ed4f2b18db56acc025d0506f8cf826a3dea). Please feel free to improve it !
**Update gist (2014-07-28) available ** [here](https://gist.github.com/kwent/82f544dd0488619fd596). Please feel free to improve it !

## More...

- [Neo4j - The World's Leading Graph Database][6]
- [Neo4j-backup][1]
- [Introducing Amazon S3 Multipart Upload][4]
- [AWS S3][5]
- [AWS Command Line Interface][2]
- [Lzop file compressor][3]

[1]: http://docs.neo4j.org/chunked/stable/re04.html
[2]: http://aws.amazon.com/cli
[3]: http://www.lzop.org
[4]: https://aws.amazon.com/about-aws/whats-new/2010/11/10/Amazon-S3-Introducing-Multipart-Upload
[5]: http://aws.amazon.com/s3
[6]: http://www.neo4j.org
[7]: http://unixhelp.ed.ac.uk/CGI/man-cgi?tar