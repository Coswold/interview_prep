from linked_list import LinkedList

class Circular_Buffer(object):

    def __init__(self, data=None):
        self.buffer = LinkedList()
        self.size = 0
        for i in range(0, 8):
            self.buffer.append(None)
        self.buffer.tail.next = self.buffer.head

        if data != None:
            for i in data:
                self.insert(i)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def items(self):
        items = []
        current = self.buffer.head
        while current.next != self.buffer.tail:
            items.append(current.data)
            current = current.next
        return items

    def insert(self, data):
        current = self.buffer.head
        current.data = data
        self.buffer.head = current.next
        self.buffer.tail = self.buffer.tail.next
        self.buffer.tail.next = self.buffer.head
        if self.size < 8:
            self.size += 1

    def delete(self):
        temp = self.buffer.tail.data
        self.buffer.tail.data = None
        self.buffer.tail = self.buffer.tail.next
        self.size -= 1
        return temp


if __name__ == '__main__':
    ll = Circular_Buffer()
    ll.insert(8)
    ll.insert("hello")
    print(ll)
