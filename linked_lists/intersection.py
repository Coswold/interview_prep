"""Q2.7"""
from linked_list import LinkedList

def intersection(ll1, ll2):
    current1 = ll1.head
    length1 = 0
    while current1 != None:
        length1 += 1
        current1 = current1.next

    current2 = ll2.head
    length2 = 0
    while current2 != None:
        length2 += 1
        current2 = current2.next

    if current2 != current1:
        raise ValueError('No Intersection')

    if length1 > length2:
        length = length1 - length2
        current = ll1.head
        while length > 0:
            current = current.next
            length -= 1
        return current

    else:
        length = length2 - length1
        current = ll2.head
        while length > 0:
            current = current.next
            length -= 1
        return current



if __name__ == '__main__':
    ll1 = LinkedList([0, 1, 2, 2, 1, 0])
    ll2 = LinkedList([2, 2, 1, 0])
    print(intersection(ll1, ll2))
