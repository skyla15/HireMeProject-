# 두 정수 사이의 합
def solution(a, b):
    return sum(range(min(a,b),max(a,b)+1))


# 수박수박수박수박수?
def solution(n):
    subak = '수박'
    return ''.join([subak[k%2] for k in range(n)])


# 서울에서 김서방 찾기
def solution(seoul):
    return ''.join(['김서방은 ', str(seoul.index('Kim')), '에 있다'])


# 약수의 합
def solution(n):
    return sum([k for k in range(1, n+1) if n % k == 0])


# 문자열 내 p와 y의 개수
def solution(s):
    p = len([x for x in s.lower() if x == 'p'])
    y = len([x for x in s.lower() if x == 'y'])
    return p == y


# 같은 숫자는 싫어
def solution(arr):
    answer = []
    m, n = 0, 1
    if len(arr) == 1 or len(arr) == 2:
        answer = arr
        return answer
    for _ in range(len(arr) - 1):
        if arr[m] != arr[n]:
            answer.append(arr[m])
        m += 1
        n += 1
    answer.append(arr[n - 1])
    return answer


# 가운데 글자 가져오기
def solution(s):
    if len(s) == 1:
        return s
    elif len(s) % 2 == 0:
        return ''.join([s[len(s)//2 - 1], s[len(s)//2]])
    else:
        return s[len(s)//2]

    
# x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x + i * x)

    return answer


# 직사각형 별찍기
def solution(a, b)
# a, b = map(int, input().strip().split(' '))
    for i in range(b):
        for j in range(a):
            print('*', end='')
        print()

        
# 평균 구하기
def solution(arr):
    return sum(arr)/len(arr)


# 행렬의 덧셈
import numpy as np
def solution(arr1, arr2):
    answer1 = np.array(arr1) + np.array(arr2)
    # return answer1.tolist()
    answer2 = [[None for col in range(len(arr1[0]))] for row in range(len(arr1))]
    for m in range(len(arr1)):
        for n in range(len(arr1[m])):
            answer2[m][n] = arr1[m][n] + arr2[m][n]
    return answer2


# 짝수와 홀수
def solution(num):
    a = ['Even', 'Odd']
    return a[num%2]


# 자릿수 더하기
def solution(n):
    answer = 0
    l = len(str(n))
    for i in range(l):
        answer += int(str(n)[i])
    return answer


# 최대공약수와 최소공배수
def solution(n, m):
    # 1
    a = [i for i in range(1, n + 1) if n % i == 0]
    b = [i for i in range(1, m + 1) if m % i == 0]
    gcd1 = max([i for i in a if i in b])

    # 2
    a = max(n, m)
    b = min(n, m)
    while b:
        a, b = b, a % b
    gcd2 = a

    return [gcd1, n * m // gcd1]


# 정수 제곱근 판별
import math
def solution(n):
    sq = int(math.sqrt(n))
    if sq**2 == n:
        return (sq+1) ** 2
    return -1


# 문자열 다루기 기본
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False


# 정수 내림차순으로 배치하기
def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))


# 자연수 뒤집어 배열로 만들기
def solution(n):
    return [int(x) for x in str(n)[::-1]]


# 핸드폰 번호 가리기
def solution(phone_number):
    l = len(list(phone_number))
    return '*' * (l-4) + str(phone_number)[l-4:]


# K번째 수
def solution(array, commands):
    for a, b, c in commands:
        answer.append(sorted(array[a - 1:b])[c - 1])
    return answer


# 하샤드 수
def solution(x):
    return x % sum([int(x) for x in str(x)]) == 0


# 나누어 떨어지는 숫자배열
def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    if len(answer) == 0:
        return [-1]
    return sorted(answer)


# 모의고사
def solution(answers):
    temp = list()
    answer = list()
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo1, supo2, supo3 = list(), list(), list()
    for i in range(len(answers)):
        supo1.append(a1[i % 5] - answers[i])
        supo2.append(a2[i % 8] - answers[i])
        supo3.append(a3[i % 10] - answers[i])

    temp.append(supo1.count(0))
    temp.append(supo2.count(0))
    temp.append(supo3.count(0))

    for i in range(3):
        if temp[i] == max(temp):
            answer.append(i + 1)

    return answer


# 완주하지 못한 선수 
# time complextiy with 'in' operator is O(N), 
# if used, the worst time complexity would be O(n^2) which is not the goal of this problem.
# Here, you have to use the data structure 'hash' which is already implented in Python as dictionary.
# With dictionary, you can reach each element with time complexity of O(n).
def solution(participant, completion):
    hash = {}
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1
            
    for c in completion:
        if c in hash:
            hash[c] -= 1
            if hash[c] == 0:
                del hash[c]
    return list(hash.keys())[0]
            

# 2016
def solution(a, b):
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30] # 1~ 11
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    mon = 0
    for i in range(a):
        mon += month[i]
    days = mon + b    
    
    return day[days%7]


# 소수찾기 
# 에라토스테네스의 체!
# n의 최대 약수 : sqrt(n) 이하 
def solution(n):
    a = [False] * (n + 1)
    m = int(n**0.5)
    # sqrt(n)까지만 외부 반복
    for i in range(2, m+1):
        if a[i]: continue 
        # 내부 반복 : n 까지 모든 수에 대해 True 값 -> 소수가 아님 
        for j in range(i + i, n + 1, i):
            a[j] = True        
    return len([x for x in range(2, n + 1) if a[x] == False])


# 예산
def solution(d, budget):
    answer = 0
    d.sort()
    while len(d) > 0:
        budget -= d.pop(0)
        if budget < 0:
            break;
        else:
            answer += 1
    return answer


# 체육복 
def solution(n, lost, reserve):
    reserves = [x for x in reserve if x not in lost]
    lost = [x for x in lost if x not in reserve]

    for r in reserves:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1) 
            
    return n - len(lost)


# 시저 암호 
def solution(s, n):
    print(ord('a'), ord('z'), ord('A'), ord('Z'))
    # 97 122 65 90 
    answer = ''
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            if ord(c) + n > 122:
                answer += chr(97 + (ord(c) + n) % 123)
            else:
                answer += chr(ord(c) + n) 
        elif ord(c) >= 65 and ord(c) <= 90:
            if ord(c) + n > 90:
                answer += chr(65 + (ord(c) + n) % 91) 
            else:
                answer += chr(ord(c) + n) 
        else:
            answer += c
    return answer
            

# 비밀지도 
# format, bin 등.. => 진법 변환 공부하기.
def solution(n, arr1, arr2):
    secret_map = list()
    for k in range(n): 
        secret_map.append(format((arr1[k] | arr2[k]), 'b'))

    for i in range(n):
        if len(format(secret_map[i])) < n:
            secret_map[i] = '0' * ( n - len(secret_map[i]) ) + secret_map[i]
        secret_map[i] = ''.join(['#' if x == '1' else ' ' for x in secret_map[i]])
    return secret_map

