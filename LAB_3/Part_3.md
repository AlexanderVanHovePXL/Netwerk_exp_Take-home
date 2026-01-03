## Part 3: Python Network automation with NETMIKO

### 1. Task Preparation and Implementation

**Voorbereiding:**
- de voorbeeld python script downloaden in openen in visual studio code: 
    - https://github.com/wlepxl/Network-Programmability_Basics/blob/master/programming_fundamentals/python_part_3/api_netmiko_example.py
- de IP adres van de virtuele router.

**Implementatie:**
- Open visual studio code en maak een folder voor de file api_netmiko_example.py
- In deze file heb ik dan de host, port, user en password verandert waardoor je meteen kan verbinden aan de server.
- aangezien we onze essentials hebben ingevuld kunnen we nu de commando's ingeven dat we kunnen doorsturen
- Script uitgevoerd om verbinding te maken met het IOS-XE VM. 
- Show-commando’s toegevoegd zoals `show ip interface brief` en `show run int Gig1`. 
- Output geprint via `pprint()` en opgeslagen in een extern `.txt` bestand. 
- Script uitgebreid met: - Configuratiecommando’s via `send_config_set`.

### 2. Task Troubleshooting

**Problemen:**
1. Bij elke oefening was er een leer curve dat ik moest volgen en opzoeken.

**Oplossingen:**
1. Dingen uitgeproberen en als dat niet lukt, opzoeken en uitvoeren.

### 3. Task Verification

**testmethoden:**

- Vooral kijken naar de output, aangezien je exact dezelfde output zou krijgen als op de echte router.
- Op de router zelf kijken of de veranderingen zijn uitgevoerd.