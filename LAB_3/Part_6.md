## Part 5: Use NETCONF to Access an IOS XE Device

### 1. Task Preparation and Implementation

**Voorbereiding:**

- Postman installeren of via de DEVSEC VM postman openen en klaar maken voor gebruik.
- Zorg dat je de juiste processen aan hebt staan voor deze lab.
    - Dit kan je zien door het commando: `show platform software yang-management process`.
    -  Als dat niet zo is moet de in de terminal van je router de commando: `restconf` doen
    - Voor de https(NGINX) server en authenticatie van de api aan te zetten, moet je in de terminal de commando's: `ip http secure-server` en `ip http authentication local`
- Ping de router voor zeker te zijn dat die aan staat en bereikbaar is.

**Implementatie:**

- In postman een GET request aanmaken met als als enpoint `https://192.168.0.122/restconf`
    - Je moet bij de authorization tab het aanpassen naar basic auth en de ssh user en passwoord meegeven.
    - In de settings van de request moet je checken dat je voor de zekerheid `SSL certificate verification` af hebt staan.
    - Als je json wilt sturen en ontvangen in plaats van xml(wat standaard is), dan moet je in de header key `Content-Type` en `Accept` neer zetten met als beide values: `application/yang-data+json`.
        - Je kan ook de value `application/yang-data+xml` gebruiken als je liever xml terug krijgt.
- Voor alle interfaces te bekijken kun je als endpoint: `https://192.168.0.122/restconf/data/ietf-interfaces:interfaces` geven.
    - Als je een specifieke interface wilt meegeven moet je de laatste endpoint nemen en erachter: `interface=GigabitEthernet1` neerschrijven.
    - wanneer je een specifieke interface bekijkt ga je zien dat die geen Ipv4 adress aangeeft. De reden hiervoor is omdat de IP via de DHCP server gegeven word.
    - Als je in de terminal handmatig een IP adres meegreeft krijg je die wel te zien.

- Als je een Loopback1 wilt maken als interface. Moet je zoals de vorige endpoint, de naam van de interface meegeven.
    -Bijvoorbeeld: `interface=Loopback1`
    - Verander de request type naar PUT en voeg een body toe.
        -Voor de body kun je de GET request output copy-pasten en de bepaalde aanpassingen maken.


### 2. Task Troubleshooting

**Problemen:**
1. ik probeerde de endpoint te gebruiken voor een specefieke interface te bekijken en ik kreeg een `404 Not Found`.
2. Tijdens het uittesten van het script in python kreeg ik een error dat die de module requests niet kon vinden.
3. Ik kreeg een error dat mijn authenticatie niet werkten.


**Oplossingen:**
1. Blijkbaar zijn de endpoints hoofdletter gevoelig. Dus ik had `gigabitEthernet1` geschreven zonder hoofdletter in het begin waardoor die de interface niet kon vinden.
2. Voor de module requests te kunnen gebruiken moet je het volgende commando doen: `pip install requests`.
3. Voor authenticatie te laten werken moet je de ronde haakjes gebruiken `()` in plaats van de brackets `{}`, anders ga je errors hebben.

### 3. Task Verification

**testmethoden:**

- Als je de request doorstuurt via postman of python krijg je altijd een request terug waar staat of het Ok, NOT FOUND, etc is. Naast de OK of CREATED response krijg je bij een GET request de json/xml body die laat zien wat er verandert is.
 