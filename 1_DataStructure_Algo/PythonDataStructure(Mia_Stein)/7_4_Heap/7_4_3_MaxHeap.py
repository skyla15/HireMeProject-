#
# # 최대 힙 구현 #
# #                        0(3)
# #            1(2)                     2(5)
# #     3(1)          4(7)       5(8)           6(2)
# i노드 자식의 왼쪽 인덱스 : (i*2)+1
# i노드 자식의 오른쪽 인덱스 : (i*2)+2
#
# 1) 전체 배열의 길이를 반으로 나눈다 ( 7 // 2 -> 3 )
# 2) 인덱스 3 인경우 자식이 없음 -> 인덱스 하나 내려감
# 3) 인덱스 2 : 자식이 있고 자식의 값이 더 클 경우 본인의 값이랑 교환 5 <-> 8
# #                        0(3)
# #            1(2)                     2(8)
# #     3(1)          4(7)       5(5)           6(2)
# 4) 교환한 인덱스 5를 다시 자식들과 비교
# 5) 자식이 없으므로 인덱스 하나 내림
# 6) 2~5를 인덱스가 0 일때까지 반복

class Heapify(object):
    def __init__(self, data=None):
        # 데이터들을 받거나 빈 리스트를 생성
        self.data = data or []
        # print(len(data)//2)
        for i in range(len(data)//2,-1,-1):
            # print('i : ', i)
            # 현재 트리 인덱스 길이의 반 인덱스에서
            # 0까지 역으로 루프
            self.__max_heapify__(i)

    def left_child(self, i):
        return (i << 1) + 1

    def right_chid(self, i):
        return (i << 1) + 2

    def parent(self, i):
        if i & 1 :
            return i >> 1
        else :
            return (i >> 1) -1

    # 최대힙으로 만듬
    def __max_heapify__(self,i):
        largest = i                 # 현재 노드
        left = self.left_child(i)   # 왼쪽 자식 노드 인덱스
        right = self.right_chid(i)  # 오른쪽 자식 노드 인덱스
        n = len(self.data)          # 리스트 길이

        # 자식 비교는 왼쪽부터 비교하고
        # 현재 노드 ( i ) 가 왼쪽 자식보다 작을 경우 왼쪽 자식 노드를 largest로 지정
        largest = ( (left < n and self.data[left] > self.data[largest]) and left ) or largest
        # 현재노드가 ( largest ) -< 왼쪽노드가 부모노드보다 클 경우, 현재 largest는 왼쪽 자식 노드의 인덱스를 갖고 있음 >-
        # 오른쪽 자식보다 작을 경우 오른쪽 자식의 인덱스를 largest로 가져감
        largest = ( (right < n and self.data[right] > self.data[largest]) and right ) or largest

        # 만약 현재 인덱스의 값이 자식보다 작을 경우 Swap
        if i is not largest :
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            print(self.data)
            # 스왑 전, 모든 자식들의 값이 부모 노드보다 컸을 경우, 하나만 바뀌므로
            # 다시 스왑된 부모의 값으로 자식들과의 값을 비교
            self.__max_heapify__(largest)


    # 최대값 가져오기 ( 노드의 가장 낮은 인덱스 값 )
    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]
        # 첫 노드와 마지막 노드를 바꾸어줌 => 힙 재정렬을 위함
        self.data[0] = self.data[n-1]
        # 현재 트리를 첫번째 인덱스와 마지막 값이 바뀐 인덱스를 갖는 리스트를 현재 힙의 데이터로 변경 및
        # 마지막 인덱스 제거
        self.data = self.data[:n-1]
        # 첫번째 인덱스 외의 트리는 최대 힙 정렬이 되어있는 상태
        # 따라서 첫번쨰 인덱스에 대해서만 힙 정렬을 다시 해줌
        self.__max_heapify__(0)
        return max_element

    # 최대힙에 값을 추가하기
    def insert(self,item):
        # i = 현재 추가하려는 아이템이 들어갈 인덱스
        i = len(self.data)
        # 마지막 다음 인덱스에 추가하려는 값을 추가
        self.data.append(item)

        # 현재 들어온 값과 부모 인덱스와 값을 계속 비교하여
        # 들어온 값이 부모보다 크다면 부모의 값을 현재 인덱스에 넣고
        # 그 부모의 인덱스를 현재 아이템을 넣을 인덱스로 갖고 있음
        while (i != 0 ) and item > self.data[self.parent(i)] :
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        # 부모의 값보다 현재 들어온 값이 작을 경우 그 인덱스에 현재의 값을 넣어줌
        self.data[i] = item
        print(self.data)

    def __repr__(self):
        return repr(self.data)


def test_heapify():
    l1 = [(1, 'dog'),(4, 'sex'),(10, 'cat'),(5, 'desire')]
    # l1 = [ 3,2,2,2,7,8,2]
    h = Heapify(l1)
    print(h)
    print(h.extract_max())

    # assert(h.extract_max() == 8 ) # 만약 최대값이 8이 아닐경우 에러

if __name__ == '__main__' :
    test_heapify()
