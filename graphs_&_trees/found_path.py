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

    def __reset__(self, node):
        node.visited = False
        for key, value in node.following.items():
            print(key, value)
            if value.visited == True:
                self.__reset__(value)


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

    def search(self, data):
        item = []
        self._search_data(self.root, data, item.append)
        self.__reset__(self.root)
        if len(item) > 0:
            return item[0]
        else:
            return None

    def _search_data(self, node, data, visit):
        if node.data == data:
            visit(node)
            return
        node.visited = True
        for key, value in node.following.items():
            if value.visited == False:
                self._search_data(value, data, visit)

    def search_path(self, p1, p2):
        p1 = self.search(p1)
        p2 = self.search(p2)
        print(p1, p2)
        if p1 != None and p2 != None:
            item = []
            self._search_data(p1, p2.data, item.append)
            self.__reset__(self.root)
            if len(item) > 0:
                return True
            else:
                return False




if __name__ == '__main__':
    graph = Graph()
    graph.insert(['a', 'b', 'c'])
    graph.insert(['a', 'b', 'z', 'a'])
    print(graph.root.following['b'].following['z'].following)
    print(graph.search('b'))
    print(graph.search_path('z', 'a'))
