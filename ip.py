import re
import ipaddress

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

classless = "((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)/(3[0-2]|[1-2]?[0-9])"


def test(ip):
    result=re.search(classless,ip)
    if result:
        print("Valid IP address")
    else:
        print("Invalid IP address")

def calculate_addresses(ip):
     #create ip network object
     network = ipaddress.ip_network(ip, strict=False)
     # Network address (subnet address)
     network_address = network.network_address
     print(network_address)
     # Broadcast address
     broadcast_address = network.broadcast_address
     print(broadcast_address)
     # Subnet mask
     subnet_mask = network.netmask
     print(subnet_mask)

ip="192.168.2.100/24"
test(ip)
calculate_addresses(ip)

