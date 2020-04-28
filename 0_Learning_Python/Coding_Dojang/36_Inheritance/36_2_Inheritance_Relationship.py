# 36.2.1  상속 관계 (is-a 관계)
# 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용합니다.
# 즉, "학생은 사람이다."라고 했을 때 말이 되면 동등한 관계

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')



# 36.2.2  포함 관계 (has-a 관)
# 상속을 사용하지 않고 속성에 인스턴스를 넣어서 관리

class Person:
    def greeting(self):
        print('안녕하세요.')


class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)