# Introduction: Network address translation, Subnet Masking, Difference between Intranet andInternet, Working of Internet, Dynamic and Static Routing, Domain Name Server , networkingtools - ipconfig, ping, netstat, traceroute

import socket
import os
import subprocess
import platform
import time

# Simulating 'ipconfig' command (network configuration)
def ipconfig_simulation():
    if platform.system() == "Windows":
        output = subprocess.check_output("ipconfig", universal_newlines=True)
    else:
        output = subprocess.check_output("ifconfig", universal_newlines=True)
    return output

# Simulating 'ping' command (network reachability check)
def ping_simulation(host="8.8.8.8"):
    try:
        response = subprocess.check_output(["ping", host, "-c", "4"], universal_newlines=True)
        return response
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e}"

# Simulating 'netstat' command (network statistics)
def netstat_simulation():
    output = subprocess.check_output(["netstat", "-an"], universal_newlines=True)
    return output

# Simulating 'traceroute' command (path of network packets)
def traceroute_simulation(host="8.8.8.8"):
    if platform.system() == "Windows":
        output = subprocess.check_output(["tracert", host], universal_newlines=True)
    else:
        output = subprocess.check_output(["traceroute", host], universal_newlines=True)
    return output

# Simulating the NAT (Network Address Translation) process
def nat_simulation():
    nat_result = """
    NAT Translation:
    - Private IP (Local): 192.168.1.2 -> Public IP (Global): 203.0.113.5
    - Private IP (Local): 192.168.1.3 -> Public IP (Global): 203.0.113.5
    """
    return nat_result

# Simulating subnet mask (basic check)
def subnet_mask_simulation():
    subnet_mask = "255.255.255.0"
    ip_address = "192.168.1.10"
    network_part = f"Network Part: {ip_address.split('.')[0]}.{ip_address.split('.')[1]}.{ip_address.split('.')[2]}.0"
    return f"Subnet Mask: {subnet_mask}\n{network_part}"

# Simulating DNS resolution (domain to IP)
def dns_simulation(domain="www.google.com"):
    ip_address = socket.gethostbyname(domain)
    return f"Domain: {domain} -> IP Address: {ip_address}"

# Simulating routing behavior (static vs dynamic)
def routing_simulation():
    static_route = "Static Route: 192.168.1.0/24 -> Gateway: 192.168.0.1"
    dynamic_route = "Dynamic Route: 10.1.0.0/16 via OSPF"
    return f"Routing Information:\n{static_route}\n{dynamic_route}"

# Simulating differences between Intranet and Internet
def intranet_vs_internet():
    explanation = '''
    Intranet: A private network, often internal to a company, that allows employees to share information and resources.
    It is not publicly accessible and often has its own security protocols.

    Internet: A vast network that interconnects millions of private, public, academic, business, and government networks.
    It is a global system that uses standardized protocols to allow for worldwide communication.
    '''
    return explanation

# Simulating the Working of the Internet
def working_of_internet():
    explanation = '''
    The Internet is based on the TCP/IP model, where devices (clients) connect to servers to request data (e.g., websites).
    Routers forward packets of data based on IP addresses, and the DNS (Domain Name System) resolves human-readable
    domain names (e.g., www.example.com) into IP addresses that computers can understand.
    '''
    return explanation

# Simulating Dynamic and Static Routing
def routing_explanation():
    explanation = '''
    Static Routing: Routes are manually configured and remain constant unless changed by a network administrator.
    Dynamic Routing: Routers automatically adjust routing paths based on current network conditions, using protocols
    like RIP, OSPF, or BGP.
    '''
    return explanation

# Simulating DNS functionality (Simplified version)
def dns_explanation():
    explanation = '''
    DNS (Domain Name System) translates domain names like "www.example.com" into IP addresses. DNS servers maintain
    a database of domain names and their corresponding IP addresses, allowing users to access websites using human-friendly
    names instead of numeric IP addresses.
    '''
    return explanation

# Function to simulate all the network tools together
def run_all_simulations():
    print("Running Network Simulations...\n")

    # Run ipconfig/ifconfig simulation
    print("IP Configuration:")
    print(ipconfig_simulation(), "\n")

    # Run ping simulation
    print("Ping Simulation (to 8.8.8.8):")
    print(ping_simulation(), "\n")

    # Run netstat simulation
    print("Network Statistics (Netstat):")
    print(netstat_simulation(), "\n")

    # Run traceroute simulation
    print("Traceroute Simulation (to 8.8.8.8):")
    print(traceroute_simulation(), "\n")

    # Run NAT Simulation
    print("NAT Simulation:")
    print(nat_simulation(), "\n")

    # Run Subnet Mask Simulation
    print("Subnet Mask Simulation:")
    print(subnet_mask_simulation(), "\n")

    # Run DNS Simulation
    print("DNS Simulation (www.google.com):")
    print(dns_simulation(), "\n")

    # Run Routing Simulation
    print("Routing Simulation (Static vs Dynamic):")
    print(routing_simulation(), "\n")

    # Additional explanations
    print("Intranet vs Internet:")
    print(intranet_vs_internet(), "\n")

    print("Working of the Internet:")
    print(working_of_internet(), "\n")

    print("Routing Explanation:")
    print(routing_explanation(), "\n")

    print("DNS Explanation:")
    print(dns_explanation(), "\n")

# Execute all simulations
if __name__ == "__main__":
    run_all_simulations()
