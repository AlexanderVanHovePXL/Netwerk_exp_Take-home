## Part 4: Explore YANG Models

### 1. Task Preparation and Implementation

**Voorbereiding:**
- een folder maken genaamd devnet-src en visual studio in die map openen.
- een kopie maken van de `ietf-interfaces.yang` maken en een folder maken pyang waar deze file in komt te staan.
    [Github](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1693/ietf-interfaces.yang)
- pyang installeren of updaten: `pip install pyang --upgrade`.
- Wat je ook kan doen(en heb ik persoonlijk gedaan) is een .venv file gemaakt in de directory en daar alles pyang op geinstalleerd.

**Implementatie:**
- door het commando `pyang -f tree ietf-interfaces.yang` krijg je te zien dat de `leaf enabled` veel makkelijker te zien is

### 2. Task Troubleshooting

**Problemen:**
1. Als ik pyang installeerden via pip in mijn terminal, ging het niet. naar het PATH dus dan kon ik die niet gebruiken tenzij ik het hele pad opgaf.

**Oplossingen:**
1. een .venv file met een profile erin die je kan activeren en dan heb je een omgeving waar je pyang wel kan installeren zonder PATH problemen.

### 3. Task Verification

**testmethoden:**

- Kijken of pyang geinstalleerd is kun je doen door het commando: `pyang -v`.
- Het gegeven commando uitvoeren en zien of je dezelfde output krijgt.