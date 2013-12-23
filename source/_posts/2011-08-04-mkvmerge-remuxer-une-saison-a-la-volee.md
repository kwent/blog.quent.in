---
title: Mkvmerge | Remuxer une saison à la volée
author: Quentin
layout: post
permalink: /index.php/2011/08/mkvmerge-remuxer-une-saison-a-la-volee/
dsq_thread_id:
  - 382023060
hl_twitter_has_auto_tweeted:
  - 'I just posted Mkvmerge | Remuxer une saison à la volée, read it here: http://blog.quentinrousseau.fr/?p=73'
categories:
  - Script
tags:
  - bash
  - mkvmerge
  - mkvtoolnix
  - remux
  - Script
  - Synology
---
Heureux possesseur d&rsquo;un **NAS** <a href="http://www.synology.com/us/products/DS211j/index.php" target="_blank">Synology DS211j</a>, j&rsquo;ai parfois besoin de remuxer **des saisons complètes de séries** (pour intégrer des sous titres la plupart du temps), et tant qu&rsquo;à faire autant les remuxer **en local** sur le NAS.

Pour cela j&rsquo;utilise le binaire **mkvmerge** contenu dans le package <a href="http://www.bunkus.org/videotools/mkvtoolnix/" target="_blank"><strong>mkvtoolnix</strong></a>.

<span style="color: #ff6600;"><strong>1ère étape:</strong></span> Récupérer le paquet mkvtoolnix et l&rsquo;installer.

**Note:** Je ne récupère pas mkvtoolnix via le dépôt <a href="http://ipkg.nslu2-linux.org/feeds/optware/cs05q3armel/cross/unstable/" target="_blank">http://ipkg.nslu2-linux.org/feeds/optware/cs05q3armel/cross/unstable/</a> car celui-ci n&rsquo;a pas fonctionné pour moi (manque de dépendances). **Voir <a href="http://forum.synology.com/enu/viewtopic.php?f=40&t=36845" target="_blank">ici</a>**.

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
          <span class="kw2">wget</span> mkvtoolnix http:<span class="sy0">//</span>www.rzuser.uni-heidelberg.de<span class="sy0">/</span>~tkolb3<span class="sy0">/</span>mkvtoolnix_4.2.0-<span class="nu0">1</span>_arm.ipk<br /> <br /> ipkg <span class="kw2">install</span> mkvtoolnix_4.2.0-<span class="nu0">1</span>_arm.ipk
        </div>
      </td>
    </tr>
  </table>
</div>

Vous vous retrouvez face à une jolie erreur de **MD5** (c&rsquo;est normal car ce n&rsquo;est pas le paquet issu du dépôt officiel)

Il faut alors modifier le MD5 dans **/opt/lib/ipkg/lists/cross** de mkvtoolnix par celui-ci **0be20bd376391c911a7eeba46c8883ac **et réitérer l&rsquo;opération.****

<span style="color: #ff6600;"><strong>2ème étape:</strong></span> mkvtoolnix est maintenant opérationnel sur le Synology, passons au remuxage !****

### <span style="color: #333333;">Contexte:</span>

Soit **une saison** de** 23 épisodes **auxquelles je veux ajouter des **fichiers de sous titres (.srt) Français et Anglais, la structure étant la suivante:  
**

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="kw2">ls</span><br /> 01 - REMUX  <span class="co0"># Dossier de destination</span><br /> 02 - FR_SRT <span class="co0"># Contient les sous titres FR sous la forme Serie.SXXEXX.720p.HDTV.x264.srt</span><br /> 03 - EN_SRT <span class="co0"># Contient les sous titres EN sous la forme Serie.SXXEXX.720p.HDTV.x264.srt</span><br /> Serie.SXXE01.720p.HDTV.x264.mkv <span class="co0">#Fichier à remuxer</span><br /> Serie.SXXE02.720p.HDTV.x264.mkv <span class="co0">#Fichier à remuxer</span><br /> Serie.SXXE03.720p.HDTV.x264.mkv <span class="co0">#Fichier à remuxer</span><br /> Serie.SXXE04.720p.HDTV.x264.mkv <span class="co0">#Fichier à remuxer</span><br /> ...<br /> Serie.SXXE23.720p.HDTV.x264.mkv <span class="co0">#Fichier à remuxer</span>
        </div>
      </td>
    </tr>
  </table>
</div>

On ajoute à cela un petit script reposant sur une **boucle for**.

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;height:300px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />20<br />21<br />22<br />23<br />24<br />25<br />26<br />27<br />28<br />29<br />30<br />31<br />32<br />33<br />34<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="co0">#!/bin/bash</span><br /> <br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Mkvmerge - Remux en série."</span><br /> <span class="re2">PATH_TO_MEDIA</span>=<span class="re4">$3</span><br /> <span class="re2">FR_PATH</span>=<span class="re4">$4</span><span class="st_h">'/'</span><br /> <span class="re2">EN_PATH</span>=<span class="re4">$5</span><span class="st_h">'/'</span><br /> <span class="re2">OUTPUT_FOLDER</span>=<span class="re4">$6</span><br /> <br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Remux des episodes $1 à l'épisode $2"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Répértoire des médias à transcoder: $3"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"FR_PATH: $4"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"EN_PATH: $5"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Notes: .srt files need to be in UTF-8 format"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Répértoire de destination: $6"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span><br /> <br /> <span class="kw1">for</span> i <span class="kw1">in</span> <span class="sy0">`</span><span class="kw2">seq</span> <span class="re4">$1</span> <span class="re4">$2</span><span class="sy0">`</span><br /> <span class="kw1">do</span><br /> <br /> <span class="co0">#Prefix '0' pour les épisodes < 10</span><br /> <span class="kw1">if</span> <span class="kw3">test</span> <span class="re1">$i</span> <span class="re5">-lt</span> <span class="nu0">10</span><br /> <span class="kw1">then</span><br /> <span class="re2">namefile</span>=<span class="st0">"Serie.SXXE0<span class="es2">$i</span>.720p.HDTV.x264"</span><br /> <span class="kw1">else</span><br /> <span class="re2">namefile</span>=<span class="st0">"Serie.SXXE<span class="es2">$i</span>.720p.HDTV.x264"</span><br /> <span class="kw1">fi</span><br /> <br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Media entrant: <span class="es2">$PATH_TO_MEDIA</span>/<span class="es2">$namefile</span>"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"Media sortant: <span class="es2">$OUTPUT_FOLDER</span>/<span class="es2">$namefile</span>"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"EN SRT: <span class="es2">$EN_PATH</span><span class="es2">$namefile</span>.srt"</span><br /> <span class="kw3">echo</span> <span class="re5">-e</span> <span class="st0">"FR SRT: <span class="es2">$FR_PATH</span><span class="es2">$namefile</span>.srt"</span><br /> mkvmerge <span class="re5">-v</span> <span class="re5">-o</span> <span class="st0">"<span class="es2">$OUTPUT_FOLDER</span>/<span class="es2">$namefile</span>.mkv"</span> <span class="st0">"--language"</span> <span class="st0">"1:eng"</span> <span class="st0">"--default-track"</span> <span class="st0">"1:no"</span> <span class="st0">"--forced-track"</span> <span class="st0">"1:no"</span> <span class="st0">"--display-dimensions"</span> <span class="st0">"1:1280x720"</span> <span class="st0">"--default-track"</span> <span class="st0">"2:yes"</span> <span class="st0">"--forced-track"</span> <span class="st0">"2:no"</span> <span class="st0">"-a"</span> <span class="st0">"2"</span> <span class="st0">"-d"</span> <span class="st0">"1"</span> <span class="st0">"-S"</span> <span class="st0">"-T"</span> <span class="st0">"--no-global-tags"</span> <span class="st0">"--no-chapters"</span> <span class="st0">"<span class="es2">$PATH_TO_MEDIA</span>/<span class="es2">$namefile</span>.mkv"</span> <span class="st0">"--language"</span> <span class="st0">"0:eng"</span> <span class="st0">"--track-name"</span> <span class="st0">"0:English"</span> <span class="st0">"--default-track"</span> <span class="st0">"0:no"</span> <span class="st0">"--forced-track"</span> <span class="st0">"0:no"</span> <span class="st0">"-s"</span> <span class="st0">"0"</span> <span class="st0">"-D"</span> <span class="st0">"-A"</span> <span class="st0">"-T"</span> <span class="st0">"--no-global-tags"</span> <span class="st0">"--no-chapters"</span> <span class="st0">"<span class="es2">$EN_PATH</span><span class="es2">$namefile</span>.srt"</span> <span class="st0">"--language"</span> <span class="st0">"0:fre"</span> <span class="st0">"--track-name"</span> <span class="st0">"0:French"</span> <span class="st0">"--forced-track"</span> <span class="st0">"0:no"</span> <span class="st0">"-s"</span> <span class="st0">"0"</span> <span class="st0">"-D"</span> <span class="st0">"-A"</span> <span class="st0">"-T"</span> <span class="st0">"--no-global-tags"</span> <span class="st0">"--no-chapters"</span> <span class="st0">"<span class="es2">$FR_PATH</span><span class="es2">$namefile</span>.srt"</span> <span class="st0">"--track-order"</span> <span class="st0">"0:1,0:2,2:0,1:0"</span><br /> <br /> <span class="kw1">done</span>
        </div>
      </td>
    </tr>
  </table>
</div>

**3ème étape:** Il ne reste plus qu&rsquo;à appeler notre script de la façon suivante :

<div class="codecolorer-container bash default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer">
          <span class="co0"># sh monscript 1 23 $FOLDER_TO_MEDIA $FR_SUBTITLES_FOLDER $EN_SUBTITLES_FOLDER $DESTINATION_FOLDER</span><br /> <span class="kw2">sh</span> monscript <span class="nu0">1</span> <span class="nu0">23</span> <span class="st0">"/Series/MaSerie/Saison X"</span> <span class="st0">"/Series/MaSerie/Saison X/02 - FR_SRT"</span> <span class="st0">"/Series/MaSerie/Saison X/03 - EN_SRT"</span> <span class="st0">"/Series/MaSerie/Saison X/01 - REMUX"</span>
        </div>
      </td>
    </tr>
  </table>
</div>

<span style="color: #ff0000;"><strong>Note</strong></span><span style="color: #ff0000;"><strong> 1</strong></span><span style="color: #ff0000;"><strong>:</strong></span> Dans l&rsquo;état actuel du script, la langue française sera la langue **par défaut**. Pour changer ce comportement, jouez avec le paramètre suivante: **&laquo;&nbsp;&#8211;**default-track&nbsp;&raquo; &laquo;&nbsp;2:yes&nbsp;&raquo;** ou **&laquo;&nbsp;**&#8211;default-track&nbsp;&raquo; &laquo;&nbsp;0:no&nbsp;&raquo;******.

**<span style="color: #ff0000;">Note 2:</span>** Dans l&rsquo;état actuel du script, les fichiers de sous titres (.srt) doivent être encodés au format **UTF-8**. Pour changer ce comportement, jouez avec le paramètre: **&laquo;&nbsp;&#8211;chapter-charset character-set&nbsp;&raquo;**

<span style="color: #ff0000;"><strong>Update:</strong> <span style="color: #000000;">Gist available with script update : <a href="https://gist.github.com/kwent/5382866">https://gist.github.com/kwent/5382866</a></span></span>

## En savoir plus&#8230;

*   <a href="http://www.bunkus.org/videotools/mkvtoolnix/" title="mkvtoolnix -- Matroska tools for Linux/Unix and Windows" rel="nofollow">mkvtoolnix -- Matroska tools for Linux/Unix and Windows</a> ![][1]
*   <a href="http://www.bunkus.org/videotools/mkvtoolnix/doc/mkvmerge.html" title="mkvmerge" rel="nofollow">mkvmerge</a> ![][1]
*   <a href="http://www.synology.com/us/products/DS211j/index.php" title="Synology Network Attached Storage - Products :: DiskStation ..." rel="nofollow">Synology Network Attached Storage - Products :: DiskStation ...</a> ![][1]

 [1]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png