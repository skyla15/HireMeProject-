# 36.3.1  super()로 기반 클래스 초기화하기
# super().__init__ 없이 부모 클래스의 속성을 사용하면 에러 발생(부모의 인스턴스 생성 안됨)
# 만약 자식 클래스에 __init__() 메소드가 없다면
# 부모클래스의 __init()__이 실행되기에 부모클래스 초기화 필요없음
#
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'


james = Student()
print(james.school)
print(james.hello)


# 36.3.2  부모 클래스를 초기화하지 않아도 되는 경우
# 만약 자식 클래스에 __init__() 메소드가 없다면
# 부모클래스의 __init()__이 실행되기에 부모클래스 초기화 필요없음

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    pass


james = Student() # Person __init__ 출력
print(james.hello)



# 참고 | 좀 더 명확하게 super 사용하기
# super는 다음과 같이 파생 클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있습니다.
# 물론 super()와 기능은 같습니다.
# super(파생클래스, self).메서드

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()     # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'
