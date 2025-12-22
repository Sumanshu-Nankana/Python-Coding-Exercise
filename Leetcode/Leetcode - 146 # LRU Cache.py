from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = dict()
        self.cache = deque()

    def get(self, key: int) -> int:
        if key in self.hash_map:
            value = self.hash_map[key]
            self.cache.remove(key)
            self.cache.appendleft(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            if len(self.cache) == self.capacity:
                oldest = self.cache.pop()
                del self.hash_map[oldest]

        else:
            self.cache.remove(key)
        self.hash_map[key] = value
        self.cache.appendleft(key)


# more optimal solution and more faster
class LRUCacheWithoutDeque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = dict()

    def get(self, key: int) -> int:
        if key in self.hash_map:
            value = self.hash_map[key]
            del self.hash_map[key]
            self.hash_map[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            if len(self.hash_map) < self.capacity:
                self.hash_map[key] = value
            else:
                del self.hash_map[next(iter(self.hash_map))]
                self.hash_map[key] = value
        else:
            del self.hash_map[key]
            self.hash_map[key] = value


# Not much optimal
class LRUCacheWithoutDequeSimple:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = dict()

    def get(self, key: int) -> int:
        if key in self.hash_map:
            value = self.hash_map[key]
            del self.hash_map[key]
            self.hash_map[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            if len(self.hash_map) < self.capacity:
                self.hash_map[key] = value
            else:
                oldest_key = list(self.hash_map.keys())[0]
                del self.hash_map[oldest_key]
                self.hash_map[key] = value
        else:
            del self.hash_map[key]
            self.hash_map[key] = value



from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # last=False pops the first (oldest) item
            self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
