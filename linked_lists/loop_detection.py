"""Q2.8"""
from linked_list import Node

"""First approach"""
def loop_detection(node):
    visited = {}
    while node != None:
        if node not in visited:
            visited[node] = True
        else:
            return node
        node = node.next
    return None

"""Optimized solution (broken)"""
def loop_detection2(node):
    slow = node
    fast = node
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break

    if fast == None or fast.next == None:
        return None

    slow = node
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast

if __name__ == '__main__':
    node1 = Node('A')
    node1.next = Node('B')
    node1.next.next = Node('C')
    node1.next.next.next = Node('D')
    node1.next.next.next.next = Node('E')
    node1.next.next.next.next.next = node1.next

    print(loop_detection(node1))
    print(loop_detection2(node1))
