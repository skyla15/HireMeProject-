import heapq

''' heapq 모듈 사용 '''
class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)

    def __getitem__(self, index):
        return self._queue[index]


def test_priority_queue():
    q = PriorityQueue()
    q.push('test1', 1)
    q.push('test2', 4)
    q.push('test3', 3)
    print(q[0])
    print()
    print(q.pop())
    print(q.pop())
    print(q.pop())
    # assert (str(q.pop()) == "Item('test2')")
    print("테스트 통과!")

test_priority_queue()


'''
import heapq

-> 가장 작은 값이 루트로 들어감
 
heapq.heapify(반복 가능 객체) : 리스트를 O(n) 시간 안에 힘으로 변환

heapq.heappush(힙 객체, 요소)

heapq.heappop(힙) : 힙에서 가장 작은 항목 제거

heapq.heappushpop(힙 객체, 요소) : 힙의 가장 작은 항목 반환, 새항목 추가

heapq.heapreplace(힙 객체, 요소) : 힙의 가장 작은 항목 반환, 새 항목 추가
=>  heappush / heappop 을 따로 쓰는 것보다
    heappushpop / heapreplace 를 쓰는 것이 효율적
'''