from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update & move to end
            self.cache.move_to_end(key)
        
        self.cache[key] = value

        # Remove least recently used
        if len(self.cache) > self.capacity:
            removed = self.cache.popitem(last=False)
            print(f"❌ Removed (LRU): {removed}")


# Demo
cache = LRUCache(3)

cache.put(1, "A")
cache.put(2, "B")
cache.put(3, "C")

print(cache.get(1))  # Access 1 → becomes recent

cache.put(4, "D")    # Removes least used (2)

print(cache.get(2))  # -1 (removed)
print(cache.get(3))  # C
