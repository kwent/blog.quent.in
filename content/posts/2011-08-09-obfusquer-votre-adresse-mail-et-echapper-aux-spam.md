---
aliases:
- /index.php/2011/08/obfusquer-votre-adresse-mail-et-echapper-aux-spam/
author: Quentin
categories:
- development
- script
- web
cover: /images/covers/obfusquer-votre-adresse-mail-et-echapper-aux-spam.png
date: '2011-08-09T18:32:20'
disqus_identifier: '381555879'
slug: obfusquer-votre-adresse-mail-et-echapper-aux-spam
tags:
- email
- javascript
- mail
- navigateur
- obfuscation
- spam
title: Obfusquer votre adresse mail et échapper aux SPAM
---

![Spam in mailbox](/images/posts/spam-300x199.jpg)

Il nous arrive bien souvent de devoir renseigner notre **@mail** au sein d'une page web.  
Seulement il est essentiel de prendre des précautions sur la manière de la renseigner face au **SPAM**.  
En effet, une @mail renseignée en **simple texte** est **facilement détectable par un robot** (via une simple expression régulière par exemple) et en moins de quelques secondes, vous voilà inscrit sur une liste de SPAM **contre votre volonté**.

Des méthodes sont déjà utilisées pour essayer de palier à ce problème:

**<span style="color: #333333;">1°</span> Obfuscation textuelle**

```plain
Remplacer @ et . par "[at]" et "[dot]"
email[at]domain[dot]com
```

> **<span style="color: #339966;">Avantages</span>**
> 
> *   <span style="color: #339966;"><span style="color: #000000;">Obfuscation efficace et implémentation simple.<br /> </span></span>
> 
> **<span style="color: #ff0000;">Inconvénients</span>**
> 
> *   <span style="color: #ff0000;"><span style="color: #000000;">Impossibilité de construire un mailto.</span></span>

**<span style="color: #333333;">2°</span> Obfuscation par CSS**

```html
<span class=“obfuscate”>moc.niamod@liame</span>
```
```css
/* Et le renverse via CSS */
.obfuscate { unicode-bidi: bidi-override; direction: rtl; }
```

> **<span style="color: #339966;">Avantages</span>**
> 
> *   <span style="color: #000000;">Obfuscation très efficace.</span>
> 
> **<span style="color: #ff0000;">Inconvénients</span>**
> 
> *   <span style="color: #000000;">Impossibilité de construire un mailto.</span>
> *   <span style="color: #000000;">Si le CSS n'est pas disponible, l'@mail s'affichera à l'envers.<br /> </span>

**<span style="color: #333333;">3°</span> Obfuscation par JavaScript**

La plupart des robots** n'exécutent pas** de Javascript (pour des questions de performance et pour ne pas se faire tracer, j'imagine...). Alors on peut s'amuser à utiliser des algorithmes tels que le [**ROT13**][1] *(rotate by 13 places)*.

```javascript

Rot13 = {
    map: null,

    convert: function(a) {
        Rot13.init();

        var s = ””;
        for (i=; i < a.length; i++) {
            var b = a.charAt(i);
            s += ((b>=‘A’ && b<=‘Z’) || (b>=‘a’ && b<=‘z’) ? Rot13.map[b] : b);
        }
        return s;
    },

    init: function() {
        if (Rot13.map != null)
            return;
              
        var map = new Array();
        var s   = “abcdefghijklmnopqrstuvwxyz”;

        for (i=; i<s.length; i++)
            map[s.charAt(i)] = s.charAt((i+13)%26);
        for (i=; i<s.length; i++)
            map[s.charAt(i).toUpperCase()] = s.charAt((i+13)%26).toUpperCase();

        Rot13.map = map;
    },

    write: function(a) {
        document.write(Rot13.convert(a));
    }
}

```
```html
<script type=“text/javascript”>
   Rot13.write(’rznvy@qbznva.pbz);
</script>
```

> <span style="color: #339966;"><strong>Avantages</strong></span>
> 
> *   <span style="color: #000000;">Obfuscation très efficace.</span>
> 
> <span style="color: #ff0000;"><strong>Inconvénients</strong></span>
> 
> *   <span style="color: #000000;">Si le client web ne supporte pas le JavaScript, aucune @mail ne sera affichée.</span>

D'autres solutions existent comme afficher l'@mail **dans une image** mais les robots utilisent des techniques **de reconnaissance optique de caractères** au sein d'une image: l'OCR.

![Email address embedded in an image](/images/posts/mail.png)

### Tests grandeur nature

Un collège de **<a href="https://techblog.tilllate.com/2008/07/20/ten-methods-to-obfuscate-e-mail-addresses-compared/" target="_blank">techblog</a>** nous invite à regarder** le volume de SPAM reçu en fonction des différentes méthodes d'obsfuscation** après avoir laissé ses @mail dans la nature pendant **1 an et demi**.

<div style="width: 440px" class="wp-caption aligncenter">
  <img title="Méthodes d'obfuscation" src="https://techblog.tilllate.com/images/posts/obfuscation_methods.png" alt="" width="430" height="317" /><p class="wp-caption-text">
    Volume de SPAM reçu en fonction des différentes méthodes d'obfuscation
  </p>
</div>

Les résultats parlent d'eux même, **<span style="color: #ff0000;">ne renseignez pas</span>** (même sous la torture) votre @mail en **simple texte **! Utilisez au minimum la méthode n°1, qui diminue fortement les chances d'être détecté par un robot.

## More...

*   <a href="https://fr.wikipedia.org/wiki/ROT13" title="ROT13 - Wikipédia" rel="nofollow">ROT13 - Wikipédia</a>
*   <a href="https://fr.wikipedia.org/wiki/Spam" title="Spam - Wikipédia" rel="nofollow">Spam - Wikipédia</a>
*   <a href="https://hivelogic.com/enkoder/" title="Enkoder" rel="nofollow">Enkoder</a>
*   <a href="https://perishablepress.com/press/2010/08/01/best-method-for-email-obfuscation/" title="Best Method for Email Obfuscation? • Perishable Press" rel="nofollow">Best Method for Email Obfuscation? • Perishable Press</a>
*   <a href="https://scott.yang.id.au/2003/06/obfuscate-email-address-with-javascript-rot13/" title="Obfuscate Email Address With Javascript Rot13 | SYP" rel="nofollow">Obfuscate Email Address With Javascript Rot13 | SYP</a>
*   <a href="https://www.mailtoencoder.com/" title="Encode your email address with javascript to prevent spam ..." rel="nofollow">Encode your email address with javascript to prevent spam ...</a>