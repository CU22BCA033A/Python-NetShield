from scapy.all import sniff, IP, TCP
from firewall.logger import log_event

ALLOWED_IPS = ["192.168.1.10"]
DENIED_IPS = ["192.168.1.100"]
ALLOWED_PORTS = [22, 80, 443]
DENIED_PORTS = [23, 445]

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if src_ip in DENIED_IPS:
            log_event(f"[❌ BLOCKED] {src_ip} -> {dst_ip}")
            return
        
        if packet.haslayer(TCP):
            dst_port = packet[TCP].dport
            if dst_port in DENIED_PORTS:
                log_event(f"[❌ BLOCKED] {src_ip} -> {dst_ip}:{dst_port}")
                return

        log_event(f"[✅ ALLOWED] {src_ip} -> {dst_ip}")

def start_sniffing():
    print("[🔥 Firewall Monitoring Traffic...]")
    sniff(prn=packet_callback, store=False)
