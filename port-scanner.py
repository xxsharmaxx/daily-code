# Day 5: Basic Port Scanner
### ✅ Day 5
## Basic Port Scanner using Python (socket programming)

import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Timeout for faster scanning

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: OPEN")

            sock.close()

 except KeyboardInterrupt:
            print("\nScan stopped by user.")
            break

        except socket.gaierror:
            print("Hostname could not be resolved.")
            break

        except socket.error:
            print("Could not connect to server.")
            break


       

# Input
target = input("Enter target IP or domain (e.g., 127.0.0.1): ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

scan_ports(target, start_port, end_port)
