# Shallow Copy 활용한 풀이

'''
B
1) Shallow Copy
A = list(B)
# B와 다른 객체를 가르키는 객체 A
# 하지만 각각의 객체가 참조하는 주소는 동일
# 객체 안의 객체에는 적용 안됨
ex)
a = [[1,2],[3,4],[5,6]]
b = list(a)
id(a) == id(b) # False
id(a[0]) == id(b[0]) # True
a[0].append(100)
print(b) # [[1,2,100],[3,4],[5,6]]
'''


print(solution(['12', '134']))

