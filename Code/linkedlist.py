#!python

from operator import index


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        length = 0
        node = self.head
        while node is not None:    #while node: does the same thing!
            length += 1
            node = node.next
        return length
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each


    def append(self, item):
        new_node = Node(item)
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail


    def prepend(self, item):
        new_node = Node(item)
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists

    def find(self, item):

        node = self.head
        while node is not None:    #while node: does the same thing!
            if node.data == item:
                return True
            node = node.next
        return False
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False

    def find_if_matches(self, matching_function):
    #Return an item from this linked list if it is present.
        node = self.head
        while node is not None:     #while node: does the same thing!
            if matching_function(node.data): 
                return node.data
            node = node.next
        return None 

    def update(self, key, new_data):
        node = self.head
        while node:
            if key == node.data[0]:
                node.data[1] = new_data
            node = node.next

    def delete(self, item):

        if self.is_empty == True or self.find(item) == False:   #n
            raise ValueError('Item not found: {}'.format(item))

        elif self.head.data == item and self.tail.data == item:
            self.head = None
            self.tail = None

        elif self.head.data == item:
            new_head = self.head.next
            self.head = new_head

        elif self.tail.data == item:
            node = self.head
            new_tail = node
            while node.next is not self.tail:      #n
                node = node.next
                new_tail = node
            self.tail = new_tail
            self.tail.next = None

        else:
            node = self.head 
            current_node = node

            while node is not None and node.data is not item:
                current_node = node
                print(f'current node: {current_node}')
                node = node.next                 #n
                print(f'node match :{node}')
                reroute_to = node.next
                print(f'reroute_to: {reroute_to}')

            current_node.next = reroute_to
            
            

        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)
    print(my_ll.head)
    print(my_ll.tail)

    


