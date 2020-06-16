

# 프로그래머스 쇠막대기
from collections import deque

def solution2(arrangement):
    answer = 0
    cnt = 0
    s = deque()


'''ㅏ
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


