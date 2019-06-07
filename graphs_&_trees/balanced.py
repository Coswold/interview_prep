"""Q4.4"""

from binary_tree import BinarySearchTree

def get_height(root):
    if root == None:
        return -1
    return max(get_height(root.left), get_height(root.right) + 1)

def balanced(root):
    if root == None:
        return True
    height_diff = abs(get_height(root.left) - get_height(root.right))
    if height_diff > 1:
        return False
    else:
        return balanced(root.left) and balanced(root.right)


if __name__ == '__main__':
    tree = BinarySearchTree([5, 2, 7, 3, 1, 6, 8])
    print(balanced(tree.root))
    print(get_height(tree.root))
