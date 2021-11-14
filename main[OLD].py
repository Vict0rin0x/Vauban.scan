from scapy.all import *
import optparse

from scapy.volatile import RandShort


def scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1,
                        verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def printfun(returnlist):
    print("IP\t\t\tMAC Address\n----------------------------------------------")
    for elem in returnlist:
        print(elem["ip"] + "\t\t" + elem["mac"])


def portScan(dstIp, port):
    print("syn scan on, %s with ports %s" % (dstIp, port))
    sport = RandShort()
    for port in port:
        pkt = sr1(IP(dst=dstIp) / TCP(sport=port, dport=port, flags="S"), timeout=1, verbose=0)
        if pkt != None:
            if pkt.haslayer(TCP):
                if pkt[TCP].flags == 20:
                    print_ports(port, "Closed")
                elif pkt[TCP].flags == 18:
                    print_ports(port, "Open")
                else:
                    print_ports(port, "TCP packet resp / filtered")
            elif pkt.haslayer(ICMP):
                print_ports(port, "ICMP resp / filtered")
            else:
                print_ports(port, "Unknown resp")
                print(pkt.summary())
        else:
            print_ports(port, "Unanswered")


def getip():
    parser = optparse.OptionParser()
    parser.add_option('-i', "--ip", dest='received_ip', help="Please enter the ip you want to scan")
    (option, arguments) = parser.parse_args()
    return option.received_ip


# Donnée membres :
portList = []

ipreq = getip()
listIp = scan(ipreq)
printfun(listIp)
portScan(ipreq, 80)
