"""Q4.1"""

class Node(object):

    def __init__(self, data=None, following=None):
        """Initialize this node with the given data."""
        self.data = data
        self.following = {}
        self.visited = False

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class Graph(object):

    def __init__(self, iterable=None):
        self.root = Node()
        if iterable:
            for path in iterable:
                self.insert(path)

    def insert(self, path):
        if self.root.data == None:
            self.root.data = path[0]
        current = self.root
        for i in path:
            if i == current.data:
                continue
            elif i not in current.following:
                current.following[i] = Node(i)
            current = current.following[i]

    # def search_data(self, node, data):
    #     if node.data == None:
    #         return
    #     if node.data == data:
    #         return node
    #     node.visited = True
    #     for i in node.following.items():
    #         print(i)
    #         if i.visited == False:
    #             self.search(i, data)
    #     return None

    # def search_path(self, p1, p2):
    #     current = self.root




if __name__ == '__main__':
    graph = Graph()
    graph.insert(['a', 'b', 'c'])
    graph.insert(['a', 'b', 'z', 'a'])
    print(graph.root.following['b'].following['z'].following)
    #print(graph.search_data(graph.root, 'z'))
