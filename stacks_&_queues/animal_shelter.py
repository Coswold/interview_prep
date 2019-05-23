"""Q3.6"""

class AnimalSort(object):

    def __init__(self, iterable=None):
        self.animals = []
        if iterable:
            for item in iterable:
                if item == 'Cat' or item == 'Dog':
                    self.enqueue(item)

    def enqueue(self, item):
        self.animals.append(item)

    def dequeue_any(self):
        if len(self.animals) > 0:
            return self.animals.pop(0)

    def dequeue_dog(self):
        i = 0
        while i < len(self.animals):
            if self.animals[i] == 'Dog':
                return self.animals.pop(i)
            i += 1

        return None

    def dequeue_cat(self):
        i = 0
        while i < len(self.animals):
            if self.animals[i] == 'Cat':
                return self.animals.pop(i)
            i += 1

        return None


if __name__ == '__main__':
    stack = AnimalSort(['Cat', 'Cat', 'Dog', 'Dog', 'Cat'])
    print(stack.animals)
    print(stack.dequeue_dog())
    print(stack.animals)
