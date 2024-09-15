"""
De-Queue
"""


class Deque:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def add_front(self, item):
        self.data.append(item)

    def add_rear(self, item):
        self.data.insert(0, item)

    def remove_front(self):
        return self.data.pop()

    def remove_rear(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)
