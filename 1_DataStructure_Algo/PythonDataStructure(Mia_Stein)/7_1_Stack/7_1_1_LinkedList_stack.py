##############
# Stack ADT ##
############################
# 시간 복잡도 : O(1)
# Last In First Out (선입선출)
############################
# empty : 스택이 비었는 지 확인
# push : 맨 끝에 데이터 삽입
# pop : 스택 마지막 값 제거, 반환
# top / peek : 마지막 값 확인
# size : 스택 사이즈 확인

class StackNode(object) :
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack(object) :
    # Creates an empty stack
    def __init__(self):
        self.top = None
        self._size = 0

    # Returns True if the Stack is empty otherwise False
    def isEmpty(self):
        return self.top is None

    def size(self):
        return self._size

    def push(self, item):
        # Creates a Node and set it to the top
        self.top = StackNode(item, self.top)
        self._size += 1

    def pop(self):
        # Removes and returns the top item on the Stack
        assert not self.isEmpty(), 'Cannot pop from an Empty Stack'
        node = self.top
        self.top = self.top.next
        self._size -= 1
        return node.item

    def peek(self):
        assert not self.isEmpty(), 'Cannot peek from an Empty Stack'
        return self.top.item

    def size(self):
        return self._size

    def printStack(self):
        node = self.top
        while node :
            print(node.item, end=' ')
            node = node.next
        print()

if __name__ == '__main__':
    stack = Stack()
    print('is Stack Empty? : {0}'.format(stack.isEmpty()))
    print('pushing 1~9..')
    for i in range(10) :
        stack.push(i)
    stack.printStack()
    print('Peek : {0}'.format(stack.peek()))
    print('pop : {0}'.format(stack.pop()))
    print('Peek : {0}'.format(stack.peek()))
    print('size : {0}'.format(stack.size()))




