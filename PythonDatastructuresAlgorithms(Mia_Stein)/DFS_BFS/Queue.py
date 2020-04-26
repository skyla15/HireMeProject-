class CircularQueue:
    def __init__(self, MAX_SIZE):
        self.q = [None]*MAX_SIZE
        self.front = 0
        self.rear = 0
        self.MAX_SIZE = MAX_SIZE

    def enqueue(self, item):
        assert not self.isFull, print('Circular Queue Full')
        self.rear = ( self.rear + 1 ) % self.MAX_SIZE
        self.q[self.rear] = item

    def isFull(self):
        return self.rear+1 == self.front

    def dequeue(self):
        assert not self.isEmpty(), print('Circular Queue Empty')
        self.front = ( self.front + 1 ) % self.MAX_SIZE
        return self.q[self.front]

    def display(self):
        displayL = []
        if self.rear > self.front :
            displayL = self.q[self.front+1:self.rear+1]
        elif self.rear < self.front :
            displayL = self.q[0:self.rear+1] + self.q[self.front+1:]

        print(displayL)

    def size(self):
        assert not self.isEmpty(), print('Circular Queue Empty')
        # 모듈러 연산
        return (self.rear - self.front + self.MAX_SIZE) % self.MAX_SIZE
        #   f           r
        #     X X X X X X
        # 0 1 2 3 4 5 6 7 8

        #       r     f
        # X X X X       X X
        # 0 1 2 3 4 5 6 7 8

    def peek(self):
        assert not self.isEmpty(), print('Circular Queue Empty')
        return self.q[self.front+1]

    def isEmpty(self):
        return self.front == self.rear



class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def front_enqueue(self, item):
        assert not self.isFull(), print('CircularDeque Full')
        self.q[self.front] = item
        # 모듈러 연산
        self.front = ( self.front - 1 + self.MAX_SIZE ) % self.MAX_SIZE

    def rear_dequeue(self):
        assert not self.isEmpty(), print('queue Empty')
        item = self.q[self.rear]
        self.rear = ( self.rear - 1 ) % self.MAX_SIZE
        return item

    def rear_peek(self):
        return self.q[self.rear]



# List 한개 사용
# insert 시 O(n)
class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0, item)

    def dequeue(self):
        assert not self.isEmpty(), print('Circular Queue Empty')
        return self.q.pop()

    def size(self):
        assert not self.isEmpty(), print('Circular Queue Empty')
        return len(self.q)

    def peek(self):
        return self.q[-1]

    def isEmpty(self):
        return not bool(self.q)


# 스택 2개 사용
# 삽입 시 빠른 삽입이 가능해짐
# 하지만 삭제 시 O(n)
class DoubleListQueue:
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def transfer(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

    def enqueue(self, item):
        self.inStack.append(item)

    def dequeue(self):
        if self.isEmpty() :
            print('Empty')
            return
        if not self.outStack : # outStack 이 비었다면
            self.transfer()
        if self.outStack:
            return self.outStack.pop()

    def isEmpty(self):
        return self.outStack or self.inStack

    def peek(self):
        if self.isEmpty() :
            print('Empty')
            return
        if self.outStack :
            self.transfer()
        if self.outStack :
            return self.outStack[-1]


class LinkedQueue:
    def __init__(self):
        self.tail = None
        self.front = None
        self.size = 0

    def enqueue(self, item):
        node = Node(item)
        if not self.front:      # 첫 노드 삽입, front는 맨 처음 노드 가르키고 있음 ㄷ
            self.tail = node
            self.front = node
        self.tail.next = node   # 이전 노드를 새로운 노드에 연결
        self.tail = node        # 새로운 노드는 가장 마지막 노드
        self.size += 1

    def dequeue(self):
        assert not self.isEmpty(), print('queue Empty')
        item = self.front.item
        self.front = self.front.next
        self.size -= 1
        return item

    def size(self):
        assert not self.isEmpty(), print('queue Empty')
        return self.size

    def peek(self):
        assert not self.isEmpty(), print('queue Empty')
        return self.front.item

    def isEmpty(self):
        return self.size == 0

    def display(self):
        temp = self.front
        while temp :
            print(temp.item)
            temp = temp.next



class linkedDeque(LinkedQueue):
    def __init__(self):
        super().__init__()

    def front_enqueue(self, item):
        node = Node(item)
        if not self.front:  # 첫 노드일 경우
            self.front = node
            self.tail = node
        else:
            node.next = self.front
            self.front.next = node

    def rear_dequeue(self):
        assert not self.isEmpty(), print('Linked Deque Empty')
        temp = self.front
        item = self.tail.item

        while temp.next != self.tail :
            temp = temp.next

        temp.next = None
        self.tail = temp
        return item

    def rear_peek(self):
        assert not self.isEmpty(), print('Linked Deque Empty')
        return self.tail.item



class Node :
    def __init__(self, item=None):
        self.item = None
        self.next = None
