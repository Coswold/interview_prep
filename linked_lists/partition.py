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

if __name__ == '__main__':
    ll = LinkedList([3, 5, 8, 5, 10, 2, 1])
    print(partition(ll, 5))
