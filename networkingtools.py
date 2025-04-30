# Demonstrate the use of networking tools like ping, ipconfig, netstat and traceroute

import os
import platform
import subprocess
import time

# Function to simulate 'ping' command
def simulate_ping():
    print("\nSimulating the 'ping' command...")
    target = "google.com"
    
    # Depending on the OS, the ping command varies (Windows uses 'ping -n', Linux uses 'ping -c')
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", target]  # Ping google.com 4 times (Windows)
    else:
        command = ["ping", "-c", "4", target]  # Ping google.com 4 times (Linux/macOS)

    try:
        # Running the command and capturing the output
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing ping: {e}")

# Function to simulate 'ipconfig' command (Displays network configuration)
def simulate_ipconfig():
    print("\nSimulating the 'ipconfig' command...")
    
    # Depending on the OS, 'ipconfig' is used on Windows, and 'ifconfig' or 'ip a' is used on Linux/macOS
    if platform.system().lower() == "windows":
        command = ["ipconfig"]
    else:
        command = ["ifconfig"] if platform.system().lower() != "darwin" else ["ip", "a"]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing ipconfig/ifconfig: {e}")

# Function to simulate 'netstat' command (Displays network connections, routing tables)
def simulate_netstat():
    print("\nSimulating the 'netstat' command...")
    
    # Netstat command (both Windows and Linux/macOS use the same command)
    command = ["netstat", "-an"]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing netstat: {e}")

# Function to simulate 'traceroute' command (Traces the route packets take to a network host)
def simulate_traceroute():
    print("\nSimulating the 'traceroute' command...")
    target = "google.com"
    
    # Depending on the OS, 'traceroute' (Linux/macOS) or 'tracert' (Windows)
    if platform.system().lower() == "windows":
        command = ["tracert", target]
    else:
        command = ["traceroute", target]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error executing traceroute: {e}")

# Main function to run the simulations of networking tools
def run_network_tools_simulation():
    print("Welcome to the Networking Tools Simulation!\n")
    
    # Simulate each network tool one by one
    simulate_ping()
    time.sleep(1)  # Wait for 1 second between simulations
    simulate_ipconfig()
    time.sleep(1)
    simulate_netstat()
    time.sleep(1)
    simulate_traceroute()

if __name__ == "__main__":
    run_network_tools_simulation()
