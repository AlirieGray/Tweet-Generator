from linkedlist import LinkedList
from linkedlist import Node

class Queue(LinkedList):
    def __init__(self, iterable=None):
        super().__init__(iterable);

    def enqueue(item):
        """Adds an object to the end of the Queue."""
        self.append(item);

    def dequeue(item):
        """ Removes and returns the object at the beginning of the Queue."""
        temp = self.tail;
        self.delete(self.tail);
        return temp;


if __name__ == '__main__':
    Q = Queue(["Hello", "world,", "I", "am", "a", "queue!"])
    for i in Q.iterate():
        print(i.data)
