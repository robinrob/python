#!/usr/bin/env python


class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def _query1(head, x, mx):
    new_node = Node(x, next_node=head)
    if new_node.data > mx:
        mx = new_node.data

    return new_node, mx


def _query2(head, mx):
    if head is not None:
        new_head = head.next
        if head.data == mx:
            mx = _find_max(new_head)
        return new_head, mx

    else:
        return head, mx


def _query3(mx):
    print mx


def _find_max(head):
    mx = 0

    while head is not None:
        mx = max(mx, head.data)
        head = head.next

    return mx


def _print_list(head):
    node = head
    while node is not None:
        print node.data
        node = node.next
    print


def _print_nodes(nodes):
    for node in nodes:
        print node.data
    print


def run():
    n = int(raw_input())

    head = None
    mx = 0

    for i in range(n):
        row = [int(i) for i in raw_input().split(' ')]

        query_type = row[0]
        x = None
        if len(row) == 2:
            x = row[1]

        if query_type == 1:
            head, mx = _query1(head, x, mx)

        elif query_type == 2:
            head, mx = _query2(head, mx)

        elif query_type == 3:
            _query3(mx)

run()