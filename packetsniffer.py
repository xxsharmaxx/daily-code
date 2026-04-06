# Day 7: Basic Packet Sniffer

import socket

def packet_sniffer():
    # Create raw socket
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

    # Get local host IP
    host = socket.gethostbyname(socket.gethostname())

    # Bind socket
    sniffer.bind((host, 0))

    # Include IP headers
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # Enable promiscuous mode
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print(f"Listening on {host}...\n")
 try:
        while True:
            raw_data, addr = sniffer.recvfrom(65535)

            print(f"Packet from: {addr}")

    except KeyboardInterrupt:
        print("\nStopping sniffer...")

        # Disable promiscuous mode
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == "__main__":
    packet_sniffer()
   
