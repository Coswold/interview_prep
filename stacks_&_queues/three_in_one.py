"""Q3.1"""

class MultiStack(object):

    def __init__(self, size=1, count=3):
        self.stack_capacity = size
        self.sizes = [0] * count
        self.values = [None] * size * count

    def __repr__(self):
        string = ""
        i = 0
        while i < len(self.sizes):
            string += 'Stack{}({} items, top={})\n'.format(i, self.sizes[i], self.peek(i))
            i += 1
        return string

    def __index_of_top__(self, stack_num):
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        if size == 0:
            size = 1
        return offset + size - 1

    def push(self, stack_num, value):
        if self.is_full(stack_num) == True:
            raise ValueError('Stack is full')
        else:
            self.sizes[stack_num] += 1
            self.values[self.__index_of_top__(stack_num)] = value

    def pop(self, stack_num):
        if self.is_empty(stack_num) == True:
            raise ValueError('Stack is empty')
        else:
            top = self.__index_of_top__(stack_num)
            value = self.values[top]
            self.values[top] = None
            self.sizes[stack_num] -= 1
            return value

    def peek(self, stack_num):
        return self.values[self.__index_of_top__(stack_num)]

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0


if __name__ == '__main__':
    stack = MultiStack(2, 4)
    stack.push(0, 'hello')
    stack.push(1, 'there')
    stack.push(3, 'wow')
    print(stack)
    print(stack.pop(1))
    print(stack.values)
