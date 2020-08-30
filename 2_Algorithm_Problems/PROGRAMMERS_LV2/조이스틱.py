from collections import deque


def updown_count(c):
    if ord(c) >= 79:
        return ord('Z') - ord(c) + 1
    else:
        return ord(c) - 65


def solution(name):
    non_a_deque = deque()
    answer = 0

    # 좌우 움직이는 횟수 // 한 쪽으로 계속 이동
    for i in range(1, len(name)):
        if name[i] != 'A':
            non_a_deque.append(i)

    # 첫 단어가 A가 아닌 경우
    if len(non_a_deque) == 0 and name[0] != 'A':
        return updown_count(name[0])

    elif len(non_a_deque) == 0:
        return answer

    current_index = 0
    visited = list()
    right_flag = left_flage = False

    while non_a_deque:
        mostleft = non_a_deque[0]
        mostright = non_a_deque[-1]

        # 오른쪽으로 이동
        print(non_a_deque)
        if mostleft - current_index <= len(name) - mostright + current_index:
            if left_flag == True or right_flag == True:
                current_index += 1
            right_flag = True
            while current_index <= mostleft:
                print('right')
                if name[current_index] != 'A' and current_index not in visited:
                    answer += updown_count(name[current_index])
                answer += 1
                # print(name[current_index], 'current index : ', current_index, ' answer : ', answer)
                visited.append(current_index)
                current_index += 1
            current_index -= 1
            non_a_deque.popleft()
        # 왼쪽으로 이동
        else:
            if left_flag == True or right_flag == True:
                current_index -= 1
            left_flag = True
            for _ in range(current_index, mostright - len(name) - 1, -1):
                print('left')
                if name[current_index] != 'A' and current_index not in visited:
                    answer += updown_count(name[current_index])
                answer += 1
                visited.append(current_index)
                # print(name[current_index], 'current index : ', current_index, ' answer : ', answer)
                current_index -= 1
            non_a_deque.pop()
            current_index += 1

    answer -= 1
    return answer


# print('answer : ', solution('ABABA'))
print(solution('JAN'))  # 23
print(solution('JEROEN'))  # 56

'''
# 11번 케이스 안돌아감 -> 좌우 계속 비교하면서 이동해야됨. 단 방향 이동 안됨 
from collections import deque

def solution(name):

    non_a_deque = deque()
    answer = 0
    # name = 'AABAAAAAAABBB'

    # 좌우 움직이는 횟수 // 한 쪽으로 계속 이동 
    # A아닌 글자 저장, 좌우 이동 결정 
    for i in range(1, len(name)):
        if name[i] != 'A':
            non_a_deque.append(i)   

    if len(non_a_deque) == 0 and name[0] != 'A':
        if ord(name[0]) >= 79:
            answer += ord('Z') - ord(name[0]) + 1
        else:
            answer += ord(name[0]) - 65
        return answer

    elif len(non_a_deque) == 0:
        return answer

    elif non_a_deque[0] <= len(name) - non_a_deque[-1]:
        # 오른쪽으로 이동, 마지막 non_a_deque 인덱쓰까지 이동 
        for i in range(non_a_deque[-1] + 1):
            # A까지 거리 오른쪽, 왼쪽 계산 
            if name[i] != 'A':
                if ord(name[i]) >= 79:
                    answer += ord('Z') - ord(name[i]) + 1
                else:
                    answer += ord(name[i]) - 65
                print('updown : ', answer)
            answer += 1 
            print('right  : ', answer, name[i], i)
        answer -= 1
        print('answer : ', answer)

    else:
        # 왼쪽으로 이동, 처음 non_a_dque 인덱스까지 이동  
        for i in range(0, non_a_deque[0] - len(name) - 1 , -1):
            up_down_count = 0
            if name[i] != 'A':
                if ord(name[i]) >= 79:
                    answer += ord('Z') - ord(name[i]) + 1
                else:
                    answer += ord(name[i]) - 65
                print('updown : ', answer)
            answer += 1
            print('left   : ', answer, name[i], i)
        answer -= 1
        print('answer : ', answer)
    return answer


'''

