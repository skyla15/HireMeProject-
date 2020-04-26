# 참고 | map, filter, reduce와 리스트 표현식
# 리스트(딕셔너리, 세트) 표현식으로 처리할 수 있는 경우에는 map,
# filter와 람다 표현식 대신 리스트 표현식을 사용하는 것이 좋습니다.
# list(filter(lambda x: x > 5 and x < 10, a))는
# 다음과 같이 리스트 표현식으로도 만들 수 있습니다.
# >>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# >>> [i for i in a if i > 5 and i < 10]
# [8, 7, 9]

# for, while 반복문으로 처리할 수 있는 경우에도
# reduce 대신 for, while을 사용하는 것이 좋습니다.
# 왜냐하면 reduce는 코드가 조금만 복잡해져도 의미하는 바를 한 눈에 알아보기가 힘들기 때문입니다.
# 이러한 이유로 파이썬 3부터는 reduce가 내장 함수에서 제외되었습니다.
# reduce(lambda x, y: x + y, a)는 다음과 같이 for 반복문으로 표현할 수 있습니다.
# >>> a = [1, 2, 3, 4, 5]
# >>> x = a[0]
# >>> for i in range(len(a) - 1):
# ...     x = x + a[i + 1]
# ...
# >>> x
# 15

# 32.1 람다 표현식 ( 익명 함수 )
# 32.1.1 람다 표현식 사용하기
# 아래 두 함수는 같은 값을 반환
def plus_ten(x) :
    return x + 10

lambda x : x + 10

# 32.1.2 람다 표현식 자체 호출
# (람다 표현식)(매개변수)
for i in range(10) :
    x = lambda y : y+10 # 람다 객체 선언
    print(x(i))

# 32.1.3 map함수에 람다 함수 사용하기
li = list(map((lambda x : x+10), [10,20,30]))
print(li)

# 32.1.4 매개변수가 없는 lambda 표현식
(lambda : 1)()
print((lambda : 1)() )


# 32.2.1 람다 표현식에 if else 사용 함
# -> if만 사용시 문법에러
# -> elif 사용 불가능 :  if else 중 사용
# -> 반환값1 if 조건식1 else 반환값2 if 조건식2 else 반환값3
list_1=[1,2,3,4,5,6,7,8,9,10]
x = map((lambda x : '빵' if x%2 == 0 else '' if x%3 ==0 else x * 100), list_1)
print(list(x))

# 32.2.2 map에 여러 객체 넣기
# map(함수, 반복 가능 객체1, 시퀀스 객체2....)
a = [1,2,3,4,5]
b = [10,20,30,40,50]
map_a_b = map((lambda a, b : a*b), a, b)
list_a_b = list(map_a_b)
print(list_a_b)


# 32.2.3 filter(함수, 반복 가능 객체)
# 함수의 반환값이 True인 경우의 값으로 새로운 리스트 생성
def f(x) :
    return x > 5 and x < 10
a = [1,2,3,4,5,6,7,8,9]
print(list(filter(f,a)))
print( list( filter((lambda x : x > 5 and x < 10), a) ) )

# 32.2.4 reduce(함수, 반복 가능 객체)
# 반복 가능 객체를 함수처리 후 누적 덧셈 후 반환
from functools import reduce
a = [1,2,3,4,5,6,7,8,9]
reduced_a = reduce((lambda x,y : x+y), a)
print(reduced_a)