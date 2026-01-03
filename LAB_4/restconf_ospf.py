import requests

# GitHub RAW URL naar jouw JSON-configuratie
url_github = "https://raw.githubusercontent.com/AlexanderVanHovePXL/Netwerk_exp_Take-home/refs/heads/main/configs/restconf.json"

# RESTCONF device info
device_ip = "192.168.0.122"
username = "cisco"
password = "cisco123!"

# RESTCONF URL voor Cisco IOS-XE native config
restconf_url = f"https://{device_ip}/restconf/data/Cisco-IOS-XE-native:native"

# RESTCONF headers
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

# 1. Config ophalen uit GitHub
response = requests.get(url_github)
config_json = response.json()

# 2. Config toepassen via RESTCONF (PUT = idempotent)
resp = requests.put(
    restconf_url,
    auth=(username, password),
    headers=headers,
    json=config_json,
    verify=False
)

# 3. Resultaat tonen
print("Status code:", resp.status_code)
print("Response:")
print(resp.text)
