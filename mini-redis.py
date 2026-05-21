class MiniRedis:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value
        print(f"✅ SET {key} = {value}")

    def get(self, key):
        if key in self.store:
            print(f"📦 {key} = {self.store[key]}")
        else:
            print("❌ Key not found")

    def delete(self, key):
        if key in self.store:
            del self.store[key]
            print(f"🗑️ Deleted key: {key}")
        else:
            print("❌ Key not found")

    def keys(self):
        if self.store:
            print("\n🔑 Stored Keys:")
            for key in self.store:
                print("-", key)
        else:
            print("📭 No keys stored")


def main():
    redis = MiniRedis()

    while True:
        print("\n====== MINI REDIS SERVER ======")
        print("1. SET key")
        print("2. GET key")
        print("3. DELETE key")
        print("4. SHOW keys")
        print("5. EXIT")

        choice = input("Enter choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            redis.set(key, value)

        elif choice == "2":
            key = input("Enter key: ")
            redis.get(key)

        elif choice == "3":
            key = input("Enter key: ")
            redis.delete(key)

        elif choice == "4":
            redis.keys()

        elif choice == "5":
            print("👋 Exiting Mini Redis...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
