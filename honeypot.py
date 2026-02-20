import socket
import threading
import time
from logger import log_connection
from detector import detect_malicious

HOST = '0.0.0.0'
PORT = 9999
SOCKET_TIMEOUT = 10

def handle_client(conn, addr):
    ip, port = addr
    print(f"[+] Connection from {ip}:{port}")
    
    try:
        conn.settimeout(SOCKET_TIMEOUT)
        conn.send(b"Welcome to the server\r\n")
        data = conn.recv(1024).decode(errors='ignore')
        
        print(f"[+] Data received: {data}")
        
        is_malicious = False
        attack_type = ""
        
        if data:
            try:
                is_malicious, attack_type = detect_malicious(ip, port, data)
                log_connection(ip, port, data, is_malicious, attack_type)
                
                if is_malicious:
                    print(f"[!] Malicious behavior detected: {attack_type}")
                    conn.send(b"Malicious behavior detected! Closing connection...\r\n")
                else:
                    conn.send(b"Connection seems normal. Closing...\r\n")
            except Exception as e:
                print(f"[!] Error in detection: {e}")
                conn.send(b"Error in detection. Closing connection...\r\n")
        
        time.sleep(1)
        conn.send(b"Goodbye!\r\n")
    except socket.timeout:
        print(f"[!] Connection from {ip}:{port} timed out")
    except Exception as e:
        print(f"[!] Error handling client {ip}:{port}: {e}")
    finally:
        conn.close()

def start_honeypot():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[+] Honeypot listening on port {PORT}...")
    except OSError as e:
        print(f"[!] Error: Port {PORT} is already in use or cannot be bound. {e}")
        return
    
    try:
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[!] Honeypot shutting down...")
    finally:
        s.close()

if __name__ == "__main__":
    start_honeypot()