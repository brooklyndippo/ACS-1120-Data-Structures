#!python

from mimetypes import init
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        bucket_index =  hash(key) % len(self.buckets)
        # print(bucket_index)
        return bucket_index

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, val in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                # print (f'key: {key}')
                # print (f'value: {value}')
                all_values.append(value)
        return all_values
        # TODO: Collect all values in each bucket

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            items = bucket.items()
            for item in items:
                item = tuple(item)
                all_items.append(item)
            #all_items.extend(tuple(bucket.items()))
            #print(all_items)
        return all_items

    def length(self):
        count = 0
        for bucket in self.buckets:
            for item in bucket.items():
                count += 1
        return count
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)

        if entry:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # 1: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        
        #2a:  entry = bucket.find_if_matches(matches_key)
        # TODO: Check if key-value entry exists in bucket  #use find_if_matches code
        #anonymous function with no name ==> callback function! (marco/polo)
        #lets us go through all of the bucket entries & for each entry and find key within scope of get
        #2: Check if key-value entry exists in bucket. 
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)

        #3: If found, return value associated with given key.
        if entry is not None:
            value = entry[1]
            return value
        else:
            raise KeyError('Key not found: {}'.format(key))
        
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # print(index)
        # print(bucket)
        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)
        # print(entry)
        # TODO: If found, update value associated with given key
        if entry:
            bucket.update(key, value)
        else:
            #print('not cool')
            bucket.append([key, value])
            #print(bucket.head)
        # TODO: Otherwise, insert given key-value entry into bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # TODO: Check if key-value entry exists in bucket
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)

        # TODO: If found, delete entry associated with given key
        if entry:
            bucket.delete(entry)
        else:
            #print('not cool')
            raise KeyError('Key not found: {}'.format(key))
        #  TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

if __name__ == '__main__':
    ht = HashTable()
    print('hash table: {}'.format(ht))