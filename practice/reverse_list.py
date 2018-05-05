#!/usr/bin/env python


class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def Reverse(head):
    if head is not None:
        nodes = []
        node = head
        while node is not None:
            nodes.append(node)
            node = node.next

        nodes.reverse()

        prev_node = nodes[0]
        prev_node.next = None
        head = prev_node
        if len(nodes) > 1:
            for node in nodes[1:]:
                prev_node.next = node
                prev_node = node

            prev_node.next = None

    return head


def _print_list(head):
    node = head
    while node is not None:
        print node.data
        node = node.next


head = Node(data=0)
one = Node(data=1)
head.next = one
two = Node(data=2)
one.next = two
three = Node(data=3)
two.next = three

_print_list(head)
print
head = Reverse(head)
_print_list(head)