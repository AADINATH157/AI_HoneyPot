import socket

def simulate_attack():
    target_ip = '127.0.0.1'
    target_port = 9999

    try:
        print(f"[+] Connecting to {target_ip}:{target_port}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        print("[+] Connection established.")

        # Receive initial message from the honeypot
        banner = s.recv(1024).decode()
        if banner:
            print(f"[+] Server banner: {banner.strip()}")
        else:
            print("[!] No banner received from the server.")

        # Send a meaningful payload
        payload = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        print(f"[+] Sending payload: {payload.strip()}")
        s.send(payload.encode())
        print("[+] Payload sent.")

        # Receive response from honeypot
        response = s.recv(1024).decode()
        if response:
            print(f"[+] Response: {response.strip()}")
        else:
            print("[!] No response received from the server.")

        s.close()
        print("[+] Connection closed.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    simulate_attack()