#! /usr/bin/env python

from scapy.all import *

for i in range(0, 10):
    send(IP(dst='172.17.0.2', 
    )/ICMP())    
        
    print("sent packet")

