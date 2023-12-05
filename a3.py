
from netmiko import ConnectHandler

# Router details
router = {
    'Router': 'R1',
    'ip': '192.168.1.1',  # Replace with your router's IP address
    'username': 'cisco',
    'password': 'cisco123',
    'secret': 'cisco1234',
}

# Establish SSH connection to the router
net_connect = ConnectHandler(**router)
net_connect.enable()

# Configure loopback interface
loopback_config = [
    'interface loopback0',
    'ip address 1.1.1.1 255.255.255.255',
    'exit',
]

net_connect.send_config_set(loopback_config)

# Configure GigabitEthernet0/0
interface_config = [
    'interface GigabitEthernet0/0',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
    'exit',
]

net_connect.send_config_set(interface_config)

# Configure OSPF
ospf_config = [
    'router ospf 1',
    'network 1.1.1.1 0.0.0.0 area 0',
    'network 192.168.2.0 0.0.0.255 area 0',
    'exit',
]

net_connect.send_config_set(ospf_config)

# Save the configuration
net_connect.save_config()

# Disconnect from the router
net_connect.disconnect()