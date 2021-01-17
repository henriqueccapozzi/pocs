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

LOOPBACK_INTERFACE = "Loopback9876"
create_loopback = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{}</name>
            <description>python netconf created interface</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                ianaift:softwareLoopback
            </type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>9.8.7.6</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
""".format(LOOPBACK_INTERFACE)

iosxe_create_loopback = iosxe_manager.edit_config(
    target="running", config=create_loopback)
print("Result os creation", iosxe_create_loopback.ok)
print("*"*60)
interface_filter = """
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{}</name>
        </interface>
    </interfaces>
</filter>
""".format(LOOPBACK_INTERFACE)

lp = iosxe_manager.get_config("running", interface_filter)

print("Result os lp", lp.ok)
print(lp.xml)
print("*"*60)
delete_loopback = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
                <name>{}</name>
        </interface>
    </interfaces>
</config>
""".format(LOOPBACK_INTERFACE)

iosxe_delete_loopback = iosxe_manager.edit_config(
    target="running", config=delete_loopback)

print("Result os lp", iosxe_delete_loopback.ok)
print(iosxe_delete_loopback.xml)
print("*"*60)
lp = iosxe_manager.get_config("running", interface_filter)

print("Result os lp", lp.ok)
print(lp.xml)
iosxe_manager.close_session()
