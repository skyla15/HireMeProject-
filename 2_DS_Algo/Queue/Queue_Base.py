from abc import *

class Queue_Base(metaclass=ABCMeta):
    def __init__(self):
        self.in_queue = []
        self.out_queue = []
    # 리스트 구현 시 : head, count
    # 링크드 리스트로 구현 시 : head / tail / count

    @abstractmethod
    def enqueue(self, item):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def transfer(self):
        pass

    def transfer(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    # In_Stack
# (Enqueue) : append 사용
#     [0]  [1]  [2]  [3]  [4]  [5]
#      a
#      a    b
#      a    b    c ....

# (Dequeue) : Out_Queue로 마지막 요소부터(pop) Transfer
#             Out_queue의 마지막 요소 반환(pop)
#     [0]  [1]  [2]  [3]  [4]  [5]
#      a
#      a    b
#      a    b    c ....


# Out_Stack
#     [0]  [1]  [2]  [3]  [4]  [5]
#      c
#      c    b
#      c    b    a

