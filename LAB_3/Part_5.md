## Part 5: Use NETCONF to Access an IOS XE Device

### 1. Task Preparation and Implementation

**Voorbereiding:**

- Check via het commando: `show ip interface brief` nogeens of het IP niet verandert is.
- Ping de router voor zeker te zijn dat alles goed werkt
- Zet een terminal klaar die met SSH verbonden is aan de router.

**Implementatie:**

- gebruik de gegeven commando: `show platform software yang-management process`
    - kijk of ncsshd aan staat.
- Bij mij stond het nog niet aan, waardoor ik de commando `netconf-yang` moest doen.
- Het script wat aanpassen per oefening zoals aangegeven in het document 


### 2. Task Troubleshooting

**Problemen:**
1. Ik kon in de terminal de xml lijnen niet gewoon pasten en dat die iets terug stuurden.

**Oplossingen:**
1. via python het als script schrijven en doorsturen, stuurt wel de juiste xnml door en de juiste response terug

### 3. Task Verification

**testmethoden:**

- Bij de loopback maken kan je in je terminal van de router het commando: `show ip interface brief` meegeven om te zien op je nu wel een Loopback1 hebt.
