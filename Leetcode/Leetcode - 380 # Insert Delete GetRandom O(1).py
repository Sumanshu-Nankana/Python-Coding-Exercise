import random


class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.data_store = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            self.data_store.append(val)
            self.hash_map[val] = len(self.data_store) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        # Get the index of the value to remove
        idx_to_remove = self.hash_map[val]
        # get the last_value
        last_val = self.data_store[-1]

        # Overwrite the element to remove with the last element
        self.data_store[idx_to_remove] = last_val
        # Update the map
        self.hash_map[last_val] = idx_to_remove

        # Remove redundant element
        self.data_store.pop()
        # Remove the value from the hash_map
        del self.hash_map[val]

        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.data_store) - 1)
        return self.data_store[random_index]

        # we can use the choice method as well
        # return random.choice(self.data_store)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()