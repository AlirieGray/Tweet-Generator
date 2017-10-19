from linkedlist import LinkedList
from linkedlist import Node

class Queue(LinkedList):
    def __init__(self, iterable=None):
        super().__init__(iterable)

    def enqueue(self, item):
        """Add an object to the end of the Queue."""
        self.append(item)

    def dequeue(self):
        """Remove and return the object at the beginning of the Queue."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        temp = self.head.data
        self.head = self.head.next
        return temp

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from empty queue")
        return self.head.data

    def toTuple(self):
        q_list = []
        current = self.head
        while current:
            q_list.append(current.data)
            current = current.next
        return tuple(q_list)

if __name__ == '__main__':
    q = Queue(["Hello", "world,", "I", "am", "a", "queue!"])
    print(q.toTuple())
    while not q.is_empty():
        print(q.dequeue())
