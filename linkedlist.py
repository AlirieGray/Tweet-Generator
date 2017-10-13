#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def hasNext(self):
        """Returns true if the node has a node after it, false otherwise"""
        return (not (self.next is None))

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):
    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None: # O(n)
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # store the running count in a variable (constant time)
        count = 0
        # constant time to check if the head node is null
        if self.is_empty():
            return count
        # start at the head node and iterate through the list
        # O(n) time is all cases because we always go through the whole list
        current = self.head
        while (current):
            current = current.next
            # keep track of how many nodes we have touched
            count += 1
        # and return the count (constant time)
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # if the list is empty, make a new node to be both the head and tail
        # constant time
        newNode = Node(item)
        if not self.head:
            self.head = newNode
        else:
            # otherwise, have the tail point to the new node
            # and the new node becomes the new tail
            # constant time
            self.tail.next = newNode
        self.tail = newNode

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # create a new node (constant time)
        newNode = Node(item)
        # change the pointer of the new node to point to the old head (constant time)
        newNode.next = self.head
        # and reassign the head pointer to the new node (constant time)
        self.head = newNode
        # if the list was previously empty, (has no tail pointer)
        # then assign the tail pointer to be the new node (constant time)
        if not self.tail:
            self.tail = self.head

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # store a boolean to keep track of whether the item is in the list
        # (constant time)
        found = False

        # if the list is empty, exit the function (constant time to check head node)
        if self.head is None:
            raise ValueError("List is empty");
            return

        # if the head is the item we are looking for, reassign the head pointer
        if self.head.data == item:
            found = True
            # if the item we are removing is the only item in the list
            # that is, if the head and tail point to the same node
            # then set the head and tail pointers to null (constant time)
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            # otherwise if the head is the node we are removing but it is not
            # the only node in the list, reassign the head pointer to be the
            # node that follows it (constant time)
            self.head = self.head.next

        # starting w/ the head, loop through the entire list until we reach
        # a node that does not have a next node (which will be the tail)
        # O(n) in all cases
        current = self.head
        while current.hasNext():
            # check if the node after the current node contains the data we are
            # trying to remove (constant time to compare data)
            if current.next.data == item:
                found = True
                # if the found node is the tail, reassign the tail pointer
                # constant time to reassign pointer
                if current.next is self.tail:
                    self.tail = current
                    current.next = None
                    break
                # if we reach the item, remove it by changing the pointer behind
                # it to point in front of it, and continue (constant time)
                else:
                    current.next = current.next.next
            current = current.next
        if not found:
            raise ValueError("Item not in list!")

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # otherwise, start at the head node and iterate through
        # worst case: O(n) (item is at end of list)
        # best case: O(1) (item is at head of list)
        current = self.head
        while current:
            if quality(current.data):
                return current.data
            current = current.next

    def iterate(self):
        """Iterates from the head of the list"""
        current = self.head
        while current:
            yield current
            current = current.next

    def getElementAt(self, index):
        """Returns the data at a specific index"""
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('second element: ' + str(ll.head.next))
    print('third element (tail): ' + str(ll.head.next.next))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))

    for i in ll.iterate():
        print("Iterating " + i.data)

    # Enable this after implementing delete:
    print('Deleting items:')
    ll.delete('B')
    print('deleted B')
    print(ll)
    ll.delete('C')
    print('deleted C')
    print(ll)
    ll.delete('A')
    print('deleted A')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()
