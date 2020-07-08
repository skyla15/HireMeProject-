
'''
node <-(next)- node <-(next)- node  <-(next)- new_node
                                             self._head
'''

class LinkedStack(object):
    class _Node(object):
        __slots__ = '_element', '_next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, element):
        new_node = self._Node(element, self._head)
        self._head = new_node
        self._size += 1

    def pop(self):
        assert not self.is_empty(), 'Stack is Empty'
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e

    def is_empty(self):
        return self._size == 0

    def top(self):
        return self._head._element

    def display(self):
        temp = self._head
        while temp != None:
            print(temp._element)
            temp = temp._next

def stack_main():
    s = LinkedStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.display()



stack_main()

