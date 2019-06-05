"""Q4.3"""

from linked_list import LinkedList
from binary_tree import BinarySearchTree

def create_level_ll(root, lists, level):
    if root == None:
        return
    if len(lists) == level:
        list = LinkedList()
        lists.append(list)
    else:
        list = lists[level]
    list.append(root.data)
    create_level_ll(root.left, lists, level + 1)
    create_level_ll(root.right, lists, level + 1)


if __name__ == '__main__':
    tree = BinarySearchTree([5, 6, 3, 8, 4, 10, 1, 2])
    listsll = []
    create_level_ll(tree.root, listsll, 0)
    print(listsll)
