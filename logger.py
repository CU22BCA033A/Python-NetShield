import datetime

LOG_FILE = "firewall.log"

def log_event(event):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.datetime.now()} - {event}\n")
    print(event)
