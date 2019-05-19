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
    node = node.next
    fast = node.next.next
    while fast != None:
        print(node, fast)
        if fast == node:
            return node
        fast = fast.next.next
        node = node.next

    return None

if __name__ == '__main__':
    node1 = Node('A')
    node1.next = Node('B')
    node1.next.next = Node('C')
    node1.next.next.next = Node('D')
    node1.next.next.next.next = Node('E')
    node1.next.next.next.next.next = node1.next

    #print(loop_detection(node1))
    print(loop_detection2(node1))
