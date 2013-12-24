---
title: 'PhotoCatch | Déclenchement automatisé d&rsquo;un appareil photo D90 à partir d&rsquo;un capteur de mouvements et d&rsquo;un Arduino'
author: Quentin
layout: post
permalink: /index.php/2012/01/photocatch-declenchement-automatise-dun-appareil-photo-d90-a-partir-dun-capteur-de-mouvements-et-dun-arduino/
hl_twitter_has_auto_tweeted:
  - 'I just posted PhotoCatch | Déclenchement automatisé d&#8217;un appareil photo D90 à partir d&#8217;un capteur de mouvements et d&#8217...'
dsq_thread_id:
  - 557476527
categories:
  - Développement
tags:
  - appareil photo
  - arduino
  - d90
  - electronique
  - fablab
date: Mon, 30 Jan 2012 09:21:03 -8000
---
Dans mon dernier post, je parlais de notre réalisation lors du FabLab à savoir :

**Un appareil photo avec déclenchement automatisé via un capteur de mouvement et un arduino.**

Aujourd&rsquo;hui, je vais détailler le montage de cette réalisation.

<p style="text-align: center;">
  <a href="http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/photoCatch.png"><img class="size-medium wp-image-307 aligncenter" title="PhotoCatch" src="http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/photoCatch-279x300.png" alt="" width="279" height="300" /></a>
</p>

### Le matériel

```plain
Un boîtier NIKON D90
Une télécommande filaire premier prix (Disponible [ici][1])
Un arduino uno
Un servomoteur
Un capteur ultrasons
Une breadboard
Quatres afficheurs 7 segments
Une touche de talent
```

### PhotoCatch &#8211; Etape par étape

<div id="attachment_323" style="width: 222px" class="wp-caption aligncenter">
  <a href="http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/A2_biss.jpg"><img class="size-medium wp-image-323" title="PhotoCatch" src="http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/A2_biss-212x300.jpg" alt="" width="212" height="300" /></a><p class="wp-caption-text">
    Principe de PhotoCatch
  </p>
</div>

### Achat de la télécommande

1.  La première étape consiste à acheter une télécommande qui va piloter le déclenchement de l&rsquo;appareil photo. Celle ci suffit amplement : <a href="http://quent.in/Af9bg0" target="_blank">http://quent.in/Af9bg0</a>
2.  Couper délicatement l&rsquo;extrémité de la télécommande afin de ne pas détériorer les 3 fils qui se cachent sous la gaîne en plastique.

Parmis ces 3 fils, on trouve un fil blanc, jaune et rouge.

*   Le contact du fil blanc (masse) et jaune permettent de faire l&rsquo;autofocus.
*   Le contact  du fil blanc (masse) et du fil rouge permettent de déclencher la capture.

### Schémas de montage

Réalisés sous Fritzing &#8211; <http://fritzing.org>

*   2 optocoupleurs pour contrôler le mécanisme de focus et de shoot (et d&rsquo;isoler l&rsquo;appareil photo du reste du circuit) ;
*   1 capteur ultrasons permettant de calculer la distance d&rsquo;un obstacle (30° d&rsquo;ouverture) ;
*   1 servomoteur permettant au capteur ultrasons de balayer un champ plus large (180°) ;
*   4 afficheurs 7 segments permettant de compter le nombre de photos prises.

[<img class="aligncenter size-medium wp-image-327" title="PhotoCatchV1_schema" src="http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/PhotoCatchV1_bb-300x287.png" alt="" width="300" height="287" />][2][<img class="aligncenter size-medium wp-image-326" title="PhotoCatch_wire" src="http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/PhotoCatchV1_schem-300x168.png" alt="" width="300" height="168" />][3] 
### Code arduino

Le code est disponible dans son intégralité sur **GitHub** : <a href="https://github.com/2xyo/fablab/tree/master/photocatch " target="_blank">https://github.com/2xyo/fablab/blob/master/photocatch/src/photocatch.ino</a> et sous **&laquo;&nbsp;THE BEER-WARE LICENSE&nbsp;&raquo;** <img src="http://blog.quentinrousseau.fr/wp-includes/images/smilies/icon_wink.gif" alt=";)" class="wp-smiley" /> 

```c
/*
||
|| @author Yohann Lepage
|| @author Quentin Rousseau
|| @version 0.2
||
|| @description
|| PhotoCatch prend automatiquement une photo lorsque
|| quelqu'un passe devant l'appareil grace à son capteur
|| à ultra-son
||
*/

#include <Servo.h>
#include <SoftwareSerial.h>
#define DEBUG true

// Librairies utilisées
// http://arduino.cc/en/Tutorial/Sweep
// http://arduino.cc/en/Tutorial/Ping

//7 Segments
int rxSegPin =  0;
int txSegPin  = 3;
int photosCounter = 0;
SoftwareSerial segSerial = SoftwareSerial(rxSegPin, txSegPin);

// Ultra Son
// Pin Ultra son
int pingPin = 9;
int val = 0;
int ultrasoundValue = 0;
int timecount = 0; // Echo counter

// Appareil Photo
// Pin Focus
int focusPin = 5;
// Pin Shoot
int shootPin = 6;
// Durée du focus
int focusTime = 0;

// Distance pour le shoot
int shoot_threshold = 100;

// Servo Moteur
Servo myservo;
// Pin Servo
int servoPin = 10;
// Position du Servo Moteur 0 - 180° 
int pos = 0;

// Démarrage de l'Arduino
void setup()
{  
    //Serial pour mode DEBUG
    if(DEBUG)
      Serial.begin(9600);    
    // Attachement du servo au servoPin 
    myservo.attach(servoPin);
    // Passage en mode Output pour l'ultra son
    pinMode(pingPin, OUTPUT);
    // Passage en Output pour le focus
    pinMode(focusPin, OUTPUT);
    // Passage en Output pour le Shoot
    pinMode(shootPin, OUTPUT);
    // Passage en low des focus et shoot
    digitalWrite(focusPin, LOW);
    digitalWrite(shootPin, LOW);
    //7 Segments
    segSerial.begin(9600);
    pinMode(rxSegPin, INPUT);
    pinMode(txSegPin, OUTPUT);
    
    segSerial.print("vv");
    //Turn Colon Off
    segSerial.print('4d',HEX);
    segSerial.print('00',HEX);
}

// Démarrage de la boucle principale
void loop()
{
  // Appel à la méthode de balayage grace au servo
    sweep();
}

// Détection d'un objet
void sonar()
{
   // establish variables for duration of the ping, 
   // and the distance result in inches and centimeters:
   long duration, inches, cm;

   // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
   // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(5);
   digitalWrite(pingPin, LOW);

   // The same pin is used to read the signal from the PING))): a HIGH
   // pulse whose duration is the time (in microseconds) from the sending
   // of the ping to the reception of its echo off of an object.
   pinMode(pingPin, INPUT);
   duration = pulseIn(pingPin, HIGH);
   
   Serial.print(microsecondsToCentimeters(duration));
   Serial.print(" cm\n");
   
   if(microsecondsToCentimeters(duration) <= shoot_threshold)
   {
     shoot();
   } 
   
   delay(150);
}
// Balayage avec le Servo
void sweep()
{
    for(pos = 0; pos < 90; pos += 1) // goes from 0 degrees to 180 degrees
    
    { // in steps of 1 degree
        myservo.write(pos); // tell servo to go to position in variable 'pos'
        //delay(15); // waits 15ms for the servo to reach the position
        sonar();
    }
    
    for(pos = 90; pos >=1; pos-=1) // goes from 180 degrees to 0 degrees
    
    {
        myservo.write(pos); // tell servo to go to position in variable 'pos'
        //delay(15); // waits 15ms for the servo to reach the position
        sonar();
    }
}

long microsecondsToCentimeters(long microseconds)
{
   // The speed of sound is 340 m/s or 29 microseconds per centimeter.
   // The ping travels out and back, so to find the distance of the
   // object we take half of the distance travelled.
   return microseconds / 29 / 2;
}

//Display Photos Counter on the 7 Segments Display
void displaySeg()
{
  photosCounter = photosCounter +1 ;
  
  if(photosCounter < 10) 
  {
    segSerial.print("   ");
    segSerial.print(photosCounter);
  } 
  else if(photosCounter < 100) 
  {
    segSerial.print("  ");
    segSerial.print(photosCounter);
  } 
  else if(photosCounter < 1000) 
  {
    segSerial.print(" ");
    segSerial.print(photosCounter);
  } 
  else 
  {
    segSerial.print(photosCounter);
  } 
  
  Serial.print("Compteur photos : ");
  Serial.print(photosCounter);
  Serial.print("\n");
}

// Capture d'une photo
void shoot()
{
    // Focus
    digitalWrite(focusPin, HIGH);
    delay(focusTime);
    
    // Déclenchement de la photo 
    digitalWrite(shootPin, HIGH);
    delay(200);
    
    displaySeg();
    
    //  Remise à 0 des Pins
    digitalWrite(focusPin, LOW);
    digitalWrite(shootPin, LOW);
}

```

### Démonstration par mon collègue Yohann Lepage (<a href="https://twitter.com/#!/2xyo" target="_blank">@2xyo</a>)

<center>
</center>

### Bonus &#8211; Timelapse de l&rsquo;explor&rsquo;Camp par PhotoCatch :

<center>
</center>

### Evolution possible

*   <span style="font-family: 'mceinline';">Utiliser <strong>&laquo;&nbsp;Picture Transfert Protocol&nbsp;&raquo;</strong> qui permet de contrôler beaucoup plus de paramètres tels que l&rsquo;ouverture de l&rsquo;objectif, la vitesse et même la récupération des photos. Tout cela par contrôle USB.</span>



## En savoir plus&#8230;

*   <a href="http://arduino.cc/en/Tutorial/Ping" title="Arduino - Ping" rel="nofollow">Arduino - Ping</a> ![][4]
*   <a href="http://arduino.cc/en/Tutorial/Sweep" title="Arduino - Sweep" rel="nofollow">Arduino - Sweep</a> ![][4]
*   <a href="http://libptp.sourceforge.net/" title="libptp2 Project Page" rel="nofollow">libptp2 Project Page</a> ![][4]

 [1]: http://cgi.ebay.fr/TELECOMMANDE-filaire-1m-pour-NIKON-D90-D3100-D5000-MC-DC2-/190620347929?pt=FR_T%C3%A9l%C3%A9commandes_d%C3%A9clencheurs&hash=item2c61dbae19
 [2]: http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/PhotoCatchV1_bb.png
 [3]: http://blog.quentinrousseau.fr/wp-content/uploads/2012/01/PhotoCatchV1_schem.png
 [4]: http://blog.quentinrousseau.fr/wp-content/plugins/netblog/images/external-link-ltr-icon.png