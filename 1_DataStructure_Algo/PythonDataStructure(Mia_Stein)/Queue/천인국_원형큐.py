# Circular Queue
# 파이썬으로 쉽게 풀어쓴 자료구조
# front 인덱스는 항상 비어있는 상태
# 삽입 : rear+1
# 삭제 : front = front+1 이후 front 요소 삭제
# 사이즈 모듈러 연산 : (b - a + size) % size  => b - a 의 절댓값
# display : slicing 연산으로 보여줌 => for 문이나 while 문보다 시간복잡도 낮음


class Circular_Queue :
    def __init__(self, MAX_SIZE):
        self.circularQ = [None]*MAX_SIZE
        self.MAX_SIZE = MAX_SIZE
        self.front = 0                  # 프론트, 리어 초기화
        self.rear = 0

    def enqueue(self,item):
        try :                           # Stack Full 처리
            if self.isFull() :
                raise Exception('Circular Queue Full')
        except Exception as e :
            print(e)

        self.rear = (self.rear+1) % self.MAX_SIZE    # rear 하나 늘려주고
        self.circularQ[self.rear] = item

    def dequeue(self):          # circularQ[front] : 항상 비어있음
        try :
            if self.isEmpty() : raise Exception('Circular Queue Empty')
        except Exception as e:
            print(e)

        self.front = (self.front+1) % self.MAX_SIZE  # front 한 칸 전진
        return self.circularQ[self.front]


    def size(self):         # 핵심 : 모듈러 연산
        return (self.rear - self.front + self.MAX_SIZE) % self.MAX_SIZE

    def isFull(self):
        return self.rear + 1 == self.front  # front는 비어있는 상태로 두기때문

    def isEmpty(self):
        return self.front == self.rear      # front 가 이동해서 rear까지 옴

    def display(self):
        if self.isEmpty() :
            print('Queue Empty')
            return

        diplay_list = []
        #       f     r
        # 0 1 2 3 4 5 6 7 8
        if self.front < self.rear :
            display_list = self.circularQ[self.front+1:self.rear+1]

        #       r     f
        # 0 1 2 3 4 5 6 7 8
        else :
            display_list = self.circualrQ[self.front:self.MAX_SIZE] + \
                self.circularQ[0:self.raer]

        print('current Q')
        print('f=%s r=%d' %(self.front, self.rear), display_list)



cq = Circular_Queue(10)
cq.enqueue(1)
cq.display()
