# insert 메소드를 사용함으로써 모든 요소가 메모리에서 이동될 수 있음
# insert 작업 => O(n), 비효율적
# 큐의 시간복잡도 = O(1) 


from Queue_Base import *

class Queue(Queue_Base) :
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0, item)
        # 요소를 삽입하면 기존 요소들은 뒤 인덱스로 보냄
        # pop을 통해 요소 뺼 수 있음, First In First Out

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        else :
            print('Queue Empty')

    def isEmpty(self):
        return not bool(self.items)

    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]
        else :
            print('Queue Empty')

    def size(self):
        if not self.isEmpty() :
            return len(self.items)

    def __repr__(self):
        return repr(self.items)

if __name__ == '__main__' :
    queue = Queue()
    print('isEmpty? : {0}'.format(queue.isEmpty()))
    print('inserting numbers : 0 ~ 9 ... ')
    for i in range(10) :
        queue.enqueue(i)
    print('isEmpty? : {0}'.format(queue.isEmpty()))
    print('peek : {0}'.format(queue.peek()))
    print('size : {0}'.format(queue.size()))
    print('dequeue : {0}'.format(queue.dequeue()))
    print('peek : {0}'.format(queue.peek()))
    print('size : {0}'.format(queue.size()))