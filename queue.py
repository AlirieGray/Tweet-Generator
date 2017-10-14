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

if __name__ == '__main__':
    Q = Queue(["Hello", "world,", "I", "am", "a", "queue!"])
    while not Q.is_empty():
        print(Q.dequeue())
