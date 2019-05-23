"""Q3.3"""

"""Stack that holds smallest items at the top"""
class SortStack(object):

    def __init__(self, iterable=None):
        self.s1 = []
        self.s2 = []
        if iterable:
            for item in iterable:
                self.push(item)

    def __sort__(self):
        while len(self.s1) > 0:
            temp = self.s1.pop()
            while len(self.s2) > 0 and self.s2[-1] > temp:
                self.s1.append(self.s2.pop())
            self.s2.append(temp)

        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

    def push(self, item):
        self.s1.append(item)
        self.__sort__()

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def is_empty(self):
        return len(self.s1) == 0


if __name__ == '__main__':
    stack = SortStack([5, 1, 8, 6, 10])
    print(stack.s1)
    print(stack.peek())
    stack.push(0.5)
    print(stack.peek())
    print(stack.pop())
    stack.push(7)
    print(stack.s1)
