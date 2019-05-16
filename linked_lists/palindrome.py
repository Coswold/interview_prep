"""Q2.6"""
from linked_list import LinkedList

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
            print(stack[-1])
            stack.pop()
        node = node.next
        length -= 1

    if len(stack) == 0:
        return True
    return False



if __name__ == '__main__':
    ll = LinkedList(['t', 'a', 'c', 'c', 'a', 't'])
    print(is_palindrome(ll.head))
