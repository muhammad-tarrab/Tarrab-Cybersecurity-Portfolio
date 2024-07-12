import time
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

# Initialize a counter for packet indexing
packet_counter = 0

# This function is called for each packet captured
def packet_callback(packet):
    global packet_counter
    packet_counter += 1
    
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        
        # Initialize an empty list to store the packet information
        packet_info = [f"Packet #{packet_counter}"]  # Add packet index
        
        # Add source and destination IP addresses
        packet_info.append(f"Source IP: {ip_layer.src}")
        packet_info.append(f"Destination IP: {ip_layer.dst}")
        
        # Check if the packet has a TCP layer
        if TCP in packet:
            tcp_layer = packet[TCP]
            packet_info.append("Protocol: TCP")
            packet_info.append(f"Source Port: {tcp_layer.sport}")
            packet_info.append(f"Destination Port: {tcp_layer.dport}")
        
        # Check if the packet has a UDP layer
        elif UDP in packet:
            udp_layer = packet[UDP]
            packet_info.append("Protocol: UDP")
            packet_info.append(f"Source Port: {udp_layer.sport}")
            packet_info.append(f"Destination Port: {udp_layer.dport}")
        
        # Check if the packet has an ICMP layer
        elif ICMP in packet:
            packet_info.append("Protocol: ICMP")
        
        # Check if the packet has a Raw layer (payload data)
        if Raw in packet:
            packet_info.append(f"Payload: {packet[Raw].load}")
        
        # Print the packet information with a separator
        print("\n".join(packet_info))
        print("-" * 50)  # Separator line
        
        # Delay to slow down the output
        time.sleep(1)

# This function prints a disclaimer
def disclaimer():
    print("This tool is for educational purposes only. Unauthorized use is prohibited.")

# Print the disclaimer
disclaimer()

# Start capturing packets and call packet_callback for each packet captured
sniff(prn=packet_callback, count=0)
