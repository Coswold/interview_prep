"""Q4.3"""

from linked_list import LinkedList

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def insert(self, item):
        # Handle the case where the tree is empty
        if self.is_empty():
            #Create a new root node
            self.root = BinaryNode(item)
            #Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        if parent == None:
            parent = self.root
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            # Create a new node and set the parent's left child
            parent.left = BinaryNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # Create a new node and set the parent's right child
            parent.right = BinaryNode(item)
        # TODO: Increase the tree size
        self.size += 1

    def _find_parent_node_recursive(self, item, node, parent=None):
        # Check if starting node exists
        if self.root is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        if node == None or node.data == item:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def list_depths(self):
        items = []
        if not self.is_empty():
            self._traverse_in_order_recursive(self.root, items.append)
        return items

    def _traverse_in_order_recursive(self, node, visit):
        # Traverse left subtree, if it exists
        if node.left != None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.right != None:
            self._traverse_in_order_recursive(node.right, visit)

def create_level_ll(root, lists, level):
    if root == None:
        return
    print(level)
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
    print(tree.root.right)
    listsll = []
    create_level_ll(tree.root, listsll, 0)
    print(listsll)
