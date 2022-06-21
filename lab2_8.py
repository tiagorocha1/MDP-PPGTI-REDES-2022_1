from ncclient import manager
import xml.dom.minidom

def exec():
    m = manager.connect(
        host="192.168.18.47",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    )


   # netconf_reply = m.get_config(source="running")
   #5 print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )

    netconf_filter = """
    <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    </filter>
    """

    netconf_reply = m.get_config(source="running", filter=netconf_filter)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

if __name__ == '__main__':
    exec()