from binary_tree import BinarySearchTree, BinaryNode

def validate(node, min=None, max=None):
    if node == None:
        return True
    if (min != None and node.data <= min) or (max != None and node.data > max):
        return False
    if validate(node.left, min, node.data) == False or validate(node.right, node.data, max) == False:
        return False
    return True

if __name__ == '__main__':
    tree = BinarySearchTree([8, 4, 9, 7, 10, 1])
    node = BinaryNode(5)
    node.left = BinaryNode(8)
    node.right = BinaryNode(4)

    print(validate(node))
