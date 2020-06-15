# def solution(p, l):
#     answer = 0
#     m = max(p)
#     while True:
#         v = p.pop(0)
#         # 인쇄 대기목록의 가장 앞에 있는 문서를 대기목록에서 꺼낸다
#         if v == m:
#             answer += 1
#             if l == 0:
#                 break
#             else:
#                 l = (len(p) + l - 1) % (len(p))
#             m = max(p)
#         else:
#             p.append(v)
#             l = (len(p) + l - 1) % (len(p))
#
#
#
#     return answer
#
#
#
# print(solution([2,1,3,2], 2))
# print(solution([1,1,1,1,1], 0))
# print(solution([1,1,2,2,3,3], 5))
# print(solution([1,1,2,2,3,3,9,9,9,9,9,9,9,9], 0))
# print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 0 ))
# '''
# 1 2 2 3 3 1
# 2 2 3 3 1 1
# 2 3 3 1 1 2
# 3 3 1 1 2 2 -> 1, 3
# 3 1 1 2 2 -> 2, 3 : cur
# '''

# Counting integers in ga given array
def solution1(arr):
    cnt = 1
    answer = list()
    last = -1
    for i, n in enumerate(arr):

        if last == n:
            cnt += 1
        else:
            if i != 0:
                k = (last, cnt)
                answer.append(k)
                cnt = 1
            last = n

    k = (last, cnt)
    answer.append(k)

    return answer

# 프로그래머스 쇠막대기
from collections import deque

def solution2(arrangement):
    answer = 0
    cnt = 0
    s = deque()


'''
( ( ( ) ) )
     |
  ___ ___
_____ _____


'''

def main():
    arr = [1, 2, 3, 3, 3, 3, 3, 4, 4]
    arrangement = "()(((()())(())()))(())"
    # print( solution1(arr) )
    solution2(arrangement)

main()


