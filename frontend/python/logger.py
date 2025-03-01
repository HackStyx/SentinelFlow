import sys
from scapy.all import sniff, get_if_addr, conf
import json


def show_packet(packet):
    try:
        # Get a clean string representation of the packet
        packet_str = packet.show(dump=True)
        
        # Ensure the output is properly encoded
        if isinstance(packet_str, bytes):
            packet_str = packet_str.decode('utf-8', errors='ignore')
        
        # Clean up the string to remove any problematic characters
        packet_str = ''.join(char for char in packet_str if ord(char) >= 32 or char in '\n\r\t')
        
        print(packet_str, flush=True)
    except Exception as e:
        print(json.dumps({"error": str(e)}), flush=True)


# Get your local IP address (assumes single interface, adjust if needed)
default_iface = conf.iface  # Auto-detect active interface
my_ip = get_if_addr(default_iface)  # Get your machine's IP on that interface

# Construct filter string to capture only incoming traffic
print(my_ip)
# filter_str = (
#     "(tcp) and ("
#     "dst port 3306 or dst port 5432 or dst port 6379 or dst port 27017 or dst port 8080 or dst port 443"
#     ") and ("
#     f"dst host {my_ip}"  # Only capture packets where your machine is the destination
#     ")"
# )
filter_str = sys.argv[1]
# filter_str += f" and (dst host {my_ip})"
print(filter_str)
# count = 0
#
#
# # Callback function to increment and display count
# def count_packets(pkt):
#     global count
#     count += 1
#     print(
#         f"Packets captured: {count}", end="\r", flush=True
#     )  # Overwrites the same line
#

# Start sniffing
try:
    sniff(filter=filter_str, prn=show_packet, store=0)
except Exception as e:
    print(json.dumps({"error": str(e)}), flush=True)
