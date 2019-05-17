"""Q2.7"""
from linked_list import LinkedList, Node

def intersection(ll1, ll2):
    current1 = ll1
    length1 = 0
    while current1.next != None:
        length1 += 1
        current1 = current1.next

    current2 = ll2
    length2 = 0
    while current2.next != None:
        length2 += 1
        current2 = current2.next

    if current2 != current1:
        raise ValueError('No Intersection')

    if length1 > length2:
        length = length1 - length2
        current = ll1
        while length > 0:
            current = current.next
            length -= 1
        current2 = ll2
        while current != current2:
            current = current.next
            curren2 = current2.next
        return current

    else:
        length = length2 - length1
        current = ll2
        while length > 0:
            current = current.next
            length -= 1
        current1 = ll1
        while current != current1:
            current = current.next
            current1 = current1.next
        return current



if __name__ == '__main__':
    # 1 -> 2 -> 3 -> 8
    # 1 -> 4 -> 8 -> 16 ^ 3
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node1.next.next.next = Node(8)
    node2 = Node(1)
    node2.next = Node(4)
    node2.next.next = Node(8)
    node2.next.next = Node(16)
    node2.next.next.next = node1.next.next
    print(intersection(node1, node2))
