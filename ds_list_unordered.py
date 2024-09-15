"""
Un Ordered List
"""
from ds_list_ordered import Node


class LinkedList(object):
    last_position = None

    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        new_node.next = current
        self.head = new_node

    def append_1(self, new_node):
        if self.last_position:
            temp = self.get_position(self.last_position - 1)
            new_node.next = temp.next
            temp.next = new_node
        else:
            self.head = new_node

    def search(self, value):
        current = self.head
        found = False
        if current:
            while current is not None and not found:
                if current.value == value:
                    found = True
                else:
                    current = current.next
        return found

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            counter += 1
            current = current.next

        return None

    def insert(self, new_element, position):
        current_position = 1
        current = self.head
        if self.head:
            while current.next:
                current_position += 1
                temp = current.next
                if current_position == position:
                    new_element.next = temp
                    current.next = new_element
                else:
                    current = temp
        else:
            self.head = new_element

    def delete(self, value):
        current = self.head
        prev = None
        found = False
        if self.head:
            while not found:
                if current.value == value:
                    found = True
                else:
                    prev = current
                    current = current.next

        if prev is not None:
            prev.next = current.next
        else:
            self.head = current.next


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    print ll.head.next.next.value
    # Should also print 3
    print ll.get_position(3).value

    # Test insert
    ll.insert(e4, 3)
    # Should print 4 now
    print ll.get_position(3).value

    # Test delete
    ll.delete(1)
    # Should print 2 now
    print ll.get_position(1).value
    # Should print 4 now
    print ll.get_position(2).value
    # Should print 3 now
    print ll.get_position(3).value

    print ll.search(3)
