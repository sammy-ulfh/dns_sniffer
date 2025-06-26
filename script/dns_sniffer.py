#!/usr/bin/env python3

import argparse
import scapy.all as scapy
import socket
import os
import sys
from termcolor import colored

# Arguments Menu
def get_arguments():
    argparser = argparse.ArgumentParser(description="DNS Sniffer")
    argparser.add_argument("-i", "--interface", dest="interface", required=True, help="Network Interface Name. (Ex: wlan0)")

    args = argparser.parse_args()

    return args.interface

# Verify privileges and correct inerface
def verify(interface):
    if os.getuid() != 0:
        print(colores("\n[!] Root privileges are required\n", "yellow"))
        sys.exit(1)

    nework_interfaces = [inter[1] for inter in socket.if_nameindex()]

    return True if interface in nework_interfaces else False

# process each packet
def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR): # verify if the packe contain DNSQR (for )
        domain = packet[scapy.DNSQR].qname.decode() # get domain name

        exclude_keywords = ["google", "cloud", "bing", "static"]

        # verify if is not a usually domain and if it was not stored
        if not domain in domains_seen and not any(keyword in domain for keyword in exclude_keywords):
            domains_seen.add(domain)

            print(colored(f"\t+) {domain}", "green"))

#sniffing
def sniff(interface):
    print(colored("\n[-] Starting sniffing...\n", "blue"))
    scapy.sniff(iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0) # filering by dns and execute process_dns_packet function for each packet

def print_banner():
    print(colored("""
█▀▄ █▄░█ █▀   █▀ █▄░█ █ █▀▀ █▀▀ █▀▀ █▀█
█▄▀ █░▀█ ▄█   ▄█ █░▀█ █ █▀░ █▀░ ██▄ █▀▄\n""", 'white'))

    print(colored("""Mᴀᴅᴇ ʙʏ sᴀᴍᴍʏ-ᴜʟғʜ\n""", 'yellow'))

#Main logic
def main():
    global domains_seen
    domains_seen = set()

    print_banner()

    interface = get_arguments() # get arguments
    isValid = verify(interface) # verify if is a valid interface

    if isValid:
        sniff(interface) # start the sniff filtering by udp in port 53 (DNS)
    else:
        print(colored("\n[!] Invalid Network Interface Name\n", "red"))

if __name__ == "__main__":
    main()
