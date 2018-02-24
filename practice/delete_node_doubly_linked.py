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
            tail = _get_tail(head)
            new_head = head.next
            tail.next = new_head
            return new_head

        else:
            for i in range(position - 1):
                node = node.next

            node.next = node.next.next

        return head


def _print_list(head):
    num_head = 0
    node = head
    while node is not None:
        if node == head:
            if num_head == 1:
                break;
            else:
                num_head += 1

        print node.data
        node = node.next


def _get_tail(head):
    node = head
    while node is not None:
        if node.next == head:
            break;
        node = node.next

    return node


head = Node(data=0)
one = Node(data=1)
head.next = one
two = Node(data=2)
one.next = two
three = Node(data=3)
two.next = three
three.next = head

_print_list(head)
print ''

tail = _get_tail(head)

# head = Delete(head, 0)
head = Delete(head, 3)

_print_list(head)