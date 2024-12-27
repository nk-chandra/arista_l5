import yaml
config = """
leaf1-DC1:
  interfaces:
    loopback0: 
      ipv4: 192.168.101.11
      mask: 32
    loopback1: 
      ipv4: 192.168.102.11
      mask: 32
    Ethernet3:
      ipv4: 192.168.103.0
      mask: 31
    Ethernet4: 
      ipv4: 192.168.103.2
      mask: 31
    Ethernet5: 
      ipv4: 192.168.103.4
      mask: 31
"""
switches = yaml.safe_load(config)
for iface in switches['leaf1-DC1']['interfaces']:
#Iterate through all interfaces using iface variable as the incrementing index
    print("interface %s"  % iface)
#Pull variables into easier to use variables
    ip = switches['leaf1-DC1']['interfaces'][iface]['ipv4']
    mask = switches['leaf1-DC1']['interfaces'][iface]['mask']
    print(" ip address %s/%s" % (ip, mask))

