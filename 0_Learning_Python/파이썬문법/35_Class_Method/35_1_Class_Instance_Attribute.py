# 35.1.1  클래스 속성 사용하기
# __init__ 메서드에서 만들었던 속성은 인스턴스 속성입니다.
# 클래스 속성은 다음과 같이 클래스에 바로 속성을 만듭니다. 클래스 속성은 모든 객체가 공유
# 클래스 외부에서 클래스 속성 접근 : 클래스 이름.클래스 속성

class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(Person.bag)

print(james.bag)
print(maria.bag)



# 35.1.2  클래스 속성 접근하기
# self.(클래스 속성)
# 클래스 이름.(클래스 속성)

class Person:
    bag = []

    def put_bag(self, stuff):
        Person.bag.append(stuff)  # 클래스 이름으로 클래스 속성에 접근
        self.bag.append(stuff)



# 참고 | 속성, 메서드 이름을 찾는 순서
# 파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾습니다.
# 그래서 인스턴스 속성이 없으면 클래스 속성을 찾게 됩니다.
# 따라서 인스턴스 속성에 없는 속성을 사용할 경우에도 클래스 속성을 참조하므로 작동은 됩니다.