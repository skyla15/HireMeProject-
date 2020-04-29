class ArrayStack(object):
    '''LIFO Stack implementation using a Python list as underlying storage'''

    def __init__(self):
        '''Create an empty stack'''
        self._data = []         # nonpublic list instance ( explicitly protected declaration )

    def __len__(self):
        '''
            Adapter Design : 리스트 클래스의 len 메소드 재정의
        '''
        return len(self._data)

    def is_empty(self):
        '''Return True if empty'''
        return len(self._data) == 0

    def push(self,e):
        '''
            Add element to the end of the list
            Add element to the top of the Stack
        '''
        self._data.append(e)

    def top(self):
        '''
            Return and the element at the top of the stack
            Raise Empty exception if the stack is empty
        '''
        if self.is_empty():
           raise Exception('Stack is Empty')
        return self._data[-1]

    def pop(self):
        '''
            Return and Remove the element at the top of the stack
            Raise Empty exception if the stack is empty
        '''
        if self.is_empty():
            raise Exception('Stack is Empty')
        return self._data.pop()


