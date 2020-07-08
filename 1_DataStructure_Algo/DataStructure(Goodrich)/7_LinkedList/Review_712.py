
'''
node  -(next)->  node  -(next)-> node
head                            tail
tail
'''


class LinkedQueue(object):
    class _Node(object):
        __slots__ = '_element', '_next'

        def __init__(self, element, next = None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, element):
        new_node = self._Node(element)
        if self.is_empty():
            self._head = new_node
        else:
            # link previous node to the new node
            # if empty, link the first node to the next node
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        assert not self.is_empty(), 'Queue is Empty'
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._head._element

    def display(self):
        temp = self._head
        while temp != None:
            print(temp._element)
            temp = temp._next


q = LinkedQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()
print('first : ', q.first())
print('dequeue : ', q.dequeue())
q.display()


