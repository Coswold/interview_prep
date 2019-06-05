"""Q4.4"""

from binary_tree import BinarySearchTree

def balanced(root, left, right):
    if root.left != None:
        left += 1
        balanced(root.left, left, right)
    if root.right != None:
        right += 1
        balanced(root.right, left, right)
    else:
        return right == left


if __name__ == '__main__':
    tree = BinarySearchTree([1, 2, 0.5, 3, 4, 5, 6])
    left = 0
    right = 0
    print(balanced(tree.root, left, right))
