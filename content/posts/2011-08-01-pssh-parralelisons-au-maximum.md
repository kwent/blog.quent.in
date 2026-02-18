---
aliases:
- /index.php/2011/08/pssh-parralelisons-au-maximum/
- /posts/2011/08/01/pssh-parralelisons-au-maximum/
author: Quentin
categories:
- system
cover: /images/covers/pssh-parralelisons-au-maximum.png
date: '2011-08-01T14:45:04'
disqus_identifier: '382021833'
slug: pssh-parralelisons-au-maximum
tags:
- cluster
- linux
- pssh
- system
title: Parallel-SSH | Parralélisez au maximum!
---

Je me suis récemment trouvé dans une situation dans laquelle je devais exécuter des commandes redondantes sur plusieurs serveurs (environnement clusterisé par exemple) et comme tout grand informaticien, je n'aime pas passer sur 50 serveurs pour répéter une tâche. Je me suis donc lancé à la recherche d'un utilitaire me permettant d'arriver à mes fins.

J'ai trouvé après quelques recherches **PSSH **(pour ***p**arallel-**ssh***) disponible à l'adresse suivante: [https://www.theether.org/pssh/](https://www.theether.org/pssh/)

Le principe est simple:

1. Je déclare mes hosts dans un fichier
```plain
user@192.168.1.1
user@192.168.1.2
user@192.168.1.3
```

2. Je lance **PSSH **en indiquant l'emplacement du fichier ci-dessus

```bash
pssh -P -h ~/nodes.txt -A “$MACOMMANDE
```

Et le tour est joué! Voici la sortie avec **MACOMMANDE='cat /etc/snmp/snmpd.conf | md5sum'** (Vérifions si le fichier snmpd.conf est strictement identique sur nos 3 serveurs).

```bash
192.168.1.1: d41d8cd98f00b204e9800998ecf8427e -
[1] 14:16:08 [SUCCESS] user@192.168.1.1
192.168.1.2: d41d8cd98f00b204e9800998ecf8427e -
[2] 14:16:08 [SUCCESS] user@192.168.1.2
192.168.1.3: d41d8cd98f00b204e9800998ecf8427e -
[3] 14:16:08 [SUCCESS] user@192.168.1.3
```

**3 MD5 identiques = 3 fichiers identiques**

Bien entendu, **utilisez cet outil avec grande précaution** et testez votre commande sur une machine test avant! En cas d'erreur, ce sera l'ensemble de vos serveurs configurés qui seront impactés...

**Note:** Il faut prélablement que les hosts soient connus par SSH dans **~/.ssh/known_hosts**

## More...

*   [Linux.com :: Parallel SSH execution and a single shell to ...](https://www.linux.com/archive/feature/151340)
*   [pssh HOWTO](https://www.theether.org/pssh/docs/0.2.3/pssh-HOWTO.html)