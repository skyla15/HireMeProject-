##############
# Stack ADT ##
############################
# 시간 복잡도 : O(1)
# Last In First Out (선입선출)
############################
# empty : 스택이 비었는 지 확인
# push : 맨 끝에 데이터 삽입
# pop : 스택 마지막 값 제거, 반환
# top / peek : 마지막 값 확인
# size : 스택 사이즈 확인

class Stack(object) :
    def __init__(self):
        self.items = [] # 스택 리스트

    def isEmpty(self):
        return not bool(self.items)

    def size(self):
        if self.items :
            return len(self.items)
        else :
            print('Stack Empty')

    def push(self,value):
        self.items.append(value) # 스택 리스트 마지막에 요소 삽입

    def pop(self):
        # 스택이 비어있는 지 확인
        if self.items :
            return self.items.pop()
        else :
            print('Stack Empty')

    def peek(self):
        if self.items :
            return self.items[-1]
        else :
            print('Stack Empty')

    def __repr__(self):
        return repr(self.items)

if __name__ == '__main__' :

    stack = Stack()
    print('Is Stack Empty? : {0}'.format(stack.isEmpty()))
    print('Inserting numbers from 0 to 10')
    for i in range(10) :
        stack.push(i)
    print('Size of the Stack? {0}'.format(stack.size()))
    print('Peek : {0}'.format(stack.peek()))
    print('pop : {0}'.format(stack.pop()))
    print('Peek : {0}'.format(stack.peek()))
    print('Is stack Empty? : {0}'.format(stack.isEmpty()))
    print(stack)

    print('Is stack Empty? : {0}'.format(stack.isEmpty()))


