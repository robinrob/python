#!/usr/bin/env python


class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def CompareLists(headA, headB):
    nodeA = headA
    nodeB = headB
    while nodeA is not None:
        if nodeB is None or (nodeA.data != nodeB.data):
            return 0

        nodeA = nodeA.next
        nodeB = nodeB.next

    return 1 if nodeB is None else 0

head1 = Node(data=0)
one = Node(data=1)
head1.next = one
two = Node(data=2)
one.next = two
three = Node(data=3)
two.next = three

head2 = Node(data=0)
one = Node(data=0)
head2.next = one
two = Node(data=2)
one.next = two
three = Node(data=3)
two.next = three

res = CompareLists(head1, head2)
print 'res: %s' % res