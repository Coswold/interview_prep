"""Q2.7"""
from linked_list import LinkedList

def intersection(node1, node2):
    while node1 != None and node2 != None:
        if node1 == node2:
            return node1
        

if __name__ == '__main__':
    ll = LinkedList([0, 1, 2, 2, 1, 0])
    print(is_palindrome(ll.head))
    print(is_palindrome_o(ll.head))
