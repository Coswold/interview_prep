"""Q2.4"""
from linked_list import LinkedList

def partition (linked_list, part):
    node = linked_list.head
    while node is not None:
        if node.data >= part:
            runner = node.next
            while runner is not None:
                if runner.data < part:
                    temp = node.data
                    node.data = runner.data
                    runner.data = temp
                    break
                runner = runner.next
        node = node.next
    return linked_list

def optimized_partition (linked_list, part):
    new_ll = LinkedList()
    search = linked_list.head
    while search is not None:
        if search.data < part:
            new_ll.prepend(search.data)
        else:
            new_ll.append(search.data)
        search = search.next
    return new_ll

if __name__ == '__main__':
    ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
    part = 2
    print(partition(ll, part))
    print(optimized_partition(ll, part))
