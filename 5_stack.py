class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def rev_string(st):
    s = Stack()
    r = ''
    for a in st:
        s.push(a)
    while not s.is_empty():
        r += s.pop()
    print(r)


rev_string("Dolby")
