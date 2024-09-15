"""
Binary Tree

If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

Searching an item is O(logn) = Height of node

Unbalanced balance tree
"""
from ds_tree import Node


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        self.insert_helper(self.root, value)

    def search(self, value):
        self.search_helper(self.root, value)

    def insert_helper(self, node, value):
        if node is not None:
            if node.value > value:
                if node.left is not None:
                    self.insert_helper(node, value)
                else:
                    node.left = Node(value)
            else:
                if node.right is not None:
                    self.insert_helper(node, value)
                else:
                    node.right = Node(value)

    def search_helper(self, node, value):
        if node is not None:
            if node.value > value:
                return True
            elif node.value > value:
                if node.left is not None:
                    self.search_helper(node, value)
            else:
                if node.right is not None:
                    self.search_helper(node, value)

        return False
