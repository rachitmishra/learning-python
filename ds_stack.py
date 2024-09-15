"""
Stack

Last In First Out
"""


class Stack(object):
    def __init__(self):
        self.data = []

    def is_empty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)  # O(n)

    def pop(self):
        return self.data.pop()  # O(n)

    def peak(self):
        return self.data[len(self.data) - 1]

    def peak_pos(self, position):
        return self.data[len(self.data) - position - 1]

    def reverse_peak(self, position):
        return self.data[position]

    def size(self):
        return len(self.data)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peak())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
