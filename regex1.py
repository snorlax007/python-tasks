import re
from scapy.all import *
import os
from scapy.layers.inet import TCP

def filter_tcp_pcap(input_file,output_file):
    # Regex patterns for filtering
    protocol="TCP|UDP|ICMP"
    ip_pattern = r"192\.168\.68\.101"
    dest_port_pattern = r"\b443\b"
    src_port_pattern = r"\b50819\b"

    # Read the pcap file
    packets = rdpcap(input_file)
    filtered_packets = []

    # Loop through each packet in the pcap file
    for packet in packets:
        # Check if the packet is a TCP packet
        if TCP in packet:
            # Convert packet to string
            packet_str = repr(packet)

            # Check for the presence of the specified patterns using regex
            if (re.search(protocol, packet_str) and re.search(ip_pattern, packet_str) and
                (re.search(dest_port_pattern, packet_str) or
                 re.search(src_port_pattern, packet_str))):

                        filtered_packets.append(packet_str)

                        # Write the filtered packets to the output file
            with open(output_file, "w") as output_txt:
                output_txt.write("\n".join(filtered_packets))


                # Print the packet to the console
                

if __name__ == "__main__":
    # Replace 'input.pcap' with the path to your pcap file.
    pcap_file = os.path.join(os.getcwd(), 'sample_traffic.pcap')
    result=os.path.join(os.getcwd(), 'r3.txt')
    filter_tcp_pcap(pcap_file,result)