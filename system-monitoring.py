import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("===== REAL-TIME SYSTEM MONITOR =====\n")

    print(f"🖥️ CPU Usage     : {cpu}%")
    print(f"🧠 RAM Usage     : {memory.percent}%")
    print(f"💾 Disk Usage    : {disk.percent}%")

    print("\n===== MEMORY DETAILS =====")
    print(f"Total RAM : {round(memory.total / (1024**3), 2)} GB")
    print(f"Used RAM  : {round(memory.used / (1024**3), 2)} GB")
    print(f"Free RAM  : {round(memory.available / (1024**3), 2)} GB")

    print("\nPress CTRL + C to stop...")

    time.sleep(2)
