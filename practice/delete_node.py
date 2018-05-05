#!/usr/bin/env python


class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def Delete(head, position):
    if head is None:
        return head

    else:
        node = head

        if position == 0:
            new_head = head.next
            return new_head

        else:
            for i in range(position - 1):
                node = node.next

            node.next = node.next.next

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
print ''

# head = Delete(head, 0)
# head = Delete(head, 1)
# head = Delete(head, 2)
head = Delete(head, 3)

_print_list(head)