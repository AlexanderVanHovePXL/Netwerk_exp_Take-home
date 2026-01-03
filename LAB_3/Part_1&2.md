### 1. Task Preparation and Implementation

**Voorbereiding:**
- VirtualBox gedownload.
- CSR1000v VM-bestand en ISO gedownload.

**Implementatie:**
- VirtualBox geïnstalleerd.
- In VirtualBox gekozen voor het importeren van de ova file voor virtualBox.
- DEVASC VM geselecteerd en geïmporteerd.
- het netwerk van de VM naar bridged zetten:
    - selecteer de VM -> ga naar instellingen -> ga naar Netwerk -> op adapter 1 bij "attached to" moet je als bridged aanduiden.
- VM gestart en router-omgeving laten opstarten.
- De ISO selecteren als optische stations en dan opnieuw opgestart.
- Op het scherm van de boot manager, de `package.conf` aanduiden.


### 2. Task Troubleshooting

**Problemen:**
1. Wanneer voor het eerste opstarten, niet meteen in het router ISO geladen.
2. De router heeft geen Ip gegeven aan GigabitEthernet1
3. Bij een connectie maken via ssh, support die bijhorende KeyAlgoritmes niet meer dat de router gebruikt.
4. een error gekregen van ssh: `no matching host key type found`

**Oplossingen:**
1. Naar apparaten -> optische stations -> IDE (IDE primary device 1 )
    a. de ISO selecteren
    b. Als je nogeens gaat kijken, zou je normaal een vinkje moeten zien dat het geselecteerd is en een reboot doen
2. Een restart op de algemene machine en dan de VM terug opstarten en dat heeft het probleem opgelost.
3 & 4.  in de .ssh van mijn computer een file genaamd config neergezet die bij deze specefieke IP dat algoritme en Host key gebruikt:
       ```
        Host 192.168.0.122
            KexAlgorithms +diffie-hellman-group14-sha1
            HostKeyalgorithms +ssh-rsa
            ```

### 3. Task Verification

**testmethoden:**

- Wanneer je de terminal ziet:
    - `ena` in typen voor de juiste privilege te hebben.
    - Het commando `show ip interface brief`.
    - Er is een lokaal Ip address gegeven dat door de DHCP van de router is gegeven.
- Ping via jou machine naar de virtual router.
- een ssh verbinding maken met de virtuele router met als gebruiker cisco
