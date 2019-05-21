class SetOfStacks(object):

    def __init__(self, cap=4, iterable=None):
        self.stacks = [[]]
        self.cap = cap
        self.current = 0
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, item):
        if len(self.stacks[self.current]) >= self.cap:
            self.stacks.append([])
            self.current += 1
        self.stacks[self.current].append(item)

    def pop(self):
        item = self.stacks[self.current].pop()
        if len(self.stacks[self.current]) == 0:
            self.stacks.pop()
            self.current -= 1
        return item


if __name__ == '__main__':
    stack = SetOfStacks(4, [5, 3, 6, 8, 1, 8])
    print(stack.stacks)
    print(stack.pop())
    stack.push(0.5)
