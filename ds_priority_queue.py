"""
Queue

First In First Out
"""


class Queue(object):
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def enqueue(self, item):
        self.data.insert(0, item)  # O(n)

    def dequeue(self):
        self.data.pop()  # O(1)

    def size(self):
        return len(self.data)
