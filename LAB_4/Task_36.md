## Task 38: End-To-End automatisering -> RESTCONF (python)

### 1. Task Preparation and Implementation

**Voorbereiding:**
- Maak de xml files aan voor je juiste configuratie door te sturen naar de router.
    - Zorg dat deze xml file op github staat.
- Maak een .venv file door de commando: `python -m venv .venv`
    - ik raad aan voor daarna dependencies te installeren via deze commando: `pip install requests ncclient`


**Implementatie:**
- Een python script gemaakt genaamd: `netconf_script.py`
    - Dit script voert de verschillende configuratie uitvoeren.
    - Ook een try catch in het script voor exceptionhandling.


### 2. Task Troubleshooting

**Problemen:**
1. ik wist niet hoe de structuur van de xml moest gevormd worden voor de juiste configuratie.
2. de OSPF wou niet meteen werken.


**Oplossingen:**
1. Door een get request te doen naar: `https://192.168.0.122/restconf/data/Cisco-IOS-XE-native:native` had ik de juiste structuur gevonden voor te gebruiken in mijn body request.
2. Ik had het moeten opzoeken, hoe ik ospf kon laten werken en het duurden vrij lang, maar ik heb deze website gevonden die veel helpte: `https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/179/b_179_programmability_cg/m_179_prog_yang_netconf.html`

### 3. Task Verification

**testmethoden:**

- Voor de hostname
    - Kijk in de terminal voor de nieuwe hostname.
- Interfaces bekijken:
    - met de commando: `show ip interface brief` krijg je alle interfaces te zien of de Loopback is aangemaakt.
- OSPF bekijken
    - Met de commando: `show ip ospf interface brief`