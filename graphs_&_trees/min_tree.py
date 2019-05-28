"""Q4.2"""

class BinaryNode(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

    def height(self):
        left1 = 0
        right1 = 0
        if self.left != None:
            left1 = 1 + self.left.height()
        if self.right != None:
            right1 = 1 + self.right.height()
        if left1 > right1:
            return left1
        elif right1 >= left1:
            return right1

"""MinTree takes an array(must be sorted in ascending order) and finds the
   minimum height tree possible."""
class MinTree(object):

    def __init__(self, array=None):
        self.root = None
        if array:
            self.insert(array, 0, len(array) - 1)

    def height(self):
        if self.root != None:
            return self.root.height()

    def insert(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = BinaryNode(array[mid])
        if self.root == None:
            self.root = node
        node.left = self.insert(array, start, mid - 1)
        node.right = self.insert(array, mid + 1, end)
        return node


if __name__ == '__main__':
    tree = MinTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    print(tree.root)
    print(tree.height())
