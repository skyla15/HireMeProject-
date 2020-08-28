# 두 정수 사이의 합
def solution1(a, b):
    return sum(range(min(a,b),max(a,b)+1))

# 수박수박수박수박수?
def solution2(n):
    subak = '수박'
    return ''.join([subak[k%2] for k in range(n)])

# 서울에서 김서방 찾기
def solution3(seoul):
    return ''.join(['김서방은 ', str(seoul.index('Kim')), '에 있다'])

# 약수의 합
def solution4(n):
    return sum([k for k in range(1, n+1) if n % k == 0])

# 문자열 내 p와 y의 개수
def solution5(s):
    p = len([x for x in s.lower() if x == 'p'])
    y = len([x for x in s.lower() if x == 'y'])
    return p == y

# 같은 숫자는 싫어
def solution6(arr):
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
def solution7(s):
    answer = ''
    if len(s) == 1:
        return s
    elif len(s) % 2 == 0:
        return ''.join([s[len(s)//2 - 1], s[len(s)//2]])
    else:
        return s[len(s)//2]

# x만큼 간격이 있는 n개의 숫자
def solution8(x, n):
    answer = []
    for i in range(n):
        answer.append(x + i * x)

    return answer

# 직사각형 별찍기
def solution9(a, b)
# a, b = map(int, input().strip().split(' '))
    for i in range(b):
        for j in range(a):
            print('*', end='')
        print()

# 평균 구하기
def solution10(arr):
    return sum(arr)/len(arr)

# 행렬의 덧셈
import numpy as np
def solution11(arr1, arr2):
    answer1 = np.array(arr1) + np.array(arr2)
    # return answer1.tolist()
    answer2 = [[None for col in range(len(arr1[0]))] for row in range(len(arr1))]
    for m in range(len(arr1)):
        for n in range(len(arr1[m])):
            answer2[m][n] = arr1[m][n] + arr2[m][n]
    return answer2

# 짝수와 홀수
def solution12(num):
    a = ['Even', 'Odd']
    return a[num%2]

# 자릿수 더하기
def solution13(n):
    answer = 0
    l = len(str(n))
    for i in range(l):
        answer += int(str(n)[i])
    return answer

# 최대공약수와 최소공배수
def solution14(n, m):
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
def solution15(n):
    sq = int(math.sqrt(n))
    if sq**2 == n:
        return (sq+1) ** 2
    return -1

# 문자열 다루기 기본
def solution16(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False

# 정수 내림차순으로 배치하기
def solution17(n):
    return int(''.join(sorted(str(n), reverse = True)))

