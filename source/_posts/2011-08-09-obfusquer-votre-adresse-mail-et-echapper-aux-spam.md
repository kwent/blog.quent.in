---
title: Obfusquer votre adresse mail et échapper aux SPAM
author: Quentin
layout: post
permalink: /index.php/2011/08/obfusquer-votre-adresse-mail-et-echapper-aux-spam/
hl_twitter_has_auto_tweeted:
  - 'I just posted Obfusquer votre adresse mail et échapper aux SPAM, read it here: http://blog.quentinrousseau.fr/?p=134'
dsq_thread_id:
  - 381555879
categories:
  - Développement
  - Script
  - Web
tags:
  - email
  - javascript
  - mail
  - navigateur
  - obfuscation
  - spam
---
<img class="alignleft size-medium wp-image-184" style="border: none;" title="Spam in mailbox" src="http://blog.quentinrousseau.fr/wp-content/uploads/2011/08/spam-300x199.jpg" alt="" width="216" height="147" />  
Il nous arrive bien souvent de devoir renseigner notre **@mail** au sein d&rsquo;une page web.  
Seulement il est essentiel de prendre des précautions sur la manière de la renseigner face au **SPAM**.  
En effet, une @mail renseignée en **simple texte** est **facilement détectable par un robot** (via une simple expression régulière par exemple) et en moins de quelques secondes, vous voilà inscrit sur une liste de SPAM **contre votre volonté**.

Des méthodes sont déjà utilisées pour essayer de palier à ce problème:

**<span style="color: #333333;">1°</span> Obfuscation textuelle**

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer">
          # Remplacer @ et . par "[at]" et "[dot]"<br /> email[at]domain[dot]com
        </div>
      </td>
    </tr>
  </table>
</div>

> **<span style="color: #339966;">Avantages</span>**
> 
> *   <span style="color: #339966;"><span style="color: #000000;">Obfuscation efficace et implémentation simple.<br /> </span></span>
> 
> **<span style="color: #ff0000;">Inconvénients</span>**
> 
> *   <span style="color: #ff0000;"><span style="color: #000000;">Impossibilité de construire un mailto.</span></span>

**<span style="color: #333333;">2°</span> Obfuscation par CSS**

<div class="codecolorer-container html4strict default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />
        </div>
      </td>
      
      <td>
        <div class="html4strict codecolorer">
          <span class="sc2"><<a href="http://december.com/html/4/element/span.html"><span class="kw2">span</span></a> <span class="kw3">class</span><span class="sy0">=</span><span class="st0">"obfuscate"</span>></span>moc.niamod@liame<span class="sc2"><<span class="sy0">/</span><a href="http://december.com/html/4/element/span.html"><span class="kw2">span</span></a>></span>
        </div>
      </td>
    </tr>
  </table>
</div>

<div class="codecolorer-container css default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />
        </div>
      </td>
      
      <td>
        <div class="css codecolorer">
          <span class="coMULTI">/* Et le renverse via CSS */</span><br /> <span class="re1">.obfuscate</span> <span class="br0">&#123;</span> <span class="kw1">unicode-bidi</span><span class="sy0">:</span> <span class="kw2">bidi-override</span><span class="sy0">;</span> <span class="kw1">direction</span><span class="sy0">:</span> rtl<span class="sy0">;</span> <span class="br0">&#125;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

> **<span style="color: #339966;">Avantages</span>**
> 
> *   <span style="color: #000000;">Obfuscation très efficace.</span>
> 
> **<span style="color: #ff0000;">Inconvénients</span>**
> 
> *   <span style="color: #000000;">Impossibilité de construire un mailto.</span>
> *   <span style="color: #000000;">Si le CSS n&rsquo;est pas disponible, l&rsquo;@mail s&rsquo;affichera à l&rsquo;envers.<br /> </span>

**<span style="color: #333333;">3°</span> Obfuscation par JavaScript**

La plupart des robots** n&rsquo;exécutent pas** de Javascript (pour des questions de performance et pour ne pas se faire tracer, j&rsquo;imagine&#8230;). Alors on peut s&rsquo;amuser à utiliser des algorithmes tels que le [**ROT13**][1] *(rotate by 13 places)*.

<div class="codecolorer-container javascript default" style="overflow:auto;white-space:nowrap;width:618px;height:300px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />20<br />21<br />22<br />23<br />24<br />25<br />26<br />27<br />28<br />29<br />30<br />31<br />32<br />33<br />
        </div>
      </td>
      
      <td>
        <div class="javascript codecolorer">
          Rot13 <span class="sy0">=</span> <span class="br0">&#123;</span><br /> &nbsp; &nbsp; map<span class="sy0">:</span> <span class="kw2">null</span><span class="sy0">,</span><br /> <br /> &nbsp; &nbsp; convert<span class="sy0">:</span> <span class="kw2">function</span><span class="br0">&#40;</span>a<span class="br0">&#41;</span> <span class="br0">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; Rot13.<span class="me1">init</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> <br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw2">var</span> s <span class="sy0">=</span> <span class="st0">""</span><span class="sy0">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">for</span> <span class="br0">&#40;</span>i<span class="sy0">=</span><span class="nu0"></span><span class="sy0">;</span> i <span class="sy0"><</span> a.<span class="me1">length</span><span class="sy0">;</span> i<span class="sy0">++</span><span class="br0">&#41;</span> <span class="br0">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw2">var</span> b <span class="sy0">=</span> a.<span class="me1">charAt</span><span class="br0">&#40;</span>i<span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; s <span class="sy0">+=</span> <span class="br0">&#40;</span><span class="br0">&#40;</span>b<span class="sy0">>=</span><span class="st0">'A'</span> <span class="sy0">&&</span> b<span class="sy0"><=</span><span class="st0">'Z'</span><span class="br0">&#41;</span> <span class="sy0">||</span> <span class="br0">&#40;</span>b<span class="sy0">>=</span><span class="st0">'a'</span> <span class="sy0">&&</span> b<span class="sy0"><=</span><span class="st0">'z'</span><span class="br0">&#41;</span> <span class="sy0">?</span> Rot13.<span class="me1">map</span><span class="br0">&#91;</span>b<span class="br0">&#93;</span> <span class="sy0">:</span> b<span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="br0">&#125;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">return</span> s<span class="sy0">;</span><br /> &nbsp; &nbsp; <span class="br0">&#125;</span><span class="sy0">,</span><br /> <br /> &nbsp; &nbsp; init<span class="sy0">:</span> <span class="kw2">function</span><span class="br0">&#40;</span><span class="br0">&#41;</span> <span class="br0">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">if</span> <span class="br0">&#40;</span>Rot13.<span class="me1">map</span> <span class="sy0">!=</span> <span class="kw2">null</span><span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">return</span><span class="sy0">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw2">var</span> map <span class="sy0">=</span> <span class="kw2">new</span> Array<span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw2">var</span> s &nbsp; <span class="sy0">=</span> <span class="st0">"abcdefghijklmnopqrstuvwxyz"</span><span class="sy0">;</span><br /> <br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">for</span> <span class="br0">&#40;</span>i<span class="sy0">=</span><span class="nu0"></span><span class="sy0">;</span> i<span class="sy0"><</span>s.<span class="me1">length</span><span class="sy0">;</span> i<span class="sy0">++</span><span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; map<span class="br0">&#91;</span>s.<span class="me1">charAt</span><span class="br0">&#40;</span>i<span class="br0">&#41;</span><span class="br0">&#93;</span> <span class="sy0">=</span> s.<span class="me1">charAt</span><span class="br0">&#40;</span><span class="br0">&#40;</span>i<span class="sy0">+</span><span class="nu0">13</span><span class="br0">&#41;</span><span class="sy0">%</span>26<span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">for</span> <span class="br0">&#40;</span>i<span class="sy0">=</span><span class="nu0"></span><span class="sy0">;</span> i<span class="sy0"><</span>s.<span class="me1">length</span><span class="sy0">;</span> i<span class="sy0">++</span><span class="br0">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; map<span class="br0">&#91;</span>s.<span class="me1">charAt</span><span class="br0">&#40;</span>i<span class="br0">&#41;</span>.<span class="me1">toUpperCase</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="br0">&#93;</span> <span class="sy0">=</span> s.<span class="me1">charAt</span><span class="br0">&#40;</span><span class="br0">&#40;</span>i<span class="sy0">+</span><span class="nu0">13</span><span class="br0">&#41;</span><span class="sy0">%</span>26<span class="br0">&#41;</span>.<span class="me1">toUpperCase</span><span class="br0">&#40;</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> <br /> &nbsp; &nbsp; &nbsp; &nbsp; Rot13.<span class="me1">map</span> <span class="sy0">=</span> map<span class="sy0">;</span><br /> &nbsp; &nbsp; <span class="br0">&#125;</span><span class="sy0">,</span><br /> <br /> &nbsp; &nbsp; <span class="kw1">write</span><span class="sy0">:</span> <span class="kw2">function</span><span class="br0">&#40;</span>a<span class="br0">&#41;</span> <span class="br0">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; document.<span class="kw1">write</span><span class="br0">&#40;</span>Rot13.<span class="me1">convert</span><span class="br0">&#40;</span>a<span class="br0">&#41;</span><span class="br0">&#41;</span><span class="sy0">;</span><br /> &nbsp; &nbsp; <span class="br0">&#125;</span><br /> <span class="br0">&#125;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

<div class="codecolorer-container html4strict default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />
        </div>
      </td>
      
      <td>
        <div class="html4strict codecolorer">
          <span class="sc2"><<a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a> <span class="kw3">type</span><span class="sy0">=</span><span class="st0">"text/javascript"</span>></span><br /> // <span class="sc-2"><![CDATA[</span><br /> <span class="sc-2"> &nbsp; &nbsp;Rot13.write('<n uers="rznvy@qbznva.pbz">rznvy@qbznva.pbz</n>);</span><br /> <span class="sc-2">// ]]></span><br /> <span class="sc2"><<span class="sy0">/</span><a href="http://december.com/html/4/element/script.html"><span class="kw2">script</span></a>></span>
        </div>
      </td>
    </tr>
  </table>
</div>

> <span style="color: #339966;"><strong>Avantages</strong></span>
> 
> *   <span style="color: #000000;">Obfuscation très efficace.</span>
> 
> <span style="color: #ff0000;"><strong>Inconvénients</strong></span>
> 
> *   <span style="color: #000000;">Si le client web ne supporte pas le JavaScript, aucune @mail ne sera affichée.</span>

D&rsquo;autres solutions existent comme afficher l&rsquo;@mail **dans une image** mais les robots utilisent des techniques **de reconnaissance optique de caractères** au sein d&rsquo;une image: l&rsquo;[OCR][2]

<p style="text-align: center;">
  <img class="aligncenter size-full wp-image-213" style="border: none; background: transparent;" title="email" src="http://blog.quentinrousseau.fr/wp-content/uploads/2011/08/mail.png" alt="Email address embedded in an image." width="191" height="35" />
</p>

### Tests grandeur nature

Un collège de **<a href="http://techblog.tilllate.com/2008/07/20/ten-methods-to-obfuscate-e-mail-addresses-compared/" target="_blank">techblog</a>** nous invite à regarder** le volume de SPAM reçu en fonction des différentes méthodes d&rsquo;obsfuscation** après avoir laissé ses @mail dans la nature pendant **1 an et demi**.

<div style="width: 440px" class="wp-caption aligncenter">
  <img title="Méthodes d'obfuscation" src="http://techblog.tilllate.com/wp-content/uploads/2008/07/obfuscation_methods.png" alt="" width="430" height="317" /><p class="wp-caption-text">
    Volume de SPAM reçu en fonction des différentes méthodes d'obfuscation
  </p>
</div>

&nbsp;

Les résultats parlent d&rsquo;eux même, **<span style="color: #ff0000;">ne renseignez pas</span>** (même sous la torture) votre @mail en **simple texte **! Utilisez au minimum la méthode n°1, qui diminue fortement les chances d&rsquo;être détecté par un robot.

## En savoir plus&#8230;

*   <a href="http://fr.wikipedia.org/wiki/ROT13" title="ROT13 - Wikipédia" rel="nofollow">ROT13 - Wikipédia</a> ![][3]
*   <a href="http://fr.wikipedia.org/wiki/Spam" title="Spam - Wikipédia" rel="nofollow">Spam - Wikipédia</a> ![][3]
*   <a href="http://hivelogic.com/enkoder/" title="Enkoder" rel="nofollow">Enkoder</a> ![][3]
*   <a href="http://perishablepress.com/press/2010/08/01/best-method-for-email-obfuscation/" title="Best Method for Email Obfuscation? • Perishable Press" rel="nofollow">Best Method for Email Obfuscation? • Perishable Press</a> ![][3]
*   <a href="http://scott.yang.id.au/2003/06/obfuscate-email-address-with-javascript-rot13/" title="Obfuscate Email Address With Javascript Rot13 | SYP" rel="nofollow">Obfuscate Email Address With Javascript Rot13 | SYP</a> ![][3]
*   <a href="http://www.mailtoencoder.com/" title="Encode your email address with javascript to prevent spam ..." rel="nofollow">Encode your email address with javascript to prevent spam ...</a> ![][3]

 [1]: http://fr.wikipedia.org/wiki/ROT13
 [2]: http://fr.wikipedia.org/wiki/Optical_character_recognition
 [3]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png