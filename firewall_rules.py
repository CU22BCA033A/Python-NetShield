import os
from firewall.logger import log_event

def block_ip(ip):
    os.system(f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip}')
    log_event(f"Blocked IP: {ip}")

def allow_ip(ip):
    os.system(f'netsh advfirewall firewall delete rule name="Block {ip}"')
    log_event(f"Allowed IP: {ip}")

def block_port(port):
    os.system(f'netsh advfirewall firewall add rule name="Block Port {port}" dir=in action=block protocol=TCP localport={port}')
    log_event(f"Blocked Port: {port}")

def allow_port(port):
    os.system(f'netsh advfirewall firewall delete rule name="Block Port {port}"')
    log_event(f"Allowed Port: {port}")
