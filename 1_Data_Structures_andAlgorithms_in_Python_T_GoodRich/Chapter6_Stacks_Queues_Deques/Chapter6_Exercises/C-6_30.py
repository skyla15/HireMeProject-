# customizing sequential objectics
# https://docs.python.org/3/reference/datamodel.html#emulating-container-types

import random as r

class Deque(object):
    MAX_SIZE = 5

    def __init__(self):
        self._data = [None]*Deque.MAX_SIZE
        self._size = 0
        self._front = 0

    # return the length of Q
    def __len__(self):
        return len(self._data)

    # first
    def __getitem__(self, idx):
        assert not self.__len__() == 0, 'Deque is empty'
        back = (self._front + self._size) % len(self._data)
        if idx >= 0:
            idx = ( idx + self._front - 1) % len(self._data)
        elif idx < 0:
            back = back + idx
            print('back: ', back)

        if self._data[idx] == None:
            raise IndexError('IndexOutOfBounds')

        return self._data[idx]

    def __setitem__(self, idx, e):
        idx = ( idx + self._front -1 ) % len(self._data)
        self._data[idx] = e

        #TODO if the index is out of bounds, raise Error

    # add_first
    def appendleft(self,e):
        # if the Deque is full, resize the Deque
        if self._size == len(self._data):
            self.resize(len(self._data)*2)
        # if the Deque is not empty, move the front an index ahead
        if self.__len__() != 0:
            self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

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
        if self._size == len(self._data):
            self.resize(len(self._data)*2)
        back = (self._front + self._size) % len(self._data)
        self._data[back] = e
        self._size += 1

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

    # circulalry shift rightward k steps
    def rotate(self, k):
        assert not k < 0, 'Integer must be greater than 0'
        old_data = self._data
        self.clear()
        shift_front = ( self._front + k ) % len(self._data)
        temp_front = self._front
        for i in range(self._size):
            self._data[shift_front] = old_data[temp_front]
            shift_front = (shift_front + 1) % len(self._data)
            temp_front = (temp_front + 1) % len(self._data)

        self._front = (self._front + k) % len(self._data)


    # count the number of matches for
    def count(self, e):
        assert not self.__len__() == 0, 'Deque is empty'
        temp_front = self._front
        cnt = 0
        for i in range(self._size):
            if(self._data[temp_front] == e):
                cnt += 1
            temp_front = (temp_front + 1) % len(self._data)
        return cnt

    def resize(self, new_size):
        old_data = self._data
        self._data = [None]*new_size
        for i in range(self._size):
            self._data[i] = old_data[self._front]
            self._front = (self._front + 1) % len(old_data)
        self._front = 0

    def display(self):
        print(self._data)


def main():
    print('main')
    D = Deque()
    D.append(1)
    D.display()
    D.append(2)
    D.display()
    D.appendleft(3)
    D.display()
    D.appendleft(4)
    D.display()
    D.appendleft(5)
    D.display()
    D.appendleft(6)
    D.display()
    D.appendleft(7)
    D.display()
    D.appendleft(8)
    D.display()

    print()
    print('rotate')
    D.rotate(4)
    D.display()
    print()

    print(D.popleft())
    D.display()
    print(D.popleft())
    D.display()
    print(D.popleft())
    D.display()
    print(D.popleft())
    D.display()
    print(D.popleft())
    D.display()
    print(D.pop())
    D.display()
    print(D.pop())
    D.display()
    print(D.pop())
    D.display()

    print('len : ', len(D))
    D[1] = 1234
    print('D[1] = 1234', D[1])
    D.display()
    print('front : ', D._front, 'size : ', D._size)
    print('D[-1]', D[-1])
    print('clear')
    D.clear()
    D.display()

main()

