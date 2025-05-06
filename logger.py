import csv
from datetime import datetime

def log_connection(ip, port, data):
    with open("connections.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), ip, port, data.strip()])
