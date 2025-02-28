# 🔥 Python Firewall Project

## 📌 Overview
This project is a **Python-based firewall** that can **monitor, filter, and block network traffic**. It supports:
✅ **Packet Monitoring** using Scapy
✅ **Blocking & Allowing IPs and Ports** dynamically
✅ **Logging** all network events
✅ **Cross-platform support** (Windows & Linux)

---

## 📂 Project Structure
```
firewall_project/
│── firewall/
│   │── __init__.py        # Package initializer
│   │── packet_filter.py    # Passive packet monitoring (Scapy)
│   │── firewall_rules.py   # Active firewall rules (Windows/Linux)
│   │── logger.py           # Logs events
│── main.py                 # Entry point to run the firewall
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

---

## 🚀 Installation

### **🔹 Step 1: Install Dependencies**
```sh
pip install -r requirements.txt
```

### **🔹 Step 2: Run the Firewall**
```sh
python main.py
```

---

## ⚙️ Features & Usage

### **1️⃣ Passive Packet Monitoring (Scapy)**
This mode **logs network traffic** but does not block it.
```python
from firewall.packet_filter import start_sniffing
start_sniffing()
```

### **2️⃣ Active Firewall Rules (Windows/Linux)**
#### **Block & Allow IPs**
```python
from firewall.firewall_rules import block_ip, allow_ip
block_ip("192.168.1.100")   # Block an IP
allow_ip("192.168.1.10")   # Allow an IP
```

#### **Block & Allow Ports**
```python
from firewall.firewall_rules import block_port, allow_port
block_port(23)   # Block Telnet (Port 23)
allow_port(80)   # Allow HTTP (Port 80)
```

### **3️⃣ Logging Events**
All actions are logged in `firewall.log`.
```python
from firewall.logger import log_event
log_event("Blocked IP: 192.168.1.100")
```

---

## 🔧 Customization
You can modify `ALLOWED_IPS`, `DENIED_IPS`, `ALLOWED_PORTS`, and `DENIED_PORTS` in `packet_filter.py`.

```python
ALLOWED_IPS = ["192.168.1.10"]
DENIED_IPS = ["192.168.1.100"]
ALLOWED_PORTS = [22, 80, 443]
DENIED_PORTS = [23, 445]
```

---

## ⚠️ Permissions & Requirements
🔹 **Windows:** Run as **Administrator** (for firewall modifications).  
🔹 **Linux:** Run with **sudo** (for `iptables` rules).  
🔹 **Python 3.8+ Required**

---

## 📌 Future Improvements
✅ Add a **GUI for easy rule management**
✅ Implement **machine learning for intelligent filtering**
✅ Create a **web dashboard for real-time logs**

---

## 🛠️ Contributing
Feel free to contribute! Submit a pull request or report an issue.

---

## 📜 License
This project is **open-source** under the MIT License.

