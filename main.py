from firewall.packet_filter import start_sniffing
from firewall.firewall_rules import block_ip, allow_ip, block_port, allow_port

if __name__ == "__main__":
    print("[🚀 Firewall System Started]")
    
    # Example Usage:
    block_ip("192.168.1.100")
    allow_ip("192.168.1.10")
    block_port(23)
    allow_port(80)
    
    # Start packet filtering (passive monitoring)
    start_sniffing()
