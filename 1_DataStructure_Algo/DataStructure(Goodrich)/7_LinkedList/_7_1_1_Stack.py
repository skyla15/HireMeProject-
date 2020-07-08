'''
Stack
1. Locate the top of the stack at the head : Better efficiency
2. __slots__ in nested Node class is to streamline the memory usage
'''
'''
The use of a nested class : the nested class exists for support of the outer class.
furthermore, it can help reduce potential name conflicts as it allows for a similarly named class to exist in another context..
Also it allows for a more advanced form of inheritance in which a subclass of the outer class overrieds the 
definition of its nested class  
'''

class LinkedStack(object):
    """ LIFO Stack Implementation using a singly linked list """

    class _Node(object):
        """ Lightweight, nonpublic class for stroing a singly linked node """
        __slots__ = '_element', '_next'            # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None       # the new node is added to the head
                                # when deqeueud, the deqeue also occurs at the head of the list
        self._size = 0          # number of stack elements

    def __len__(self):
        """
            Return the number of elements in the stack
            Overwrite the __len__() method
        """
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add an element e to the 'TOP' of the stack."""
        new_node = self._Node(e, self._head)      # create a new node
        self._head = new_node                     # put the new node at the front of the queue
        self._size += 1

    def top(self):
        """
            Return the element at the top of the stack
            Raise Empty exception if the stack is empty
        """
        assert not self.is_empty(), 'Stack is empty'
        return self._head._element                  # _head 노드의 _element 반환

    def pop(self):
        """
            Remove and return the element from the top of the stack (LIFO)
            Raise Empty exception if the stack is empty
        """
        assert not self.is_empty(), 'Stack is empty'
        answer = self._head._element
        self._head = self._head._next               # 헤드를 다음 노드로 넘겨줌 ( bypass the former top node )
        self._size -= 1
        return answer


    def display(self):
        temp = self._head
        while not temp._next != None:
            print(temp.element)
            temp = temp._next

