from linked_list import LinkedList

def remove_dups(linked_list):
    buffer = {}
    current_node = linked_list.head
    while current_node is not None:
        if current_node.data not in buffer:
            buffer[current_node.data] = 1
        else:
            linked_list.delete(current_node.data)
        current_node = current_node.next
    return linked_list.items()

if __name__ == '__main__':
    ll = LinkedList(['a', 'c', 'c', 'c', 'b', 'b', 'b', 'c', 'c'])
    print(remove_dups(ll))
