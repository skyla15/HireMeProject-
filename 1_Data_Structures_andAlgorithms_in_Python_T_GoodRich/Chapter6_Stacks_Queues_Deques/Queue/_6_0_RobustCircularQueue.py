class ArrayQeueue(object):
    '''FIFO queue implementation using a Python list as underlying storage'''

    DEFAULT_CAPACITY = 10   # initial capacity

    def __init__(self):
        '''Create an empty queue'''
        self._data = [None] * ArrayQeueue.DEFAULT_CAPACITY # O(n)
        self._size = 0      # the # of e in Q
        self._front = 0     # front index

    # override __len__ method
    def __len__(self):
        return self._size

    def is_empty(self):
        '''return True if Q is empty'''
        return self._size == 0

    def first(self):
        '''
            return the element at the front of the Q
            raise Empty exception if the q is empty
        '''

        assert not self.is_empty(), 'Q is empty'
        return self._data[self._front]

    def dequeue(self):
        '''
            remove and return the element at the front
            raise exeption if q is empty
        '''
        assert not self.is_empty(), 'Q is empty'
        e = self._data[self._front]
        self._data[self._front] = None          # Help garbage collection
        self._front = (self._front + 1) % len   # advance the front to the next index
        self._size -= 1
        return e

    def enqueue(self, e):
        '''add an element to the back of queue'''
        if self._size == len(self._data):       # if the existing q is full, double the size
            self._resize( 2*len(self._data))
        tail = (self._front + self._size) % len(self._data)
                                                # get the next available index
        self._data[tail] = e                    # add an element
        self._size += 1                         # increase the size of the q

    def _resize(self, wrapover):
        '''resize a new list of capacity'''
        old_data = self._data           # Keeping the existing q
        self._data = [None]*wrapover    # Double the size of the existing q
        for k in range(self._size):     # Reassign the xisting q to the double-sized q
            self._data[k] = old_data[self._front]
            temp_front = (self.front + 1) % len(old_data)
        self._front = 0                 # front is realigned

