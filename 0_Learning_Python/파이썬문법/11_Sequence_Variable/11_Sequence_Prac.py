# 11. 시퀀스 자료형
# 1) list, tuple, range
# 2) str, bytes, bytearray
# 3) 내장함수 : count(값), index(값), len, del....
# 4) 문자열, range : 인덱스로 요소 변경 불가능

# in, not in 사용하기
# 튜플 / 스트링 / 리스트 / 문자열 사용 😁
a = [0,10,20,30,40,50]
print(10 in a) # True


# 11.1.2 시퀀스 객체 연결하기
# + 연산자 사용
# 시퀀스 객체1 + 시퀀스 객체2
print('11.1.2 (1) 시퀀스 객체 연결하기')
a = list(range(10,60,10))
b = list(range(60,110,10))
print(a+b)
print()


# 11.1.2 range 객체 연결하기
# Tuple / List로 만들어 연결
print('11.1.2 (2) range 객체 연결하기')
d = range(10,60,10)
e = range(60,110,10)
# print(d+e) # Error
print(list(d) + list(e)) # tuple(d) + tuple(e)
print()

# 11.1.3 시퀀스 객체 반복여 새 시퀀스 객체 만들기
print('11.1.3 시퀀스 객체 반복, 새 시퀀스 객체 만들기')
repetitive_a = 3*a
print(repetitive_a)

# len
print(len(a))
print(a[len(a)-1]) # 마지막 요소

# count
print('Count ')
print(a.count(10)) # 1
print()

# index
print('Index ')
print(a.index(10)) # 0
print()

# del
print('del 객체[인덱스] ')
del a[0] # 0번 인덱스 삭제
print(a)

print('del 객체[슬라이스]')
del a[0:len(a)] # 빈 리스트 반환
print(a)
print()

# slice 객체 이용
a = list(range(10,60,10))
print(str(a) + '에 slice(0,3) 객체 이용')
slice_obj = slice(0,3,1)
print(a[slice_obj])

# 리스크 뒤집기
print('리스트 뒤집기')
reverse_a = a[::-1]
print(reverse_a)