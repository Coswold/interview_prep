"""Q2.8"""
from linked_list import Node

def loop_detection(node):
    visited = {}
    while node != None:
        if node not in visited:
            visited[node] = True
        else:
            return node
        node = node.next
    return None

if __name__ == '__main__':
    # 1 -> 2 -> 3 -> 8
    # 1 -> 4 -> 8 -> 16 ^ 2
    node1 = Node('A')
    node1.next = Node('B')
    node1.next.next = Node('C')
    node1.next.next.next = Node('D')
    node1.next.next.next.next = node1.next.next

    print(loop_detection(node1))
