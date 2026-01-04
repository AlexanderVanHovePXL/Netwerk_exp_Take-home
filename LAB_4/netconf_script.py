from ncclient import manager
import requests

import xml.dom.minidom
m = manager.connect(
     host="192.168.0.122",
       port=830,
         username="cisco",
           password="cisco123!", 
           hostkey_verify=False 

)
# hostname
url = ""
response = requests.get(url)
reply1 = m.edit_config(target="running", config=netconf_hostname)
print("Hostname response:")
print(xml.dom.minidom.parseString(reply1.xml).toprettyxml())

# Apply Loopback1
reply2 = m.edit_config(target="running", config=netconf_interface)
print("Loopback1 response:")
print(xml.dom.minidom.parseString(reply2.xml).toprettyxml())

# Apply OSPF
reply3 = m.edit_config(target="running", config=netconf_ospf)
print("OSPF response:")
print(xml.dom.minidom.parseString(reply3.xml).toprettyxml())
