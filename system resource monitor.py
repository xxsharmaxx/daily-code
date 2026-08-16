import os
import time
import psutil
from datetime import datetime


def bar(value, width=25):
    filled = int((value / 100) * width)
    return "█" * filled + "░" * (width - filled)


def bytes_to_gb(value):
    return value / (1024 ** 3)


def show_system():

    os.system("cls" if os.name == "nt" else "clear")

    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print("=" * 65)
    print("             SYSTEM RESOURCE MONITOR")
    print("=" * 65)

    print(
        f"\nTime       : "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print("\nCPU")
    print(f"[{bar(cpu)}] {cpu:.1f}%")

    print("\nMemory")
    print(
        f"[{bar(memory.percent)}] "
        f"{memory.percent:.1f}%"
    )

    print(
        f"Used      : "
        f"{bytes_to_gb(memory.used):.2f} GB"
    )

    print(
        f"Available : "
        f"{bytes_to_gb(memory.available):.2f} GB"
    )

    print("\nDisk")

    print(
        f"[{bar(disk.percent)}] "
        f"{disk.percent:.1f}%"
    )

    print(
        f"Used      : "
        f"{bytes_to_gb(disk.used):.2f} GB"
    )

    print(
        f"Free      : "
        f"{bytes_to_gb(disk.free):.2f} GB"
    )

    print("\nTop Processes")
    print("-" * 65)

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append(
                (
                    info["cpu_percent"] or 0,
                    info["pid"],
                    info["name"],
                    info["memory_percent"] or 0
                )
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied
        ):
            pass

    processes.sort(reverse=True)

    print(
        f"{'PID':<10}"
        f"{'CPU %':<10}"
        f"{'RAM %':<10}"
        f"PROCESS"
    )

    print("-" * 65)

    for cpu_usage, pid, name, ram in processes[:8]:

        print(
            f"{pid:<10}"
            f"{cpu_usage:<10.1f}"
            f"{ram:<10.1f}"
            f"{str(name)[:30]}"
        )


def main():

    print("Starting System Resource Monitor...")

    try:

        while True:

            show_system()

            print(
                "\nPress Ctrl+C to stop monitoring."
            )

            time.sleep(2)

    except KeyboardInterrupt:

        print("\n\nMonitor stopped.")
        print("Goodbye!")


if __name__ == "__main__":
    main()
