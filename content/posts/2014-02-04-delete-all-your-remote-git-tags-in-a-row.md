---
categories:
- development
- script
- system
cover: /images/covers/delete-all-your-remote-git-tags-in-a-row.png
date: 2014-02-04T19:41:53-0800
slug: delete-all-your-remote-git-tags-in-a-row
tags:
- git
- github
title: Delete all your remote git tags in a row
---

Today i will introduce a simple command line to **delete all your remote git tags**.

- Note1: Only OSX System tested.
- Note2: You will probably need to download and install the [Apple Developer Tools][3].

##Command line

`git ls-remote --tags | awk '{print $2}' | xargs -n1 git push --delete origin`

##Details

###List remote tags

`git ls-remote --tags`

```
From git@github.com:kwent/TTTRegexAttributedLabel.git
fb3dbbe61dc0af7428cde1a60ec2c4b6579650ab	refs/tags/1.7.1
b38bad9153621f25a310216daa59d5535effea53	refs/tags/1.7.2
2bba8a3b2eef03449d5ea0c7100c4be520b6a353	refs/tags/1.7.5
2d94ab087de50066afa838027e448eb0e16d5f50	refs/tags/1.8.0
```

###Grep good column

`git ls-remote --tags | awk '{print $2}'`

```
From git@github.com:kwent/TTTRegexAttributedLabel.git
refs/tags/1.7.1
refs/tags/1.7.2
refs/tags/1.7.5
refs/tags/1.8.0
```

###Deletion

`git ls-remote --tags | awk '{print $2}' | xargs -n1 git push --delete origin`


## More...

- [git ls-remote][1]
- [awk][2]
- [Apple Developer][3]

[1]: https://developer.apple.com/library/mac/documentation/darwin/reference/manpages/man1/git-ls-remote.1.html
[2]: https://developer.apple.com/library/mac/documentation/darwin/reference/manpages/man1/awk.1.html
[3]: https://developer.apple.com/technologies/tools/