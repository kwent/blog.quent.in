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

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer">
          user@192.168.1.1<br /> user@192.168.1.2<br /> user@192.168.1.3
        </div>
      </td>
    </tr>
  </table>
</div>

2. Je lance **PSSH **en indiquant l&rsquo;emplacement du fichier ci-dessus****

****

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
          pssh <span class="re5">-P</span> <span class="re5">-h</span> ~<span class="sy0">/</span>nodes.txt <span class="re5">-A</span> <span class="st0">"<span class="es2">$MACOMMANDE</span>"</span>
        </div>
      </td>
    </tr>
  </table>
</div>

Et le tour est joué! Voici la sortie avec **MACOMMANDE=&rsquo;cat /etc/snmp/snmpd.conf | md5sum&rsquo;** (Vérifions si le fichier snmpd.conf est strictement identique sur nos 3 serveurs).

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          192.168.1.1: d41d8cd98f00b204e9800998ecf8427e -<br /> <span class="br0">&#91;</span><span class="nu0">1</span><span class="br0">&#93;</span> <span class="nu0">14</span>:<span class="nu0">16</span>:08 <span class="br0">&#91;</span>SUCCESS<span class="br0">&#93;</span> user<span class="sy0">@</span>192.168.1.1<br /> 192.168.1.2: d41d8cd98f00b204e9800998ecf8427e -<br /> <span class="br0">&#91;</span><span class="nu0">2</span><span class="br0">&#93;</span> <span class="nu0">14</span>:<span class="nu0">16</span>:08 <span class="br0">&#91;</span>SUCCESS<span class="br0">&#93;</span> user<span class="sy0">@</span>192.168.1.2<br /> 192.168.1.3: d41d8cd98f00b204e9800998ecf8427e -<br /> <span class="br0">&#91;</span><span class="nu0">3</span><span class="br0">&#93;</span> <span class="nu0">14</span>:<span class="nu0">16</span>:08 <span class="br0">&#91;</span>SUCCESS<span class="br0">&#93;</span> user<span class="sy0">@</span>192.168.1.3
        </div>
      </td>
    </tr>
  </table>
</div>

**3 MD5 identiques = 3 fichiers identiques**

Bien entendu, **<span style="color: #ff0000;">utilisez cet outil avec grande précaution</span>** et testez votre commande sur une machine test avant! En cas d&rsquo;erreur, ce sera l&rsquo;ensemble de vos serveurs configurés qui seront impactés&#8230;

<span style="text-decoration: underline;"><strong>Note</strong></span>**:** Il faut prélablement que les hosts soient connus par SSH dans **~/.ssh/known_hosts**

## En savoir plus&#8230;

*   <a href="http://www.linux.com/archive/feature/151340" title="Linux.com :: Parallel SSH execution and a single shell to ..." rel="nofollow">Linux.com :: Parallel SSH execution and a single shell to ...</a> ![][1]
*   <a href="http://www.theether.org/pssh/docs/0.2.3/pssh-HOWTO.html" title="pssh HOWTO" rel="nofollow">pssh HOWTO</a> ![][1]

 [1]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png