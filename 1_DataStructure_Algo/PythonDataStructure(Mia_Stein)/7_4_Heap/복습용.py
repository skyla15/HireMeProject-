class Heapify(object):
    def __init__(self, data = None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.max_heapify(i)

    def get_parent(self, i ):
        if i & 1:
            return i // 2
        else:
            return i // 2 - 1

    def get_left_child(self, i):
        return i * 2 + 1

    def get_right_child(self ,i):
        return i * 2 + 2

    def max_heapify(self,i):
        largest = i     # 현재노드
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        n = len(self.data)

        # left가 트리 안에 들어있고, 만약 자식이 부모보다 크다면, 스왑
        largest = ( left < n and self.data[left] > self.data[largest] ) and left or largest
        largest = ( right < n and self.data[right] > self.data[largest] ) and right or largest

        # 자식과 비교해서 작아졌다면
        if i is not largest:
            # swap
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            # 바뀐 자식노드를 루트로 그 아래 자식노드들과 비교
            self.max_heapify(largest)
            print(self.data)

    # 최대값 추출
    # 첫번째 노드와 마지막 노드 바꾸고
    # 힙 길이 - 1 만큼을 루트로 하여금 다시 재정렬
    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]
        self.data[0] = self.data[n-1]
        self.data = self.data[:n-1]
        self.max_heapify(0)
        return max_element

    def insert(self, item):
        self.data.append(item)
        # 마지막 인덱스
        i = len(self.data) - 1
        while ( i != 0 ) and item > self.data[self.get_parent(i)]:
            self.data[i] = self.data[self.get_parent(i)]
            i = self.get_parent(i)
        self.data[i] = item


def main():
    l1 = [ 3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    print(h.data)

main()
