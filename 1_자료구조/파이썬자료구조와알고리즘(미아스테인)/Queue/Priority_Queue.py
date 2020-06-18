class PriorityQ :
    def __init__(self):
        self.pQueue = list()
        self.count = 0

    def enqueue(self, element, priority):
        item = Items(element, priority)
        self.pQueue.append(item)
        self.count += 1

    def dequeue(self):
        assert not self.isEmpty(), print('Queue empty')

        highest = self.pQueue[0].priority
        highest_idx = 0
        for item in self.pQueue :
            if item.priority < highest :
                # 낮은 숫자가 더 높은 우선순위를 가짐
                highest = item.priority
                highest_idx = self.pQueue.index()
                # 높은 우선순위를 갖는 인덱스를 가져옴

        self.count -= 1
        item = self.pQueue.pop(highest_idx)
        return item.element
        # 높은 우선순위를 갖는 인덱스의 값을 반환 및 리스트에서 제거

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def print_(self):
        for item in self.pQueue :
            print('{0:>3} {1:>3}'.format(item.element, item.priority))


class Items :
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority


pq = PriorityQ()
pq.enqueue(1, 0)
pq.enqueue(100, 10)
pq.print_()
print('dequeue : ', pq.dequeue())
pq.print_()