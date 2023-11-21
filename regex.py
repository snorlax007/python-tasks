from scapy.all import rdpcap

# Path to the PCAP file
pcap_file_path = "C:/Users/Lenovo/Desktop/chatbot/sample_traffic.pcap"

# Output text file
output_text_file = "output.txt"

# Read packets from the PCAP file
packets = rdpcap(pcap_file_path)

# Open the output text file for writing
with open(output_text_file, "w") as output_file:
    # Iterate over each packet and write information to the text file
    for packet_num, packet in enumerate(packets, 1):
        # Write packet number
        output_file.write(f"Packet {packet_num}:\n")

        # Write all information about the packet
        output_file.write(str(packet.show(dump=True)))

        # Add a separator between packets for better readability
        output_file.write("\n" + "=" * 50 + "\n")

print(f"Packet information has been stored in {output_text_file}")
