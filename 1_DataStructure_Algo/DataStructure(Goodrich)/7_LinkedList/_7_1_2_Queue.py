"""
7.1.2. Implementing a Queue with a Singly Linked List
- Worst-case O(1) time for all operations.
- Need to use _head & _tail reference as instance variables to perform operations on the both ends
"""

class LinkedQueue(object):
    "FIFO queue implementation using a singly linked list for storage"

    class _Node:
        "Lightweight, nonpublic class for storing a singly linked node"
        __slots__ = '_element', '_next'            # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue"""
        self._head = None       # when dequeued, the head is dequeued
        self._tail = None       # new_node is added to the tail
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty"""
        return self._size == 0

    def first(self):
        """Return the element at the front of the queue"""
        assert not self.is_empty(), 'Queue is empty'
        return self._head._element

    def enqueue(self, e):
        """Add an element to the back of queue"""
        new_node = self._Node(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Return the first element of the queue"""
        assert not self.is_empty(), 'Queue is empty'
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def display(self):
        temp = self._tail
        while temp != None:
            print(temp._element)
            temp = temp._next

q = LinkedQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()