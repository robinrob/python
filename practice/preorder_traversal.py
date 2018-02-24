#!/usr/bin/env python

import sys


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


left2 = Node(data=3)
right2 = Node(data=4)
left1 = Node(data=2, left=left2, right=right2)
right1 = Node(data=5)
tree = Node(data=1, left=left1, right=right1)


def preOrder(root):
    #Write your code here

    node = root
    sys.stdout.write(str(node.data) + ' ')

    if node.left is not None:
        preOrder(node.left)

    if node.right is not None:
        preOrder(node.right)


preOrder(tree)