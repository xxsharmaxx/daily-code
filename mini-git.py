import os
import json
import hashlib
import datetime

REPO_DIR = ".mygit"
COMMITS_DIR = os.path.join(REPO_DIR, "commits")
INDEX_FILE = os.path.join(REPO_DIR, "index.json")


class MiniGit:

    def init(self):
        os.makedirs(COMMITS_DIR, exist_ok=True)

        if not os.path.exists(INDEX_FILE):
            with open(INDEX_FILE, "w") as f:
                json.dump([], f)

        print("✅ Repository initialized")

    def hash_content(self, content):
        return hashlib.sha256(content.encode()).hexdigest()

    def commit(self, filename, message):

        if not os.path.exists(filename):
            print("❌ File not found")
            return

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        commit_hash = self.hash_content(
            content + str(datetime.datetime.now())
        )

        commit_data = {
            "hash": commit_hash,
            "message": message,
            "timestamp": str(datetime.datetime.now()),
            "content": content
        }

        commit_file = os.path.join(
            COMMITS_DIR,
            commit_hash + ".json"
        )

        with open(commit_file, "w", encoding="utf-8") as f:
            json.dump(commit_data, f, indent=4)

        with open(INDEX_FILE, "r") as f:
            history = json.load(f)

        history.append({
            "hash": commit_hash,
            "message": message
        })

        with open(INDEX_FILE, "w") as f:
            json.dump(history, f, indent=4)

        print("✅ Commit created")
        print("Hash:", commit_hash[:12])

    def log(self):

        if not os.path.exists(INDEX_FILE):
            print("Repository not initialized")
            return

        with open(INDEX_FILE, "r") as f:
            history = json.load(f)

        print("\n=== COMMIT HISTORY ===")

        for commit in reversed(history):
            print(
                f"\nHash: {commit['hash'][:12]}"
            )
            print(
                f"Message: {commit['message']}"
            )

    def checkout(self, commit_hash):

        commit_file = os.path.join(
            COMMITS_DIR,
            commit_hash + ".json"
        )

        if not os.path.exists(commit_file):
            print("❌ Commit not found")
            return

        with open(commit_file, "r") as f:
            commit = json.load(f)

        restored_file = "restored_file.txt"

        with open(restored_file, "w", encoding="utf-8") as f:
            f.write(commit["content"])

        print("✅ File restored")
        print("Saved as:", restored_file)


git = MiniGit()

while True:

    print("\n===== MINI GIT =====")
    print("1. Init Repository")
    print("2. Commit File")
    print("3. View Log")
    print("4. Checkout Commit")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        git.init()

    elif choice == "2":
        filename = input("File name: ")
        message = input("Commit message: ")
        git.commit(filename, message)

    elif choice == "3":
        git.log()

    elif choice == "4":
        commit_hash = input(
            "Enter full commit hash: "
        )
        git.checkout(commit_hash)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
