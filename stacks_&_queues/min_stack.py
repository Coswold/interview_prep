"""Q3.2"""

class MinStack(object):

    def __init__(self, iterable=None):
        self.stack = []
        self.min = None
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item):
        if self.min == None or item < self.min:
            self.min = item
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.min:
            self.min = self.stack[0]
            for i in self.stack:
                if i < self.min:
                    self.min = i
        return item

    def peek_min(self):
        return self.min

if __name__ == '__main__':
    stack = MinStack([5, 3, 6, 8, 1])
    print(stack.pop())
    print(stack.peek_min())
    stack.push(0.5)
    print(stack.peek_min())
