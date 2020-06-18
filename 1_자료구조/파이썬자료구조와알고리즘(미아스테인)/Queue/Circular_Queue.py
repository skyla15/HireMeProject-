# 리스트로 큐를 구현시
# dequeue시 pop(0)을 사용하기에 리스트들이 shift될 수 있음
# => 최대 시간 복잡도 O(n)
# Circualr 큐 / Node 를 이용할 경우 shift되는 것을 막을 수 있음
# Circualr 큐 : 인덱스로 접근


class CircularQueue :
    def __init__(self, MAX_SIZE):
        self.MAX_SIZE = MAX_SIZE
        self.circularQ = [None]*MAX_SIZE
        self.count = 0  # queue size
        self.front = 0  # front
        self.back = MAX_SIZE-1   # back

    def next_index(self, idx):
        return (idx + 1) % self.MAX_SIZE

    def enqueue(self, item):
        try :
            if self.isFull() :
                raise Exception('Circular Queue is Full')
        except Exception as e :
            print(e)

        self.back = self.next_index(self.back)
        # print('self.back :', self.back)
        self.circularQ[self.back] = item
        self.count += 1

    def dequeue(self):
        try :
            if self.isEmpty() :
                raise Exception('Circualr Queue Empty')
        except Exception as e :
            print(e)

        item = self.circularQ[self.front]
        self.front = self.next_index(self.front)
        self.count -= 1
        return item

    def size(self):
        assert not self.isEmpty(), 'Circular Queue Empty'
        return self.count

    def isFull(self):
        return self.count == self.MAX_SIZE

    def isEmpty(self):
        return self.count == 0

    def peek(self):
        return self.circularQ[self.front]

    def print_(self):
        start = self.front
        while start <= self.back :
            print(self.circularQ[start], end = ' ')
            start +=1
        print()


if __name__ == '__main__' :
    cq = CircularQueue(8)
    cq.enqueue(1)
    # cq.print_()
    cq.enqueue(3)
    cq.enqueue(3)
    cq.enqueue(3)
    cq.dequeue()
    cq.dequeue()
    cq.enqueue(3)
    cq.enqueue(3)
    cq.enqueue(3)
    cq.enqueue(3)
    cq.enqueue(3)
    cq.enqueue(3)
    print(cq.circularQ[cq.front])






    cq.dequeue()
    #
    # cq.enqueue(6)
    # cq.print_()
