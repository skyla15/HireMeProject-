# Circular Queue
# 파이썬으로 쉽게 풀어쓴 자료구조
# front 인덱스는 항상 비어있는 상태!!!!!!!!!!!!
# 원형큐의 크기는 항상 고정이 되어있어야됨

# 삽입 : rear+1
# 삭제 : front = front+1 이후 front 요소 삭제
# 사이즈 모듈러 연산 : (b - a + size) % size  => b - a 의 절댓값
# display : slicing 연산으로 보여줌 => for 문이나 while 문보다 시간복잡도 낮음

class CircularQueue:
    def __init__(self, MAX_SIZE):
        # todo : set Q size
        # todo : front is always empty !
        self.q = [None] * MAX_SIZE
        self.MAX_SIZE = MAX_SIZE
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        # todo : check if Queue is full
        # todo : forward the rear and insert item into the index of the rear
        if not self.is_full():
            self.rear = ( self.rear + 1 ) % self.MAX_SIZE
            self.q[self.rear] = item
            self.size += 1
        else:
            print('Queue is Full')

    def dequeue(self):
        # todo : check if Queue is empty
        # todo : forward the front and delete the item at the front
        if not self.is_empty():
            self.front = (self.front + 1) % self.MAX_SIZE  # front 한 칸 전진
            item = self.q[self.front]
            self.q[self.front] = None
            self.size -= 1
            return item
        else :
            print('Queue is Empty')

    def is_full(self):
        return self.rear + 1 == self.front

    def is_empty(self):
        return self.front == self.rear

    def display(self):
        if self.front > self.rear:
            print( self.q[:self.rear + 1] + self.q[self.front + 1 :])
        elif self.front < self.rear:
            print( self.q[self.front + 1 : self.rear + 1])
        elif self.is_empty():
            print('q is empty')

    def size(self):
        return self.size

    def peek(self):
        if not self.is_empty():
            print(self.q[self.rear])
            return self.q[self.rear]

q = CircularQueue(10)
for i in range(8):
    q.enqueue(i)
q.display()
q.peek()
q.dequeue()
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
q.dequeue()
q.display()
