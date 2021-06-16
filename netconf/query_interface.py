#!/usr/bin/env python

from ncclient import manager
import xmltodict
from xml.dom import minidom


iosxeao = {
    'address': 'ios-xe-mgmt.cisco.com',
    'netconf_port': 10000,
    'restconf_port': 9443,
    'username': 'developer',
    'password': 'C1sco12345',
}

iosxe_manager = manager.connect(
    host=iosxeao["address"],
    port=iosxeao["netconf_port"],
    username=iosxeao["username"],
    password=iosxeao["password"],
    hostkey_verify=False
)

INTERFACE_NAME = "GigabitEthernet3"

interface_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{}</name>
        </interface>
    </interfaces>
</filter>
""".format(INTERFACE_NAME)

# Interface config object
interface_config_obj = iosxe_manager.get_config("running", interface_filter)

# Using the builtin python xml lib
interface_xml_config = minidom.parseString(interface_config_obj.xml)
print(interface_xml_config.toprettyxml(indent="  "))

# Using xmltodict - better to work with
response_dict = xmltodict.parse(interface_config_obj.xml)

intf = response_dict['rpc-reply']['data']
print(intf['interfaces']['interface']['name']['#text'])
print(intf['interfaces']['interface']['description'])
print(intf['interfaces']['interface']['enabled'])
print("*"*60)
