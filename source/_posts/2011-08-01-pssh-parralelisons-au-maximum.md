---
title: Parallel-SSH | Parralélisez au maximum!
author: Quentin
layout: post
permalink: /index.php/2011/08/pssh-parralelisons-au-maximum/
dsq_thread_id:
  - 382021833
yourls_shorturl:
  - 
categories:
  - Système
tags:
  - cluster
  - linux
  - pssh
  - système
---
Je me suis récemment trouvé dans une situation dans laquelle je devais exécuter des commandes redondantes sur plusieurs serveurs (environnement clusterisé par exemple) et comme tout grand informaticien, je n&rsquo;aime pas passer sur 50 serveurs pour répéter une tâche. Je me suis donc lancé à la recherche d&rsquo;un utilitaire me permettant d&rsquo;arriver à mes fins.

J&rsquo;ai trouvé après quelques recherches **PSSH **(pour <cite><strong>p</strong>arallel-<strong>ssh</strong>)</cite> disponible à l&rsquo;adresse suivante: <a href="http://www.theether.org/pssh/" target="_blank">http://www.theether.org/pssh/</a>

Le principe est simple:

1. Je déclare mes hosts dans un fichier
```plain
user@192.168.1.1
user@192.168.1.2
user@192.168.1.3
```

2. Je lance **PSSH **en indiquant l&rsquo;emplacement du fichier ci-dessus

```bash
pssh -P -h ~/nodes.txt -A “$MACOMMANDE
```

Et le tour est joué! Voici la sortie avec **MACOMMANDE=&rsquo;cat /etc/snmp/snmpd.conf | md5sum&rsquo;** (Vérifions si le fichier snmpd.conf est strictement identique sur nos 3 serveurs).

```bash
192.168.1.1: d41d8cd98f00b204e9800998ecf8427e -
[1] 14:16:08 [SUCCESS] user@192.168.1.1
192.168.1.2: d41d8cd98f00b204e9800998ecf8427e -
[2] 14:16:08 [SUCCESS] user@192.168.1.2
192.168.1.3: d41d8cd98f00b204e9800998ecf8427e -
[3] 14:16:08 [SUCCESS] user@192.168.1.3
```

**3 MD5 identiques = 3 fichiers identiques**

Bien entendu, **<span style="color: #ff0000;">utilisez cet outil avec grande précaution</span>** et testez votre commande sur une machine test avant! En cas d&rsquo;erreur, ce sera l&rsquo;ensemble de vos serveurs configurés qui seront impactés&#8230;

<span style="text-decoration: underline;"><strong>Note</strong></span>**:** Il faut prélablement que les hosts soient connus par SSH dans **~/.ssh/known_hosts**

## More...&#8230;

*   <a href="http://www.linux.com/archive/feature/151340" title="Linux.com :: Parallel SSH execution and a single shell to ..." rel="nofollow">Linux.com :: Parallel SSH execution and a single shell to ...</a> ![][1]
*   <a href="http://www.theether.org/pssh/docs/0.2.3/pssh-HOWTO.html" title="pssh HOWTO" rel="nofollow">pssh HOWTO</a> ![][1]

 [1]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png