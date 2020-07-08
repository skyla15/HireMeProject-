'''
Can reference to the head by advancing one step from the tail

1) when queue is empty
node1 -(next)> node1

2) when queue is not empty
node1 -(next)-> new_node -(next)-> node1
head
tail
- enqueue
    - new_node
        -> new_node.next
'''

class CircularQueue(object):

    class _Node(object):
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = None

    def __init__(self):
        '''
        No head pointer is needed as I can reference to the head of the queue
        by advancing one step ahead at the end of the circular queue
        '''
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, element):
        new_node = self._Node(element, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            # 새로운 노드의 다음은 헤드
            new_node._next = self._tail._next
            # 이전 노드와 새로운 노드 이어줌
            self._tail._next = new_node
        # tail을 새로운 노드로 설정
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        # 큐가 비었을 경우
        assert not self.is_empty(), 'Queue is empty'
        front = self._tail._next
        e = front._element
        if self._size == 1:             # 큐에 노드가 1개인 경우, Reference 처리
            self._tail = None
        else:                           # 큐에 노드가 2개 이상인 경우, 테일 -(link)> 헤드.next
            self._tail._next = front._next
        self._size -= 1
        return e

    def is_empty(self):
        return self._size == 0

    # Tail을 한 단계만 앞으로 전진 시키면, front -> back으로 빠지게 됨
    def rotate(self):
        assert not self.is_empty(), 'Queue is empty'
        front = self._tail._nextq
        self._tail = front

    def display(self):
        assert not self.is_empty(), 'Queue is empty'
        temp_front = self._tail._next
        for _ in range(self._size):
            print(temp_front._element, end = ' ')
            temp_front = temp_front._next
        print()

    def first(self):
        front = self._tail._next
        return front._element



q = CircularQueue()

for i in range(1,21):
    q.enqueue(i)
q.display()
print()

print('dequeue : ', q.dequeue())

print()

print('Before rotate : ', end = '')
print(f'first : {q.first()}')
q.display()

q.rotate()
print()

print(' After rotate : ', end = '')
print(f'first : {q.first()}')
q.display()


for _ in range(len(q)):
    q.dequeue()
    q.display()
    print(q.dequeue())

print()
