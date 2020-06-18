'''
A Round-Robin scheduler can be implemented with th general queue ADT,
by repeatedly performing the following steps on queue Q
1. e = Q.dequeue()
2. Service element e
3. Q.enequeue(e)
'''

class CircularQueue(object):
    '''Queue implementation using circularly linked list for storage'''

    class _Node(object):
        """ Lightweight, nonpublic class for stroing a singly linked node """
        __slots__ = '_element', '_next'            # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty queue'''
        self._tail = None           # Represent the tail of queue
        self._size = 0              # # of queue elements

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size

    def is_empty(self):
        '''return True if the queue is empty'''
        return self._size == 0

    def first(self):
        '''
        return the element at the front of the queue
        Raise Empty exceptinon if the queue is empty
        '''
        assert not self.is_empty(), 'Queue is empty'
        head = self._tail._next
        return head._element

    def dequeue(self):
        '''
        Remove and return the first element of the queue
        Raise Empty exceptinon if the queue is empty
        '''
        assert not self.is_empty(), 'Queue is empty'
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        '''
        Rotate front element to the back of the queue
        Chapter 7.2.1 Round-Robin Scheduler can be efficiently implemnted using this function
        '''
        if self._size > 0:
            self._tail = self._tail._next