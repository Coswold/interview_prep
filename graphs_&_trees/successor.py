class BinaryNodeParent(object):

    def __init__(self, parent=None, data=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None


def successor(node):
    if node == None:
        return None
    if node.right != None:
        return leftMost(node.right)
    else:
        q = node
        x = q.parent
        while x != None and x.left != q:
            q = x
            x = x.parent
        return x.data

def leftMost(node):
    if node == None:
        return None
    while node.left != None:
        node = node.left
    return node.data


if __name__ == '__main__':
    n1 = BinaryNodeParent()
    n1.data = 8
    n1.left = BinaryNodeParent(n1, 5)
    n1.right = BinaryNodeParent(n1, 10)
    n1.left.right = BinaryNodeParent(n1.left, 7)
    print(successor(n1.left))
