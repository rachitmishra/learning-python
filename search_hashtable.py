"""
Hashing

Complexity: O(1)
"""


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(len(hash_value), self.slots)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(len(hash_value), self.slots)

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def get(self, key):
        start_slot = self.hash(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(start_slot, self.slots)
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    @staticmethod
    def hash(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size
