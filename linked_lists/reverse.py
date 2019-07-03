class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def reverse(self):
        current = self.head
        last = None
        while current != None:
            next = current.next
            current.next = last
            last = current
            current = next
        self.setHead(last)


if __name__ == '__main__':
    node = Node()
    node.data = 1
    node.next = Node()
    node.next.setData(2)
    node.next.next = Node()
    node.next.next.setData(3)
    lst = SinglyLinkedList()
    lst.setHead(node)
    lst.reverse()
    current = lst.head
    while current != None:
        print(current.data)
        current = current.next
    lst.reverse()
    current = lst.head
    while current != None:
        print(current.data)
        current = current.next

