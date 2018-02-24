#!/usr/bin/env python


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


lr = Node(data=4)
ll = Node(data=1)
l = Node(data=5, left=ll, right=lr)
rl = Node(data=6)
r = Node(data=2, left=rl)
tree = Node(data=3, left=l, right=r)


import sys


def inOrder(root):
    #Write your code here

    node = root

    if node.left is not None:
        inOrder(node.left)

    sys.stdout.write(str(node.data) + ' ')

    if node.right is not None:
        inOrder(node.right)


inOrder(tree)