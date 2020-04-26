class Heapify(object):
    def __init__(self, data=None):
        if isinstance(data, dict):
            self.data = [(k,v) for k, v in data.items()]
            print(self.data)
        else:
            self.data = data or []
        # 전체 트리의 절반부터 검색, 리스트의 마지막에서 반대로 검색
        for i in range(len(data)//2, -1, -1):
            self.heapify(i)

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self,i):
        return (i << 1) + 2

    def get_parent(self,i):
        # when child has an odd number
        if i & 1 :
            return (i >> 1)
        else :
            return (i >> 1) - 1

    def heapify(self, i):
        largest = i  # 현재 인덱스를 largest로
        lchild = self.left_child(i)
        rchild = self.right_child(i)
        n = len(self.data) # 현재 데이터의 총 길이

        # 현재 인덱스의 값과, 자식들이 갖고 있는 값을 비교
        largest = ( ( lchild < n and self.data[lchild] > self.data[largest] ) and lchild ) or largest   # 좌측 자식
        largest = ( ( rchild < n and self.data[rchild] > self.data[largest] ) and rchild ) or largest   # 우측 자식

        # 만약 자식이 갖고 있는 값이 현재 들어온 인덱스보다 더 클 경우 Swap
        if largest is not i :
            self.data[largest], self.data[i] = self.data[i], self.data[largest]
            # 현재 가장 큰 값을 갖고 있는 인덱스로 heapify -> 자식 - 자식 - 자식
            self.heapify(largest)


    def insert(self,item):
        # add the element to the bottom level of the heap
        # compare the element with its parent. if they are in the correct order, stop
        # if not, swap the element with its parent and return to the previous step
        i = len(self.data) # item을 넣기 전 data 길이 + 1
        self.data.append(item)

        while ( i != 0 ) and item > self.data[self.get_parent(i)] :
            self.data[i] = self.data[self.get_parent(i)]
            i = self.get_parent(i)
        self.data[i] = item


    def getMax(self):
        # Save the root item in a variable
        # Replace the root of the heap with the last element on the last level
        # Compare the new root with its children; if they are in the correct order, stop
        # If not, swap the element with one of its children and return to the previous step
        val = self.data[0]
        self.data[0] = self.data[len(self.data)-1]  # 가장 마지막 노드의 값을 루트에 둠으로써 heapify 가능하도록
        self.data = self.data[:len(self.data)-1]    # 마지막 인덱스 삭제
        self.heapify(0)
        return val

    def refreshHeap(self):
        return self.data


if __name__ == '__main__':
    # testData = [(1, 'dog'),(4, 'sex'),(10, 'cat'),(5, 'desire')]

    testData = { 100 : 'NakedGirl', 1000 : 'sex', 10000 : 'whiteChicks', 1 : 'KoreanBitch' }
    priorityQ = Heapify(testData)
    print(priorityQ.getMax())
    testData = priorityQ.refreshHeap()

    priorityQ = Heapify(testData)
    testData = priorityQ.refreshHeap()
    print(priorityQ.getMax())
    priorityQ = Heapify(testData)

    print(priorityQ.getMax())
