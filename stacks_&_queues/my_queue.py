"""Q3.3"""

class MyQueue(object):

    def __init__(self, iterable=None):
        self.new_stack = []
        self.old_stack = []
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __is_empty__(self):
        return len(self.new_stack) == 0

    def __shift_stack__(self):
        while self.__is_empty__() == False:
            self.old_stack.append(self.new_stack.pop())

    def enqueue(self, item):
        self.new_stack.append(item)

    def dequeue(self):
        self.__shift_stack__()
        if len(self.old_stack) > 0:
            return self.old_stack.pop()
        return None

    def peek(self):
        self.__shift_stack__()
        return self.old_stack[-1]


if __name__ == '__main__':
    queue = MyQueue([1, 2, 3, 4])
    print(queue.old_stack)
    print(queue.new_stack)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.old_stack)
    print(queue.new_stack)
    queue.enqueue(8)
    print(queue.old_stack)
    print(queue.new_stack)
