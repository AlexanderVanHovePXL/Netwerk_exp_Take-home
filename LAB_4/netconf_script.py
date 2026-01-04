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
try:
    # hostname
    url = "https://raw.githubusercontent.com/AlexanderVanHovePXL/Netwerk_exp_Take-home/refs/heads/main/LAB_4/configs/netconf_hostname.xml"
    response = requests.get(url)

    if response.status_code == 200:
        hostname_config_xml = response.text
    else:
        print("github is wrong!!!")
        exit(0)

    # interface loopback
    url = "https://raw.githubusercontent.com/AlexanderVanHovePXL/Netwerk_exp_Take-home/refs/heads/main/LAB_4/configs/netconf_Loopback.xml"
    response = requests.get(url)
    if response.status_code == 200:
        loopback_config_xml = response.text
    else:
        print("github is wrong!!!")
        exit(0)

    # ospf
    url = "https://raw.githubusercontent.com/AlexanderVanHovePXL/Netwerk_exp_Take-home/refs/heads/main/LAB_4/configs/netconf_ospf.xml"
    response = requests.get(url)
    if response.status_code == 200:
        ospf_config_xml = response.text
    else:
        print("github is wrong!!!")
        exit(0)

    reply1 = m.edit_config(target="running", config=hostname_config_xml)
    print("Hostname response:")
    print(xml.dom.minidom.parseString(reply1.xml).toprettyxml())

    # Apply Loopback1
    reply2 = m.edit_config(target="running", config=loopback_config_xml)
    print("Loopback1 response:")
    print(xml.dom.minidom.parseString(reply2.xml).toprettyxml())

    # Apply OSPF
    reply3 = m.edit_config(target="running", config=ospf_config_xml)
    print("OSPF response:")
    print(xml.dom.minidom.parseString(reply3.xml).toprettyxml())
except Exception as e:
    print("Fout tijdens configuratie: ", e)
