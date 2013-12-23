---
title: Save time and energy with UML diagram generator tools online !
author: Quentin
layout: post
permalink: /index.php/2012/04/save-time-and-energy-with-uml-diagram-generator-tools-online/
hl_twitter_has_auto_tweeted:
  - 'I just posted Save time and energy with UML diagram generator tools online !, read it here: http://blog.quentinrousseau.fr/?p=480'
dsq_thread_id:
  - 670037950
categories:
  - Développement
  - Script
  - Web
tags:
  - diagram
  - generator
  - uml
---
### Introduction

During a software architecture report redaction, i was confronted to a major problem : I would generated some UML diagrams as **&laquo;&nbsp;Use Case&nbsp;&raquo;**, **&laquo;&nbsp;Class Diagram&nbsp;&raquo;** and **&laquo;&nbsp;Activity Diagram&nbsp;&raquo;** but i didn&rsquo;t have tools as **Microsoft Office Visio** or equivalent installed on my laptop. So i searched web tools to generate these diagrams easily.

### What i found ?

First website i found was **Web Sequence Diagram:** [www.websequencediagrams.com][1]  
Second website i found was **yUML**: [yuml.me][2]  
Third website i found was **KangaModeling**: [kangamodeling.org][3]

### Why these tools are powerful ?

#### 1. Scriptable

These tools allow to describe what we want with a **script language**.

**Example with Web Sequence Diagram Tool  **: ** **

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer">
          # Show Action with RoR<br /> Browser->URL Routing : GET<br /> URL Routing->Controller : show Action<br /> Controller -> Model : find ( params[id] )<br /> Model -> Controller : trigger<br /> Controller -> Controller : Lookup Show View<br /> Controller -> View : Render ( Show View, trigger )<br /> <br /> View -> Model : getData()<br /> Model -> Trigger (Physical Element) : request() : SNMP / SOAP / XMLRPC / ...<br /> Trigger (Physical Element) -> Model : response : XML / JSON / ...<br /> Model -> View : data<br /> <br /> View->Browser : HTML
        </div>
      </td>
    </tr>
  </table>
</div>

**Activity diagram image generated :**  
[<img class="aligncenter size-medium wp-image-483" title="show Action RoR" src="http://blog.quentinrousseau.fr/wp-content/uploads/2012/04/index.png" alt="" />][4]

**Example with Web Sequence Diagram Tool  **: ****

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer">
          [User]-(Show a monitor)<br /> [User]-(Show monitor's parameters)<br /> [Administrator] - (Manage a monitor)<br /> [Administrator] - (Manage users)<br /> (Manage a monitor)>(Delete a monitor)<br /> (Manage a monitor)>(Update a monitor)<br /> (Manage a monitor)>(Add a monitor)<br /> (Manage users)<(LDAP Active Directory)
        </div>
      </td>
    </tr>
  </table>
</div>

**Use case diagram image generated :**  
[<img class="aligncenter size-full wp-image-487" title="Use case generated with yUML" src="http://blog.quentinrousseau.fr/wp-content/uploads/2012/04/use-cases.png" alt="" width="953" height="427" />][5]

#### 2. Integration with other services

Both tools integrate an API.

They allow to integrate images in your website with just a **GET** or **POST** request.

**Example with yUML :**

<div class="codecolorer-container text default" style="overflow:auto;white-space:nowrap;width:618px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer">
          <img src="http://yuml.me/diagram/class/[Customer]->[Billing Address]" alt="" />
        </div>
      </td>
    </tr>
  </table>
</div>

**Will generate :**

<img class="aligncenter" src="http://yuml.me/diagram/class/[Customer]->[Billing Address]&nbsp;&raquo; alt=&nbsp;&raquo;" /> 
####  3. Universal

Implementation with other language is very easy.

**Example with Python implementation :**

<div class="codecolorer-container python default" style="overflow:auto;white-space:nowrap;width:618px;height:300px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />20<br />21<br />22<br />23<br />24<br />25<br />26<br />27<br />28<br />29<br />30<br />31<br />
        </div>
      </td>
      
      <td>
        <div class="python codecolorer">
          <span class="kw1">import</span> <span class="kw3">urllib</span><br /> <span class="kw1">import</span> <span class="kw3">re</span><br /> <br /> <span class="kw1">def</span> getSequenceDiagram<span class="br0">&#40;</span> text<span class="sy0">,</span> outputFile<span class="sy0">,</span> style <span class="sy0">=</span> <span class="st0">'default'</span> <span class="br0">&#41;</span>:<br /> &nbsp; &nbsp; request <span class="sy0">=</span> <span class="br0">&#123;</span><span class="br0">&#125;</span><br /> &nbsp; &nbsp; request<span class="br0">&#91;</span><span class="st0">"message"</span><span class="br0">&#93;</span> <span class="sy0">=</span> text<br /> &nbsp; &nbsp; request<span class="br0">&#91;</span><span class="st0">"style"</span><span class="br0">&#93;</span> <span class="sy0">=</span> style<br /> &nbsp; &nbsp; request<span class="br0">&#91;</span><span class="st0">"apiVersion"</span><span class="br0">&#93;</span> <span class="sy0">=</span> <span class="st0">"1"</span><br /> <br /> &nbsp; &nbsp; url <span class="sy0">=</span> <span class="kw3">urllib</span>.<span class="me1">urlencode</span><span class="br0">&#40;</span>request<span class="br0">&#41;</span><br /> <br /> &nbsp; &nbsp; f <span class="sy0">=</span> <span class="kw3">urllib</span>.<span class="me1">urlopen</span><span class="br0">&#40;</span><span class="st0">"http://www.websequencediagrams.com/"</span><span class="sy0">,</span> url<span class="br0">&#41;</span><br /> &nbsp; &nbsp; line <span class="sy0">=</span> f.<span class="kw3">readline</span><span class="br0">&#40;</span><span class="br0">&#41;</span><br /> &nbsp; &nbsp; f.<span class="me1">close</span><span class="br0">&#40;</span><span class="br0">&#41;</span><br /> <br /> &nbsp; &nbsp; expr <span class="sy0">=</span> <span class="kw3">re</span>.<span class="kw2">compile</span><span class="br0">&#40;</span><span class="st0">"(<span class="es0">\?</span>(img|pdf|png|svg)=[a-zA-Z0-9]+)"</span><span class="br0">&#41;</span><br /> &nbsp; &nbsp; m <span class="sy0">=</span> expr.<span class="me1">search</span><span class="br0">&#40;</span>line<span class="br0">&#41;</span><br /> <br /> &nbsp; &nbsp; <span class="kw1">if</span> m <span class="sy0">==</span> <span class="kw2">None</span>:<br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">print</span> <span class="st0">"Invalid response from server."</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span class="kw1">return</span> <span class="kw2">False</span><br /> <br /> &nbsp; &nbsp; <span class="kw3">urllib</span>.<span class="me1">urlretrieve</span><span class="br0">&#40;</span><span class="st0">"http://www.websequencediagrams.com/"</span> + m.<span class="me1">group</span><span class="br0">&#40;</span><span class="nu0"></span><span class="br0">&#41;</span><span class="sy0">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; outputFile <span class="br0">&#41;</span><br /> &nbsp; &nbsp; <span class="kw1">return</span> <span class="kw2">True</span><br /> <br /> style <span class="sy0">=</span> <span class="st0">"qsd"</span><br /> text <span class="sy0">=</span> <span class="st0">"alice->bob: authentication request<span class="es0">\n</span>bob-->alice: response"</span><br /> pngFile <span class="sy0">=</span> <span class="st0">"out.png"</span><br /> <br /> getSequenceDiagram<span class="br0">&#40;</span> text<span class="sy0">,</span> pngFile<span class="sy0">,</span> style <span class="br0">&#41;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

#### 4. Others skills

*   Diagram generation by command line;
*   Output formats as png, jpg, pdf, json;
*   A lot of fork projects in different languages.

<h4 style="text-align: center;">
  To resume, these tools will permit you to save time and energy. Exit graphic tools which are too much heavy, slow and onerous.
</h4>



## En savoir plus&#8230;

*   <a href="http://creately.com/Draw-UML-and-Class-Diagrams-Online" title="Draw UML diagrams Online | Online UML Tool | UML Diagram Creator | Creately" rel="nofollow">Draw UML diagrams Online | Online UML Tool | UML Diagram Creator | Creately</a> ![][6]
*   <a href="http://kangamodeling.org/" title="Kanga Modelling - Create Sequence Diagrams Using Markup Language" rel="nofollow">Kanga Modelling - Create Sequence Diagrams Using Markup Language</a> ![][6]
*   <a href="http://www.gliffy.com/uses/uml-software/" title="UML Software - Free online UML editor - no download required" rel="nofollow">UML Software - Free online UML editor - no download required</a> ![][6]
*   <a href="http://www.lucidchart.com/" title="Online Diagram & Flowchart Software | Lucidchart" rel="nofollow">Online Diagram & Flowchart Software | Lucidchart</a> ![][6]
*   <a href="http://www.websequencediagrams.com/" title="No Title" rel="nofollow">No Title</a> ![][6]
*   <a href="http://yuml.me/" title="Create UML diagrams online in seconds, no special tools needed." rel="nofollow">Create UML diagrams online in seconds, no special tools needed.</a> ![][6]

 [1]: http://www.websequencediagrams.com
 [2]: http://yuml.me
 [3]: http://kangamodeling.org
 [4]: http://blog.quentinrousseau.fr/wp-content/uploads/2012/04/index.png
 [5]: http://blog.quentinrousseau.fr/wp-content/uploads/2012/04/use-cases.png
 [6]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png