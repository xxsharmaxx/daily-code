import socket
import threading
from queue import Queue

target = input("Enter target IP or domain: ")
start_port = 1
end_port = 100

queue = Queue()

print_lock = threading.Lock()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            with print_lock:
                print(f"✅ Port {port} is OPEN")

        sock.close()

    except:
        pass


def threader():
    while True:
        port = queue.get()
        scan_port(port)
        queue.task_done()


# Create threads
for _ in range(50):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# Add ports to queue
for port in range(start_port, end_port + 1):
    queue.put(port)

queue.join()

print("\n🎯 Scanning Complete.")
