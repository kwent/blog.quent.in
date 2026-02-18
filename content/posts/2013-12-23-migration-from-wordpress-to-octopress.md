---
author: Quentin
categories:
- development
- octopress
- migration
- system
cover: /images/covers/migration-from-wordpress-to-octopress.png
date: 2013-12-23T21:26:23-0800
slug: migration-from-wordpress-to-octopress
title: Migration from WordPress to Octopress
---

## Yes i did it !

It was a long time that i was looking for another solution for hosting this blog.

This blog is now running with [**Octopress**][1] (Based on [**Jekyll**][2] Engine), and still powered by **Nginx**.

The current Theme is called [**OctoPanel**][3].

## Why ?

- **Wordpress** was good for many years to me but **too heavy/too much features** i did'nt need.

- It was a lot of pain to integrate **snippet of code** in Wordpress. (Even with plugin helpers).

- I did'nt need an instance of database running for only few articles.

- I did'nt need a **GUI** with a **WISIWYG** editor, i'm coding every days and it's faster for me to write in **Mardown syntax**.

## Cool things to know about the migration

- I migrated my old articles via a wordpress plugin called [**wordpress-to-jekyll-exporter**][4].
(This plugin is generated all articles in **Markdown syntax**. (This is not perfect but it helps)).

- Links to my articles are still the same. (**Permalinks saved**). So **no deferencement** with Google.

- I transfered all the locals images imported in Wordpress since 2 years in a new local assets folder and remodify images links in articles.

- **All the comments are saved** 'cause i used to save my comments with [**Disqus**][5]. Just to put the **disqus_thread_id** in each post and you are done !

- **Google analytics** is up. Just put my google analytics account id in the Octopress config file.

- **Share buttons** are up. Just activated them in the [Octopress][1] config file.

- **Tags & categories** are saved too. But i did'nt find so far how to display them in the list layout.

- I tried to integrate **Font Awesome** but i failed. I will figure out later.

## More...

- [OctoPress Website][1]
- [Jekyll Website][2]
- [OctoPanel Theme][3]
- [Wordpress to Jekyll Exporter][4]
- [Disqus Website][5]

[1]: https://octopress.org
[2]: https://jekyllrb.com
[3]: https://github.com/ConnorAtherton/OctoPanel
[4]: https://github.com/benbalter/wordpress-to-jekyll-exporter
[5]: https://disqus.com