from Queue_Base import *

# Out_Stack 을 기준으로
class Queue_With_Two_List(Queue_Base) :
    def __init__(self):
        self.in_stack = []
        self.out_stack =[]

    def transfer(self):
        while self.in_stack :
            self.out_stack.append(self.in_stack.pop())

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack :
            self.transfer()
        if self.out_stack :
            return self.out_stack.pop()
        else :
            # out_stack으로 다 옮겼는 데도 비었다면, 큐는 비어있음
            return 'Queue Empty'

    def isEmpty(self):
        return not self.out_stack

    def size(self):
        return len(self.out_stack)

    def peek(self):
        if not self.out_stack :
            self.transfer()
        if self.out_stack :
            return self.out_stack[-1]
        else :
            return 'Queue Empty'

    def __repr__(self):
        if not self.out_stack :
            self.transfer()
        if self.out_stack :
            repr(self.out_stack)
        else :
            return 'Queue Empty'


if __name__ == '__main__' :
    queue = Queue_With_Two_List()
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