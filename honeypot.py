import socket
from logger import log_connection
from detector import detect_malicious

HOST = '0.0.0.0'
PORT = 9999

def start_honeypot():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[+] Honeypot listening on port {PORT}...")

    while True:
        conn, addr = s.accept()
        ip, port = addr
        print(f"[+] Connection from {ip}:{port}")

        conn.send(b"Welcome to the server\r\n")
        data = conn.recv(1024).decode(errors='ignore')
        log_connection(ip, port, data)

        if detect_malicious(ip, port, data):
            print("[!] Malicious behavior detected!")

        conn.close()

if __name__ == "__main__":
    start_honeypot()
