#! /usr/bin/env python

from netfilterqueue import NetfilterQueue as nfq
from scapy.all import*

def packet_listener(packet):
    #sacpy_packet = IP(packet.get_payload())
    print(packet);
    packet.add-payload()
    #print(scapy_packet.show())
    packet.accept()

queue = nfq()
queue.bind(1, packet_listener)
queue.run();

