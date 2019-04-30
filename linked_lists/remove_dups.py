"""Q2.1"""
from linked_list import LinkedList

"""O(n) time complexity"""
def remove_dups(linked_list):
    buffer = {}
    current_node = linked_list.head
    previous = None
    while current_node is not None:
        if current_node.data not in buffer:
            buffer[current_node.data] = 1
            previous = current_node
        else:
            previous.next = current_node.next
        current_node = current_node.next
    return linked_list.items()

if __name__ == '__main__':
    ll = LinkedList(['a', 'b', 'c', 'c', 'c', 'b', 'b', 'b', 'c', 'c'])
    print(remove_dups(ll))
