import os

def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} TB"

folder = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Folder does not exist.")
    exit()

large_files = []

for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root, file)
        try:
            size = os.path.getsize(path)
            large_files.append((size, path))
        except:
            pass

large_files.sort(reverse=True)

print("\nLargest Files:\n")

for size, path in large_files[:10]:
    print(f"{format_size(size):>10}  {path}")

total = sum(size for size, _ in large_files)

print("\n-------------------------")
print("Total Files :", len(large_files))
print("Total Size  :", format_size(total))

with open("cleanup_report.txt", "w", encoding="utf-8") as report:
    report.write("Disk Cleanup Report\n\n")
    for size, path in large_files[:20]:
        report.write(f"{format_size(size)}  {path}\n")

print("\nReport saved as cleanup_report.txt")
