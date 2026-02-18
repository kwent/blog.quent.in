---
aliases:
- /index.php/2011/08/mkvmerge-remuxer-une-saison-a-la-volee/
author: Quentin
categories:
- script
cover: /images/covers/mkvmerge-remuxer-une-saison-a-la-volee.png
date: '2011-08-04T11:39:30'
disqus_identifier: '382023060'
slug: mkvmerge-remuxer-une-saison-a-la-volee
tags:
- bash
- mkvmerge
- mkvtoolnix
- remux
- script
- synology
title: Mkvmerge | Remuxer une saison à la volée
---

Heureux possesseur d'un **NAS** <a href="http://www.synology.com/us/products/DS211j/index.php" target="_blank">Synology DS211j</a>, j'ai parfois besoin de remuxer **des saisons complètes de séries** (pour intégrer des sous titres la plupart du temps), et tant qu'à faire autant les remuxer **en local** sur le NAS.

Pour cela j'utilise le binaire **mkvmerge** contenu dans le package <a href="http://www.bunkus.org/videotools/mkvtoolnix/" target="_blank"><strong>mkvtoolnix</strong></a>.

<span style="color: #ff6600;"><strong>1ère étape:</strong></span> Récupérer le paquet mkvtoolnix et l'installer.

**Note:** Je ne récupère pas mkvtoolnix via le dépôt <a href="http://ipkg.nslu2-linux.org/feeds/optware/cs05q3armel/cross/unstable/" target="_blank">http://ipkg.nslu2-linux.org/feeds/optware/cs05q3armel/cross/unstable/</a> car celui-ci n'a pas fonctionné pour moi (manque de dépendances). **Voir <a href="http://forum.synology.com/enu/viewtopic.php?f=40&t=36845" target="_blank">ici</a>**.

```bash
wget mkvtoolnix http://www.rzuser.uni-heidelberg.de/~tkolb3/mkvtoolnix_4.2.0-1_arm.ipk
ipkg install mkvtoolnix_4.2.0-1_arm.ipk
```

Vous vous retrouvez face à une jolie erreur de **MD5** (c'est normal car ce n'est pas le paquet issu du dépôt officiel)

Il faut alors modifier le MD5 dans **/opt/lib/ipkg/lists/cross** de mkvtoolnix par celui-ci **0be20bd376391c911a7eeba46c8883ac **et réitérer l'opération.****

<span style="color: #ff6600;"><strong>2ème étape:</strong></span> mkvtoolnix est maintenant opérationnel sur le Synology, passons au remuxage !

### <span style="color: #333333;">Contexte:</span>

Soit **une saison** de** 23 épisodes **auxquelles je veux ajouter des **fichiers de sous titres (.srt) Français et Anglais, la structure étant la suivante:  
**

```plain
ls
01 - REMUX  # Dossier de destination
02 - FR_SRT # Contient les sous titres FR sous la forme Serie.SXXEXX.720p.HDTV.x264.srt
03 - EN_SRT # Contient les sous titres EN sous la forme Serie.SXXEXX.720p.HDTV.x264.srt
Serie.SXXE01.720p.HDTV.x264.mkv #Fichier à remuxer
Serie.SXXE02.720p.HDTV.x264.mkv #Fichier à remuxer
Serie.SXXE03.720p.HDTV.x264.mkv #Fichier à remuxer
Serie.SXXE04.720p.HDTV.x264.mkv #Fichier à remuxer
...
Serie.SXXE23.720p.HDTV.x264.mkv #Fichier à remuxer
```

On ajoute à cela un petit script reposant sur une **boucle for**.

```bash
#!/bin/bash

echo -e “Mkvmerge - Remux en série.”
PATH_TO_MEDIA=$3
FR_PATH=$4’/’
EN_PATH=$5’/’
OUTPUT_FOLDER=$6

echo -e “Remux des episodes $1 à l’épisode $2”
echo -e “Répértoire des médias à transcoder: $3”
echo -e “FR_PATH: $4”
echo -e “EN_PATH: $5”
echo -e “Notes: .srt files need to be in UTF-8 format”
echo -e “Répértoire de destination: $6”
echo -e

for i in `seq $1 $2`
do

#Prefix ‘0’ pour les épisodes < 10
if test $i -lt 10
then
namefile=“Serie.SXXE0$i.720p.HDTV.x264”
else
namefile=“Serie.SXXE$i.720p.HDTV.x264”
fi

echo -e “Media entrant: $PATH_TO_MEDIA/$namefile”
echo -e “Media sortant: $OUTPUT_FOLDER/$namefile”
echo -e “EN SRT: $EN_PATH$namefile.srt”
echo -e “FR SRT: $FR_PATH$namefile.srt”
mkvmerge -v -o “$OUTPUT_FOLDER/$namefile.mkv” “–language” “1:eng” “–default-track” “1:no” “–forced-track” “1:no” “–display-dimensions” “1:1280x720” “–default-track” “2:yes” “–forced-track” “2:no” “-a” “2” “-d” “1” “-S” “-T” “–no-global-tags” “–no-chapters” “$PATH_TO_MEDIA/$namefile.mkv” “–language” “0:eng” “–track-name” “0:English” “–default-track” “0:no” “–forced-track” “0:no” “-s” “0” “-D” “-A” “-T” “–no-global-tags” “–no-chapters” “$EN_PATH$namefile.srt” “–language” “0:fre” “–track-name” “0:French” “–forced-track” “0:no” “-s” “0” “-D” “-A” “-T” “–no-global-tags” “–no-chapters” “$FR_PATH$namefile.srt” “–track-order” “0:1,0:2,2:0,1:0”

done
```

**3ème étape:** Il ne reste plus qu'à appeler notre script de la façon suivante :

```bash
sh monscript 1 23 $FOLDER_TO_MEDIA $FR_SUBTITLES_FOLDER $EN_SUBTITLES_FOLDER $DESTINATION_FOLDER
sh monscript 1 23 “/Series/MaSerie/Saison X” “/Series/MaSerie/Saison X/02 - FR_SRT” “/Series/MaSerie/Saison X/03 - EN_SRT” “/Series/MaSerie/Saison X/01 - REMUX”
```

<span style="color: #ff0000;"><strong>Note</strong></span><span style="color: #ff0000;"><strong> 1</strong></span><span style="color: #ff0000;"><strong>:</strong></span> Dans l'état actuel du script, la langue française sera la langue **par défaut**. Pour changer ce comportement, jouez avec le paramètre suivante: **« -**default-track » « 2:yes »** ou **« **-default-track » « 0:no »******.

**<span style="color: #ff0000;">Note 2:</span>** Dans l'état actuel du script, les fichiers de sous titres (.srt) doivent être encodés au format **UTF-8**. Pour changer ce comportement, jouez avec le paramètre: **« -chapter-charset character-set »**

<span style="color: #ff0000;"><strong>Update:</strong> <span style="color: #000000;">Gist available with script update : <a href="https://gist.github.com/kwent/5382866">https://gist.github.com/kwent/5382866</a></span></span>

## More...

*   <a href="http://www.bunkus.org/videotools/mkvtoolnix/" title="mkvtoolnix -- Matroska tools for Linux/Unix and Windows" rel="nofollow">mkvtoolnix -- Matroska tools for Linux/Unix and Windows</a>
*   <a href="http://www.bunkus.org/videotools/mkvtoolnix/doc/mkvmerge.html" title="mkvmerge" rel="nofollow">mkvmerge</a>
*   <a href="http://www.synology.com/us/products/DS211j/index.php" title="Synology Network Attached Storage - Products :: DiskStation ..." rel="nofollow">Synology Network Attached Storage - Products :: DiskStation ...</a>