"""Q3.3"""

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

    def pop_substack(self, stack_i):
        if self.stacks[stack_i]:
            item = self.stacks[stack_i].pop()
        if len(self.stacks[stack_i]) == 0:
            self.stacks.pop(stack_i)
        return item


if __name__ == '__main__':
    stack = SetOfStacks(4, [5, 3, 6, 8, 1, 16, 8, 10, 22, 29, 16, 44])
    print(stack.stacks)
    stack.push(39)
    print(stack.pop_substack(1))
    print(stack.pop_substack(1))
    print(stack.pop_substack(1))
    print(stack.pop_substack(1))
    print(stack.stacks)
