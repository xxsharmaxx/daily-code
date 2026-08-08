import os
import time
from datetime import datetime


def format_size(size):
    units = ["B", "KB", "MB", "GB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} TB"


def scan_logs(folder):
    logs = []

    for root, _, files in os.walk(folder):

        for filename in files:

            if filename.lower().endswith(".log"):

                path = os.path.join(root, filename)

                try:
                    size = os.path.getsize(path)
                    modified = os.path.getmtime(path)

                    logs.append({
                        "path": path,
                        "size": size,
                        "modified": modified
                    })

                except OSError:
                    pass

    return logs


def main():

    print("=" * 60)
    print("             LOG ROTATION MANAGER")
    print("=" * 60)

    folder = input("Enter log folder: ").strip()

    if not os.path.isdir(folder):
        print("❌ Folder not found.")
        return

    try:
        days = int(input("Delete logs older than how many days? "))

        if days < 0:
            raise ValueError

    except ValueError:
        print("❌ Enter a valid number.")
        return

    logs = scan_logs(folder)

    if not logs:
        print("\nNo .log files found.")
        return

    now = time.time()
    limit = now - (days * 24 * 60 * 60)

    old_logs = []
    total_size = 0

    print("\n📋 LOG FILES")
    print("-" * 60)

    for log in logs:

        date = datetime.fromtimestamp(
            log["modified"]
        ).strftime("%Y-%m-%d %H:%M")

        print(
            f"{format_size(log['size']):>10} | "
            f"{date} | "
            f"{log['path']}"
        )

        if log["modified"] < limit:
            old_logs.append(log)
            total_size += log["size"]

    print("\n" + "=" * 60)

    print(f"Total log files : {len(logs)}")
    print(f"Old log files   : {len(old_logs)}")
    print(f"Recoverable     : {format_size(total_size)}")

    if not old_logs:
        print("\n✅ No old logs need to be removed.")

    else:

        choice = input(
            "\nDelete these old logs? (y/n): "
        ).lower()

        deleted = 0
        recovered = 0

        if choice == "y":

            for log in old_logs:

                try:
                    os.remove(log["path"])

                    deleted += 1
                    recovered += log["size"]

                    print(
                        f"🗑️ Deleted: {log['path']}"
                    )

                except OSError as error:

                    print(
                        f"❌ Could not delete "
                        f"{log['path']}: {error}"
                    )

            print("\n" + "=" * 60)
            print("CLEANUP COMPLETE")
            print("=" * 60)

            print(f"Deleted files : {deleted}")
            print(f"Space freed   : {format_size(recovered)}")

            with open(
                "log_cleanup_report.txt",
                "w",
                encoding="utf-8"
            ) as report:

                report.write("LOG ROTATION REPORT\n")
                report.write("=" * 40 + "\n\n")
                report.write(f"Folder: {folder}\n")
                report.write(f"Age limit: {days} days\n")
                report.write(f"Deleted: {deleted}\n")
                report.write(
                    f"Space freed: {format_size(recovered)}\n"
                )

            print("\n📄 Report saved as "
                  "log_cleanup_report.txt")

        else:
            print("\nOperation cancelled.")


if __name__ == "__main__":
    main()
