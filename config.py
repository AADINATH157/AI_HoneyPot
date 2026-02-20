# AI Honeypot Configuration

# Honeypot Settings
HONEYPOT_HOST = '0.0.0.0'
HONEYPOT_PORT = 9999
SOCKET_TIMEOUT = 10  # seconds

# Web Server Settings
WEB_HOST = '0.0.0.0'
WEB_PORT = 8000

# File Paths (auto-detected, no need to change)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
LOG_FILE = os.path.join(BASE_DIR, 'connections.csv')

# ML Detection Thresholds
MALICIOUS_DATA_THRESHOLD = 500  # bytes
