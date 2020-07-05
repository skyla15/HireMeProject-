class Heapify2:
    def __init__(self, data = None):
        self.data = data
        print('status : ', self.data)
        for i in range(len(data)//2, -1, -1) :
            print('currnet stage : ', i)
            self.__min_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def left_child(self, i):
        return ( i << 1 ) + 1

    def right_child(self,i):
        return ( i << 1 ) + 2

    def get_parent(self,i ):
        if i & 1:  # i가 왼쪽 자식 노드인 경우
            return ( i >> 1 )
        else:       # i가 오른쪽 자식 노드인 경우
            return ( i >> 1 ) - 1

    def __min_heapify__(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        # 왼쪽 자식 노드와 현재 노드 비교
        smallest = ( left < n and self.data[smallest] > self.data[left] ) and left or smallest

        # 오른쪽 자식 노드와 현재 노드 비교
        smallest = ( right < n and self.data[smallest] > self.data[right] ) and right or smallest

        if i != smallest :
            # 노드 간에 값 스와핑
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
            print('status : '.format(i), self.data)
            # 현재 바뀐 인덱스부터 부모들과 비교
            self.__min_heapify__(smallest)

    def extract(self):
        n = len(self.data)

        # 반환할 값을 미리 저장
        min_data = self.data[0]

        # 재정렬을 위해 마지막 값과 첫번째 값 변경
        self.data[0] = self.data[n-1]

        # 재정렬을 위해 마지막 인덱스를 제외한 리스트 재선언
        self.data = self.data[:n-1]

        self.__min_heapify__(0)

        return min_data

    def insert(self, item):
        # 아이템이 들어갈 인덱스
        n = len(self.data)
        # 새로운 아이템을 정렬된 최소힙에 추가
        self.data.append(item)

        # 가장 쉬운 방법은 아이템을 넣은 전체 리스트를 다시 힙정렬하는 것이지만
        # 그러면 정렬이 필요없는 데이터들까지 다시 재정렬을 필요로 함
        # 따라서 현재 아이템이 들어간 인덱스부터 부모와 비교하여 스와핑만 해주면 됨

        # 0의 인덱스를 갖는 노드는 부모가 없으므로
        # 부모의 인덱스가 0인 경우, 반복문 종료
        # 종료 후 현재 인덱스에 item값 삽입
        while ( n != 0 ) and self.data[self.get_parent(n)] > item :
            # 부모의 값이 item보다 클 경우 현재 위치에 부모의 값을 삽입함
            self.data[n] = self.data[self.get_parent(n)]
            # 부모의 인덱스를 가져옴
            n = self.get_parent(n)
        self.data[n] = item




def test_heapify():
    l1 = [ 3,2,5,1,7,8,4 ]
    h = Heapify2(l1)
    print('final : ', h)
    print('extract : ')
    print(h.extract())
    h.insert(1)
    print('insert 1 : ', h)

if __name__ == '__main__' :
    test_heapify()

