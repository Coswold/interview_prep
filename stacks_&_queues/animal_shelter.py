"""Q3.6"""

"""First implementation"""
# class AnimalSort(object):
#
#     def __init__(self, iterable=None):
#         self.animals = []
#         if iterable:
#             for item in iterable:
#                 if item == 'Cat' or item == 'Dog':
#                     self.enqueue(item)
#
#     def enqueue(self, item):
#         self.animals.append(item)
#
#     def dequeue_any(self):
#         if len(self.animals) > 0:
#             return self.animals.pop(0)
#
#     def dequeue_dog(self):
#         i = 0
#         while i < len(self.animals):
#             if self.animals[i] == 'Dog':
#                 return self.animals.pop(i)
#             i += 1
#
#         return None
#
#     def dequeue_cat(self):
#         i = 0
#         while i < len(self.animals):
#             if self.animals[i] == 'Cat':
#                 return self.animals.pop(i)
#             i += 1
#
#         return None

"""Second implementation"""
class Animal(object):

    def __init__(self, name, species):
        self.name = name
        self.order = 0
        if species == 1:
            self.species = 'Dog'
        else:
            self.species = 'Cat'


class AnimalQueue(object):

    def __init__(self, animals=None):
        self.dogs = []
        self.cats = []
        self.order = 0
        if animals:
            for animal in animals:
                self.enqueue(animal)

    def peek(self):
        if self.dogs[0].order < self.cats[0].order:
            return self.dogs[0]
        else:
            return self.cats[0]

    def enqueue(self, animal):
        animal = Animal(animal[0], animal[1])
        animal.order = self.order
        self.order += 1
        if animal.species == 'Dog':
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeue_any(self):
        animal = self.peek()
        if animal.species == 'Cat':
            return self.cats.pop(0)
        else:
            return self.dogs.pop(0)

    def dequeue_dog(self):
        return self.dogs.pop(0)

    def dequeue_cat(self):
        return self.cats.pop(0)


if __name__ == '__main__':
    Queue = AnimalQueue([('Bob', 1), ('Maggie', 1), ('Jake', 0), ('Ace', 1), ('Fred', 0)])
    print(Queue.peek().name)
    print(Queue.dequeue_dog().name)
    print(Queue.dequeue_any().name)
