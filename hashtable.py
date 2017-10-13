#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        all_vals = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_vals.append(value)
        return all_vals

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        # store a list of the items to be returned
        all_items = []
        # loop through each bucket in the list of buckets (O(n) for n buckets)
        for bucket in self.buckets:
            # add each item in the bucket to the list to be returned (O(m) for m items in bucket)
            all_items.extend(bucket.items())
        # O(N) for N total items
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # store a variable to keep track of the running count (contant time)
        count = 0
        # loop through the entire list of buckets (O(n) in all cases for n buckets)
        for bucket in self.buckets:
            # start at the head of the current bucket and loop through the entire bucket
            # O(m) in all cases for m items in bucket
            current = bucket.head
            while (current):
                count += 1
                current = current.next
        # total runtime: O(N) for N items in hash table
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # use the hash to find the index of the bucket
        # and store that bucket (constant time)
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]
        # use the linked list find function to find the key in the list
        # worst case: O(n) (item is at the end of the list)
        # best case: O(1) (item is at the head of the list)
        if(bucket.find(lambda item: item[0] == key)):
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # use the hash to find the index of the bucket
        # and store that bucket (constant time)
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]
        # use the linked list find function to find the key in the list
        # and store it
        # worst case: O(n) (item is at the end of the list)
        # best case: O(1) (item is at the head of the list)
        found = bucket.find(lambda item: item[0] == key)
        if not found:
            raise KeyError("Key not present")
            return
        # return the found value (constant time)
        return found[1]

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # get bucket index
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]
        # first check if the item is already in the bucket by looping through
        # starting at the head node
        current = bucket.head
        while (current):
            # if the item is already in the bucket, update the value with a new tuple
            # worst case: O(n) (item is at the end of the list)
            # best case: O(1) (item is at the head of the list)
            if current.data[0] == key:
                current.data = (key, value)
                return
            current = current.next
        # otherwise, add the new tuple using the linked list append function
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # hash the key to find its index in the list of buckets and store
        # the bucket at that index
        bucketIndex = self._bucket_index(key)
        bucket = self.buckets[bucketIndex]
        # use the linked list find function to find the key in the bucket
        # by iterating through
        # worst case: O(n) (item is at the end of the list)
        # best case: O(1) (item is at the head of the list)
        found = bucket.find(lambda item: item[0] == key)
        # if the key is not present, throw a KeyError
        if not found:
            raise KeyError("Key not present")
        # otherwise, use the linked list delete method to remove the item
        else:
            val = found[1]
            bucket.delete((key, val))

def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    # print('Deleting entries:')
    # ht.delete('I')
    # print(ht)
    # ht.delete('V')
    # print(ht)
    # ht.delete('X')
    # print(ht)
    # print('contains(X): ' + str(ht.contains('X')))
    # print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
