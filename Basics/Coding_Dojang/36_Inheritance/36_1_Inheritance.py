# Unit 36. 클래스 상속 사용하기
# 클래스 상속은 다음과 같이 클래스를 만들 때 ( )(괄호)를 붙이고 안에 부 클래스 이름을 넣습니다
# class 부모클래스이름:
#     코드
# class 자식클래스이름(부모클래스이름):
#     코드


class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')


james = Student()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Student에 추가한 study 메서드


