from scapy.all import *

def scan_network(ip_range):
    print(f"Viendo dsipositivos que estan en mi red: {ip_range}")

    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=0 , verbose=False)
    active_host = [res[1].psrc for res in ans]
    print("Dsipositivos Conectados en este momento son: ")
    for host in active_host:
        print(f"- {host}")

if __name__ == "__main__":
    target_network ="192.168.0.1/24"
    scan_network(target_network)

