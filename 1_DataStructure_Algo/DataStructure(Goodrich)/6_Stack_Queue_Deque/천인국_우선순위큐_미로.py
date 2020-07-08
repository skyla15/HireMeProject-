import math

# max heap
class PriorityQ(object):
    def __init__(self, l = []):
        self.q = l
        for i in range(len(self.q) // 2, -1, -1):
            self.heapify(i)

    def get_parents(self, i):
        if i & 1:
            return i // 2
        else:
            return i // 2 - 1

    def get_left_child(self, i):
        return i * 2 + 1

    def get_right_child(self, i):
        return i * 2 + 2

    def heapify(self, i):
        largest = i
        n = len(self.q)
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)

        if ( left_child < n and self.q[left_child] > self.q[largest] ):
            largest = left_child
        if ( right_child < n and self.q[right_child] > self.q[largest] ):
            largest = right_child

        # 자식이 더 크다면, 스왑 후, 자식노드부터 다시 달려
        if i != largest:
            self.q[largest], self.q[i] = self.q[i], self.q[largest]
            self.heapify(largest)

    def extract_max(self):
        element = self.q[0]
        last = len(self.q) - 1
        self.q[0], self.q[last] = self.q[last], self.q[0]
        self.q = self.q[:len(self.q) - 1]
        self.heapify(0)
        return element


    def insert(self, item):
        self.q.append(item)
        new_idx = len(self.q) - 1
        while item > self.q[self.get_parents(new_idx)] and new_idx != 0:
            self.q[new_idx] = self.q[self.get_parents(new_idx)]
            new_idx = self.get_parents(new_idx)
        self.q[new_idx] = item

    def is_empty(self):
        return len(self.q) == 0


def dist(x, y):
    (ox,oy) = (5,4)
    return math.sqrt( (ox-x)**2 + (oy-y)**2 )

def isValidPos(x, y, map):
    if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return False
    if map[y][x] == '0'  or map[y][x] == 'x':
        return True

def priority_search(map):
    q = PriorityQ()
    here = ( -dist(0,1), 0, 1)
    q.insert(here)

    while not q.is_empty():
        print('======================================================')
        here = q.extract_max()
        print(here[1:3], end='->')
        _, x, y = here
        if(map[y][x] == 'x'):
            map[y][x] = '●'
            return True
        else:
            map[y][x] = '●'
            if isValidPos(x, y - 1, map): q.insert( (-dist(x, y - 1), x, y - 1) )
            if isValidPos(x, y + 1, map): q.insert( (-dist(x, y + 1), x, y + 1) )
            if isValidPos(x - 1, y, map): q.insert( (-dist(x - 1, y), x - 1, y) )
            if isValidPos(x + 1, y, map): q.insert( (-dist(x + 1, y), x + 1, y) )
        print(q.q)
        for i in range(len(map)):
            print(map[i])
        print('======================================================')
    return False


if __name__ == '__main__' :

    map = [ [ '1', '1', '1', '1', '1', '1'],
            [ 'e', '0', '0', '0', '0', '1'],
            [ '1', '0', '1', '0', '1', '1'],
            [ '1', '1', '1', '0', '0', 'x'],
            [ '1', '1', '1', '0', '1', '1'],
            [ '1', '1', '1', '1', '1', '1'],]

    for i in range(len(map)):
        print(map[i])

    result = priority_search(map)
    if result:
        print('미로찾기 성공')
        for i in range(len(map)):
            print(map[i])
    else:
        print('fucked')

    # l1 = [(1, 'dog'),(4, 'sex'),(10, 'cat'),(5, 'desire')]
    # # l1 = [ 3,2,2,2,7,8,2]
    # h = PriorityQ(l1)
    # print(h.q)
    # print(h.extract_max())
    # print(h.q)
    # print(h.extract_max())
    # print(h.q)
    # print(h.extract_max())
    # print(h.q)

