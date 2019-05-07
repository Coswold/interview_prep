"""Q2.2"""
from linked_list import LinkedList

"""My initial solution"""
def kth(linked_list, k):
    current = linked_list.head
    length = 0
    while current != None:
        current = current.next
        length += 1
    current = linked_list.head
    while length > k:
        current = current.next
        length -= 1
    return current.data

"""Optimized Solution"""
def kth_o(linked_list, k):
    first = linked_list.head
    second = linked_list.head
    while first != None and k > 0:
        first = first.next
        k -= 1
    while first is not None:
        first = first.next
        second = second.next

    return second.data


if __name__ == '__main__':
    ll = LinkedList(['a', 'b', 'c', 'd', 'e', 'f'])
    print(kth(ll, 1))
    print(kth_o(ll, 1))
