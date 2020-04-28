# 고려
# 삽입시 : 첫번째 노드인가
# 삭제시 : 큐가 비었는 가

class Node() :
    def __init__(self, item=None, next = None):
        self.item = item
        self.next = next

class Queue() :
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        node = Node(item)
        if not self.head :      # 첫 요소일 경우
            self.head = node    # 헤드/테일 포인터 자신으로 지정
            self.tail = node
        else :
            if self.tail :      # 노드들을 이어줌
                self.tail.next = node
            self.tail = node    # 현재 노드를 마지막 노드로 지정
        self.count += 1

    def dequeue(self):
        if self.head :
            temp = self.head.item
            self.head = self.head.next
            self.count -= 1
            return temp
        else :
            return 'Queue Empty'

    def isEmpty(self):
        return not self.head

    def size(self):
        return self.count

    def peek(self):
        if self.head :
            return self.head.item
        else :
            return 'Queue Empty'

    def print(self):
        node = self.head
        while node :
            print(node.item, end = ' ')
            node = node.next

if __name__ == '__main__' :
    queue = Queue()
    print('isEmpty? : {0}'.format(queue.isEmpty()))
    print('inserting numbers : 0 ~ 9 ... ')
    for i in range(10):
        queue.enqueue(i)
    print('isEmpty? : {0}'.format(queue.isEmpty()))
    print('peek : {0}'.format(queue.peek()))
    print('size : {0}'.format(queue.size()))
    print('dequeue : {0}'.format(queue.dequeue()))
    print('peek : {0}'.format(queue.peek()))
    print('size : {0}'.format(queue.size()))
    queue.print()


