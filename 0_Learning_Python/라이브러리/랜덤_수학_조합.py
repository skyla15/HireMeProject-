
"""math, random, itertools, fraction"""

"""------------
| Math module  |
 --------------
# 함수
    - factorial(x)  : x의 계승
    - gcd(a, b)     : a,b 최대 공약수
    - floor(x)      : x의 소수점 아래 버림
    - ceil(x)       : x의 소수점 아래 올림
    - pow(x,y)      : x의 y승 ( x**y )
    - sqrt(x)       : x의 제곱근
    - log(x, base)  : base를 밑으로하는 x의 로그
# 상수
    - pi            : 원주율
    - e             : 자연상수(e)
    - inf           : 양의 무한대
    """
import math
math.gcd(21, 28)    # 21과 28의 최대공약수         / 7
math.floor(math.e)  # 자연상수의 소수점 아래를 버림   / 2
math.ceil(math.e)   # 자연상수의 소수점 아래를 올림   / 3



""" ----------------
| Random module  |
 ----------------
 # 함수
    # Rnadom 정수 / 실수 
        - randint(a,b)  : a이상 b이하 정수
        - seed(a=None)  : 난수 seed 'a' 설정 / a 없을 경우 시스템 시간 사용  
                          seed값을 동일하게 설정하면 난수 발생순서가 동일하게 발생   
        - random()      : 0이상 1미만 실수 
    
    # 시퀀스 객체 사용 
        - choice(seq)   : seq 임의 요소 무작위 선택 
        - sample(seq, k): seq 임의 요소 K개 무작위 선택
        - shuffle(seq)  : seq 무작위 shuffle
 """
import random
S = ['고양이', '곰', '돼지', '여우', '담비']
print(S[random.randint(0,len(S)-1)])
print(random.choice(S))     # S에서 1개 무작위 선택
print(random.sample(S, 3))  # S에서 3개 무작위 선택
print('Original S : ', S)
print('Shuffled S : ', random.shuffle(S))


"""-----------------------------
| fractions module - 분수 표현하기  |
 -------------------------------
 # Fraction 모듈 임포트
    - from fractions import Fraction
 # 분수 만들기  
    - Fraction(1 ,3)                          # 1/3
    - Fraction(numerator=1, denominator=3)    # 1/3
 # 분자, 분모 각자 접근 
    Fraction객체.numerator 
    Fraction객체.denominator    
 # 객체 연산 
    - 정수/실수/Fraction객체 간 연산 가능  
"""
from fractions import Fraction
print(Fraction(1,3) + 0.6)              # 0.93333333...
print(Fraction(1,3) + Fraction(1,3))    # 2/3


""" -----------------------------------------
| itertools module - 반복 가능한 객체의 순열과 조합 |
 --------------------------------------------
 # 함수 
    - product(seq1, seq2, ...)  : 여러 시퀀스들의 곱집합 
    - permutations(p, r)        : p 시퀀스의 요소 r개를 나열하는 순열 ( pPr ) 
    - combinations(p, r)        : p 시퀀스의 요소 r개를 선택하는 조합 ( pCr )
    - combinations_with_replacement(p,r)
                                : p 시퀀스의 요소 r개를 중복 허용 선택하는 조합 ( p∏r ) 
"""
import itertools
from pprint import pprint
S1 = ['사막', '북극']
S2 = ['곰', '고양이', '여우']
S3 =list( itertools.product(S1, S2) )
pprint(S3)
'''
[('사막', '곰'),
 ('사막', '고양이'),
 ('사막', '여우'),
 ('북극', '곰'),
 ('북극', '고양이'),
 ('북극', '여우')]
'''

pprint(list(itertools.permutations(S2, 2)))
'''
[('곰', '고양이'),
 ('곰', '여우'),
 ('고양이', '곰'),
 ('고양이', '여우'),
 ('여우', '곰'),
 ('여우', '고양이')]
'''

pprint(list(itertools.combinations(S2, 2)))
'''
[('곰', '고양이'), 
 ('곰', '여우'), 
 ('고양이', '여우')]
'''





