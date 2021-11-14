# We used argparse for the args
import argparse
# Python objects are returned to js. We need to import json to return JSON objects (to be understood by JS)
import json
import sys
from scapy.all import *
from scapy.layers.inet import TCP, IP
from scapy.layers.l2 import ARP, Ether
import eel
eel.init("WEB")

#Store method used in the script
class methods():
    def __init__(self, ipRange, ports, method, interface):
        self.ipRange = ipRange
        self.ports = ports
        self.method = method
        self.interface = interface

#Store every client and parameters (IP, MAC and ports)
class ipElements():

    #Method to scan ports is implemented in class used to store ipElements, so we can call it for each ipElements
    def portScan(self,portsRange,interface):
        print("Start scanning...")
        for port in portsRange:
            print("Scan for " + str(port))
            pkt = sr1(IP(dst=self.ip) / TCP(sport=RandShort(), dport=port, flags="S"), timeout=1, verbose=0,iface=str(interface))
            if pkt != None:
                if pkt.haslayer(TCP):
                    #Flag return 20 -> Closed port
                    if pkt[TCP].flags == 20:
                        self.closedPorts.append(port)
                    #Flag return 18 -> Opened port
                    elif pkt[TCP].flags == 18:
                        self.openPorts.append(port)
                    #Flag return else -> Filtered port
                    else:
                        self.filteredPorts.append(port)
                else:
                    self.closedPorts.append(port)
                    #Unkown resp so go to closed ports
            else:
                self.closedPorts.append(port)
                #Unanswered so go to closed ports
        print("finished scan")

    def __init__(self, ip, mac):
        self.mac = mac
        self.ip = ip
        self.openPorts = []
        self.closedPorts = []
        self.filteredPorts = []
        print("New device detected -> IP : " + str(ip))



    #Method to put everything in a dictionnary. This is used for JSON convertion further in the script
    def to_dict(self):
        return {"mac" : self.mac, "ip" : self.ip, "openPorts" : self.openPorts, "closedPorts" : self.closedPorts, "filteredPorts" : self.filteredPorts}

#Define a network (with clients rattached to it)
class Network():
    def __init__(self, ipRange):
        self.ipRange = ipRange
        self.client_list = []
    def to_dict(self):
        c = []
        for element in self.client_list:
            d = element.to_dict()
            c.append(d)
        n = {"ipRange" :  self.ipRange, "client_list" : c }

        return n

def get_args():
    #Parse every argument
    parser = argparse.ArgumentParser("Ip and port scanner")
    parser.add_argument("-i", "--ip", help="Specify IP network/Ip address", required=True)
    parser.add_argument("-p", "--ports", help="Specify ports tested (dont specify if 1 to 1024)")
    parser.add_argument("-m", "--method", help="Specify method : (TCP SYN : t, UDP : u) TCP by default  ")
    parser.add_argument("-int", "--interface", help="Specify your interface used for this scan (make sure that this is correct)", required=True)
    args = parser.parse_args()

    targetIp = args.ip
    method = args.method.lower()
    interface = args.interface

    if args.ports:
        beforeSplit = args.ports
        #Split args that are like that -> 80-79-21
        beforeMap = beforeSplit.split("-")
        #Create a list of it
        targetPorts = list(map(int,beforeMap))
    else:
        #Default list, way longer
        targetPorts = range(1, 512)

    #To be fair, udp doesnt make any difference. Will try to implement that later
    if method == "tcp" or method == "t":
        # execute method for syn
        print("Recap : \nMethod : " + str(method) + "\nIp range : " + str(targetIp) + "\nPorts tested : " + str(
            targetPorts))
    elif method == "udp" or method == "u":
        print("Recap : \nMethod : " + str(method) + "\nIp range : " + str(targetIp) + "\nPorts tested : " + str(
            targetPorts))
    else:
        sys.exit("Wrong method. Please retry")

    return methods(targetIp, targetPorts, method, interface)


#Method to perform a IPScan
def ipScan(ipTarget):
    arp_request = ARP(pdst=ipTarget)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1,
                        verbose=False)[0]
    network = Network(ipTarget)

    for element in answered_list:
        print(element[1].psrc)
        ipClient = ipElements(element[1].psrc, element[1].hwsrc)
        network.client_list.append(ipClient)

    return network



#Method for eel, not for args
def splitStr(ports):
    beforeSplit = ports
    print(ports)
    beforeMap = beforeSplit.split("-")
    targetPorts = list(map(int,beforeMap))
    return targetPorts



#Eel way
@eel.expose()
def eelMain():
    method = get_args()
    #Perform a ipscan within the ip range in args
    networkGlobal = ipScan(method.ipRange)
    #
    for element in networkGlobal.client_list:
        element.portScan(method.ports,method.interface)

    #Parse networkGlobal to JSON to be understood by JS
    #print(str(networkGlobal.to_dict()))
    JSONnG = json.dumps(networkGlobal.to_dict())
    print(JSONnG)

    return JSONnG

eel.start('results.php')
