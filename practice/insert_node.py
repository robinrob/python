#!/usr/bin/env python


class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def _print_list(head):
    while head is not None:
        print head.data
        head = head.next


def InsertNth(head, data, position):
    if head is None:
        head = Node(data=data, next_node=None)

    else:
        node = head
        if position > 0:
            for i in range(position-1):
                node = node.next

            next_node = node.next
            new_node = Node(data=data, next_node=next_node)
            node.next = new_node
        else:
            new_node = Node(data=data, next_node=head)
            head = new_node

    return head


n = int(raw_input())

head = None
for i in range(n):
    data, pos = (int(i) for i in raw_input().split(' '))
    head = InsertNth(head, data, pos)

_print_list(head)

