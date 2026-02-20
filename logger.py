from datetime import datetime
import os
import csv

LOG_FILE = os.path.join(os.path.dirname(__file__), "connections.csv")

def log_connection(ip, port, data, is_malicious=False, attack_type=""):
    timestamp = datetime.now().isoformat()
    data_length = len(data) if data else 0
    
    file_exists = os.path.exists(LOG_FILE)
    
    with open(LOG_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists or os.path.getsize(LOG_FILE) == 0:
            writer.writerow(["timestamp", "ip", "port", "data_length", "is_malicious", "attack_type"])
        writer.writerow([timestamp, ip, port, data_length, is_malicious, attack_type])