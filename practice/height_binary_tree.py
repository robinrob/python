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


def height(root):
    depth, max_depth = _in_order(root, 0, 0)
    print max_depth - 1


def _in_order(node, depth, max_depth):
    #Write your code here

    depth += 1

    if node.left is not None:
        depth, max_depth = _in_order(node.left, depth, max_depth)

    if node.right is not None:
        depth, max_depth = _in_order(node.right, depth, max_depth)

    max_depth = max(max_depth, depth)
    depth -= 1

    return depth, max_depth


height(tree)