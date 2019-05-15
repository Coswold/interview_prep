"""Q2.4"""
from linked_list import LinkedList, Node

def sum_lists(ll1, ll2, carry=0):
    if ll1 == None and ll2 == None and carry == 0:
        return None
    value = carry
    if ll1 != None:
        value += ll1.data
    if ll2 != None:
        value += ll2.data
    result = Node(value % 10)
    if ll1 != None or ll2 != None:
        if value >= 10:
            value = 1
        else:
            value = 0
        more = sum_lists(ll1.next, ll2.next, value)
        result.next = more
    return result


if __name__ == '__main__':
    ll1 = LinkedList([5, 6, 7])
    ll2 = LinkedList([4, 5, 6])
    result = sum_lists(ll1.head, ll2.head)
    while result != None:
        print(result.data)
        result = result.next
