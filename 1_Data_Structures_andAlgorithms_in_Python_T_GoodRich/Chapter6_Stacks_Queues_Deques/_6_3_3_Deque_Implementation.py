# customizing sequential objectics
# https://docs.python.org/3/reference/datamodel.html#emulating-container-types
# Implementing all the collection.deque ADTs
# 참고 : https://github.com/wdlcameron/Solutions-to-Data-Structures-and-Algorithms-in-Python/blob/master/Chapter%206%20Exercises.ipynb
#-------------P6-33-------------------
"""
We have to support the following methods:

len
appendleft
append
popleft
pop
D[0]
D[-1]
D[j]
D[j] = val
D.clear()
D.rotate(k)
D.remove(e)
D.count(e)
"""
import collections

class Deque(object):
    MAX_SIZE = 5

    def __init__(self, maxlen = None):
        self._data = [None]*Deque.MAX_SIZE
        self._size = 0
        self._front = 0
        self._maxlen = maxlen

    def is_empty(self):
        return self._size == 0

    # return the length of Q
    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0: index = self._size + index  # Negative indices
        if not 0 <= index < self._size: raise IndexError('Invalid index')
        return (self._data[(self._front + index) % len(self._data)])

    def __setitem__(self, index, value):
        if index < 0: index = self._size + index  # Negative indices
        if not 0 <= index < self._size: raise IndexError('Invalid index')
        self._data[(self._front + index) % len(self._data)] = value

    # add_first
    def appendleft(self,e):
        # if the Deque is full, resize the Deque
        if self._size == len(self._data): self.resize(len(self._data)*2)
        self._data[(self._front-1)%len(self._data)] = e
        self._front = (self._front - 1)%len(self._data)
        self._size = self._size + 1 if self._maxlen is None else min(self._size + 1, self._maxlen)

    # delete_first
    def popleft(self):
        # if the Deque is Empty
        assert not self.__len__() == 0, 'Deque is empty'
        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size <= len(self._data) // 4:
            self.resize(len(self._data)//2)
        return e

    # add_last
    def append(self, e):
        if self._size == len(self._data): self.resize(len(self._data)*2)
        self._data[(self._front+self._size)%len(self._data)] = e
        if self._maxlen is not None and self._size == self._maxlen :
            self._front = ( self._front + 1 ) % len(self._data)
        # Overwrite the previous first
        else: self._size += 1

    # delete_last
    def pop(self):
        # if Deque is Empty, raise Excpetion
        assert not self.__len__() == 0, 'Deque is empty'
        back = (self._front + self._size - 1) % len(self._data)
        e = self._data[back]
        self._data[back] = None
        self._size -= 1
        # if the length of the item is less than 1/4 of its initial Q, resize to half
        if 0 < self._size <= len(self._data) // 4:
            self.resize(len(self._data) // 2)
        return e

    def clear(self):
        self._data = [None] * len(self._data)
        self._size = 0
        self._front = 0

    # circulalry shift rightward k steps
    def rotate(self, k):
        assert not k < 0, 'Integer must be greater than 0'
        for _ in range(k):
            e = self.pop()
            self.appendleft(e)

    # count the number of matches
    def count(self, e):
        assert not self.__len__() == 0, 'Deque is empty'
        cnt = 0
        for i in range(self._size):
            value = self.pop()
            if value == e: cnt += 1
            self.appendleft(value)
        return cnt

    def resize(self, new_size):
        if self._maxlen is not None: new_size = min(new_size, self._maxlen)
        old_data = self._data
        self._data = [None]*new_size
        for i in range(self._size):
            self._data[i] = old_data[self._front]
            self._front = (self._front + 1) % len(old_data)
        self._front = 0

    def remove(self, e):
        assert not self.__len__() == 0, 'Deque is empty'
        found = False
        for i in range(self._size):
            value = self.pop()
            if value == e and not found :
                found = True
            else: self.appendleft(value)
        return found

    def display(self):
        print(self._data)


def main():
    D = Deque()

    print('Adding last')
    for i in range(15):
        D.append(i)
        print(i, D._data)

    print('\nDelete 9', D.remove(9), D._data, D._front)

    D.clear()
    print('\nCleared Data:', D._data)

    for i in range(15):
        D.append(i % 3)

    print('\nFound', D.count(2), '2s in ', D._data)

    print('\nAdding first')
    for i in range(20, 10, -1):
        D.appendleft(i)
        print(i, D._data)

    print(D._front)

    print('\nRotating')
    for i in range(20):
        D.rotate(1)
        print('Front is:', D[0])

    print('\nPerforming the removals')
    while True:
        D.display()
        if not D.is_empty():
            print('Remove first', D[0], D.popleft(), end=' ')
        if not D.is_empty():
            print('Remove last', D[-1], D.pop())
        else:
            return

main()

