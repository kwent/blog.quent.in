---
aliases:
- /index.php/2012/04/save-time-and-energy-with-uml-diagram-generator-tools-online/
author: Quentin
categories:
- development
- script
- web
cover: /images/covers/save-time-and-energy-with-uml-diagram-generator-tools-online.png
date: '2012-04-30T10:55:05'
disqus_identifier: '670037950'
slug: save-time-and-energy-with-uml-diagram-generator-tools-online
tags:
- diagram
- generator
- uml
title: Save time and energy with UML diagram generator tools online !
---

### Introduction

During a software architecture report redaction, i was confronted to a major problem : I would generated some UML diagrams as **« Use Case »**, **« Class Diagram »** and **« Activity Diagram »** but i didn't have tools as **Microsoft Office Visio** or equivalent installed on my laptop. So i searched web tools to generate these diagrams easily.

### What i found ?

First website i found was **Web Sequence Diagram:** [www.websequencediagrams.com][1]  
Second website i found was **yUML**: [yuml.me][2]  
Third website i found was **KangaModeling**: [kangamodeling.org][3]

### Why these tools are powerful ?

#### 1. Scriptable

These tools allow to describe what we want with a **script language**.

**Example with Web Sequence Diagram Tool  **: ** **

```plain
# Show Action with RoR
Browser->URL Routing : GET
URL Routing->Controller : show Action
Controller -> Model : find ( params[id] )
Model -> Controller : trigger
Controller -> Controller : Lookup Show View
Controller -> View : Render ( Show View, trigger )

View -> Model : getData()
Model -> Trigger (Physical Element) : request() : SNMP / SOAP / XMLRPC / …
Trigger (Physical Element) -> Model : response : XML / JSON / …
Model -> View : data

View->Browser : HTML
```

**Activity diagram image generated :**  

![show Action RoR](/assets/wp-content/uploads/2012/04/index.png)

**Example with Web Sequence Diagram Tool  **: ****

```plain
[User]-(Show a monitor)
[User]-(Show monitor’s parameters)
[Administrator] - (Manage a monitor)
[Administrator] - (Manage users)
(Manage a monitor)>(Delete a monitor)
(Manage a monitor)>(Update a monitor)
(Manage a monitor)>(Add a monitor)
(Manage users)<(LDAP Active Directory)
```

**Use case diagram image generated :**  

![Use case generated with yUML](/assets/wp-content/uploads/2012/04/use-cases.png)

#### 2. Integration with other services

Both tools integrate an API.

They allow to integrate images in your website with just a **GET** or **POST** request.

**Example with yUML :**

```plain
http://yuml.me/diagram/class/[Customer]->[Billing Address]
```

**Will generate :**

![Yuml](http://yuml.me/diagram/class/[Customer]->[Billing%20Address]) 

####  3. Universal

Implementation with other language is very easy.

**Example with Python implementation :**

```python
import urllib
import re

def getSequenceDiagram( text, outputFile, style = ‘default’ ):
    request = {}
    request[“message”] = text
    request[“style”] = style
    request[“apiVersion”] = “1”

    url = urllib.urlencode(request)

    f = urllib.urlopen(“http://www.websequencediagrams.com/”, url)
    line = f.readline()
    f.close()

    expr = re.compile(”(\?(img|pdf|png|svg)=[a-zA-Z0-9]+)”)
    m = expr.search(line)

    if m == None:
        print “Invalid response from server.”
        return False

    urllib.urlretrieve(“http://www.websequencediagrams.com/” + m.group(),
            outputFile )
    return True

style = “qsd”
text = “alice->bob: authentication request\nbob–>alice: response”
pngFile = “out.png”

getSequenceDiagram( text, pngFile, style )
```

#### 4. Others skills

*   Diagram generation by command line;
*   Output formats as png, jpg, pdf, json;
*   A lot of fork projects in different languages.

<h4 style="text-align: center;">
  To resume, these tools will permit you to save time and energy. Exit graphic tools which are too much heavy, slow and onerous.
</h4>

## More...

*   <a href="http://creately.com/Draw-UML-and-Class-Diagrams-Online" title="Draw UML diagrams Online | Online UML Tool | UML Diagram Creator | Creately" rel="nofollow">Draw UML diagrams Online | Online UML Tool | UML Diagram Creator | Creately</a>
*   <a href="http://kangamodeling.org/" title="Kanga Modelling - Create Sequence Diagrams Using Markup Language">Kanga Modelling - Create Sequence Diagrams Using Markup Language</a>
*   <a href="http://www.gliffy.com/uses/uml-software/" title="UML Software - Free online UML editor - no download required" rel="nofollow">UML Software - Free online UML editor - no download required</a>
*   <a href="http://www.lucidchart.com/" title="Online Diagram & Flowchart Software | Lucidchart" rel="nofollow">Online Diagram & Flowchart Software | Lucidchart</a>
*   <a href="http://www.websequencediagrams.com/" title="No Title" rel="nofollow">www.websequencediagrams.com</a>
*   <a href="http://yuml.me/" title="Create UML diagrams online in seconds, no special tools needed." rel="nofollow">Create UML diagrams online in seconds, no special tools needed.</a>