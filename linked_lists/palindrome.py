"""Q2.6"""
from linked_list import LinkedList

"""O(2n) == O(n) Time Complexity"""
def is_palindrome(node):
    # Find length
    runner = node
    length = -1
    while runner != None:
        runner = runner.next
        length += 1

    stack = []
    half = length // 2
    while node != None:
        if length > half:
            stack.append(node.data)
        elif stack[-1] == node.data:
            stack.pop()
        node = node.next
        length -= 1

    if len(stack) == 0:
        return True
    return False

"""Refactored Solution"""
def is_palindrome_o(node):
    fast = node
    stack = []
    # Find the midpoint and push data onto stack
    while fast != None and fast.next != None:
        stack.append(node.data)
        node = node.next
        fast = fast.next.next
    # Skip middle element if odd number of nodes
    if fast != None:
        node = node.next
    # Traverse the rest of the list checking if elements are the same
    while node != None:
        if node.data != stack[-1]:
            return False
        stack.pop()
        node = node.next
    return True


if __name__ == '__main__':
    ll = LinkedList([0, 1, 2, 2, 1, 0])
    print(is_palindrome(ll.head))
    print(is_palindrome_o(ll.head))
