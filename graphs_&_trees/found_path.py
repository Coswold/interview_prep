"""Q4.1"""

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = []

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

if __name__ == '__main__':
    graph = Graph()
