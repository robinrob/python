#!/usr/bin/env python


class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def ReversePrint(head):
    if head is not None:
        if head.next is not None:
            ReversePrint(head.next)
        print head.data


head = Node(data=0)
one = Node(data=1)
head.next = one
two = Node(data=2)
one.next = two
three = Node(data=3)
two.next = three

ReversePrint(head)