# 얕은 복사는 새로운 복합 객체를 만들고,(가능한 범위까지) 원본 객체를 가리키는 참조를 새로운 복합 객체에 삽입합니다.
# 깊은 복사는 새로운 복합 객체를 만들고,재귀적으로 원본 객체의 사본을 새로 만든 복합 객체에 삽입합니다.
# mutable -> 리스트, 딕셔너리
# immutable -> 튜플, 정수, 문자열

# 리스트 객체는 값을 참조하여 사용

# Same Instance, Same Reference
alias1 = [1,2,3,4,5]
alias2 = alias1
alias2[0] = 10000
print(alias1 is alias2) # True
print(alias1 == alias2) # True
print(alias1) # 10000,2,3,4,5
print()

# Shallow Copy
# Different Instances, Same Reference
# shallow1 과 shallw2 는 서로 다른 복합 객체를 가르킴
# 하지만 복합 객체가 가르키는 참조 주소는 동일함
shallow1 = [[1,2],[3,4],[5,6]]
shallow2 = list(shallow1)
print(id(shallow1[0]), id(shallow2[0]))     # 4447851008 4447851008
print(shallow1 == shallow2)                 # True 참조들의 값이 같음
print(shallow1 is shallow2)                 # False 다른 객체
print()

shallow3 = [1,2,3,4]
shallow4 = list(shallow3)
print(id(shallow3),id(shallow4))        # 복합객체 주소는 다름
print(id(shallow3[0]),id(shallow4[0]))  # 복합 객체의 참조 주소는 같음
shallow4[0] = 10000                     # 재할당 시 주소 새로 받음
print(id(shallow3[0]), id(shallow4[0])) # shallow4[0] 재할당되어 새로운 주소를 받음
print(id(shallow3[1]), id(shallow4[1])) # 재할당된 요소 외에는 계속 같은 값을 참조하고 있음
print()



# Deep Copy