# Demonstrate the network monitoring of the internet traffic through any predefined tool

#!/bin/bash

# Step 1: Update system and install necessary network monitoring tools
echo "Updating and upgrading system..."
sudo apt update -y
sudo apt upgrade -y

echo "Installing network monitoring tools: Wireshark, iftop, nload..."
sudo apt install wireshark iftop nload -y

# Step 2: Start monitoring with 'iftop' (Real-time traffic monitoring)
echo "Starting real-time traffic monitoring with iftop..."
# Display real-time network traffic (top 10 connections, filter by bandwidth usage)
sudo iftop -ni eth0

# To start it in background:
# sudo iftop -ni eth0 &

# Step 3: Start monitoring with 'nload' (Bandwidth monitoring tool)
echo "Starting bandwidth monitoring with nload..."
# Real-time bandwidth usage monitoring (view in graphical format for input and output)
sudo nload -t 1000

# To start it in background:
# sudo nload -t 1000 &

# Step 4: Start monitoring with 'Wireshark' (Packet sniffing and inspection)
echo "Starting Wireshark for deep packet inspection..."
# Start Wireshark in GUI mode (runs interactively)
# sudo wireshark &

# Alternatively, for non-GUI (Terminal based):
echo "Starting Tshark (Wireshark CLI tool for packet capture)..."
# Start Tshark (Wireshark's CLI version)
sudo tshark -i eth0

# Step 5: Display network interfaces for monitoring
echo "Displaying network interfaces..."
ifconfig

# Step 6: Display active network connections using 'netstat'
echo "Displaying active network connections using netstat..."
netstat -tuln

# Step 7: Test network connectivity with ping
echo "Testing network connectivity (ping) to a website (e.g., google.com)..."
ping -c 4 google.com

# Step 8: Optional - Network Traffic Analysis (using NetFlow with ntopng)
echo "Setting up NetFlow traffic analysis tool ntopng..."
# Install ntopng
sudo apt install ntopng -y
# Start ntopng for network traffic visualization (access via browser at http://localhost:3000)
sudo systemctl start ntopng

# Step 9: End of script
echo "Network monitoring setup is complete."
echo "Use the following commands for real-time monitoring:"
echo "1. 'iftop' - To monitor active connections and bandwidth usage."
echo "2. 'nload' - To monitor bandwidth in and out."
echo "3. 'wireshark' - To monitor network packets (GUI version)."
echo "4. 'tshark' - CLI version of Wireshark for packet sniffing."
echo "5. 'netstat' - To display all active network connections."
echo "6. 'ping google.com' - To test network connectivity."

# End of script
