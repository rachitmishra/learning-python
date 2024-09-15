"""
Definition One:

A tree consists of a set of nodes and a set of edges that connect pairs of nodes.

A tree has the following properties:
One node of the tree is designated as the root node.

Every node nn, except the root node, is connected by an edge from exactly one other node pp,
where pp is the parent of nn.

A unique path traverses from the root to each node.

Definition Two:

A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree.
The root of each subtree is connected to the root of the parent tree by an edge.

Traversing a Tree:
DFS -> Depth First Search
BFS -> Breadth First Search


"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, value):
        self.left = Node(value)

    def set_right(self, value):
        self.right = Node(value)


class Tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def traverse_pre_order(self):
        print(self.pre_order(self.root, "")[:-2])

    def pre_order(self, start, traversal):
        if start:
            traversal += str(start.value) + "->"
            traversal += self.pre_order(start.left, "")
            traversal += self.pre_order(start.right, "")
        return traversal

    def traverse_in_order(self):
        print(self.in_order(self.root, "")[:-2])

    def in_order(self, start, traversal):
        if start:
            traversal += self.pre_order(start.left, "")
            traversal += str(start.value) + "->"
            traversal += self.pre_order(start.right, "")
        return traversal

    def traverse_post_order(self):
        print(self.post_order(self.root, "")[:-2])

    def post_order(self, start, traversal):
        if start:
            traversal += self.pre_order(start.left, "")
            traversal += self.pre_order(start.right, "")
            traversal += str(start.value) + "->"
        return traversal


if __name__ == '__main__':
    tree = Tree(4)
    tree.root.set_left(3)
    tree.root.set_right(5)
    tree.root.left.set_left(1)
    tree.root.left.set_right(2)
    tree.root.right.set_right(6)
    tree.root.right.set_right(7)
    tree.traverse_pre_order()
    tree.traverse_in_order()
    tree.traverse_post_order()
