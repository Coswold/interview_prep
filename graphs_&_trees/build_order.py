class DNode(object):
    def __init__(p):
        self.prj = p
        self.dep = []

class DTree(object):

    def __init__(projects=None, dep=None):
        self.root = None
        if dep:
            self.insert(dep)

    def insert(dep):
        for d in dep:
            if self.root == None:
                self.root = DNode(d[0])
                self.root.dep.append(DNode(d[1]))
            elif self.root.prj == d[1]:
                new = DNode(d[0])
                new.dep.append(self.root)
                self.root = new
            else:





if __name__ == '__main__':
    buildOrder(projects, dependencies)
