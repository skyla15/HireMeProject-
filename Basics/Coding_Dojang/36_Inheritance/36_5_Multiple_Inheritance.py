# 36.5.1 다중 상속 사용하기
# 파이썬의 다중상속 사용 시, 클래스의 목록 중, 왼쪽에서 오른쪽 순서로 메소드를 찾음
# 따라서 같은 메소드가 있을 경우 '기반클래스이름1'의 메소드가 호출됨
# class 부모클래스이름1:
#     코드
# class 부모클래스이름2:
#     코드
# class 자식클래스이름(기반클래스이름1, 기반클래스이름2):
#     코드


class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()  # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드



# 36.5.2 다이아몬드 상속
# 절대 사용해서는 안되는 상속방법
# A,B,C가 같은 이름의 매소드를 가질 경우, 어떤 것을 호출해야하는 지 모호 => 에러 발생 가능성
class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
class D(B, C):
    pass

x = D()
x.greeting()  # 안녕하세요. B입니다.

#     A
#   /   \
# B       C
#   \   /
#     D



# 36.5.2  메서드 탐색 순서 확인하기(MRO, Method Resolution Order)
# 파이썬에서의 다이아몬드 상속 해결책으로 사용 시, 메소드 탐색 순서가 나옴
# 클래스.mro()
# 파이썬의 다중상속 사용 시, 클래스의 목록 중, 왼쪽에서 오른쪽 순서로 메소드를 찾음
# 따라서 같은 메소드가 있을 경우 '기반클래스이름1'의 메소드가 호출됨
#
# >>> D.mro()
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# 참고 | object 클래스
# 파이썬에서 object는 모든 클래스의 조상입니다. 그래서 int의 MRO를 출력해보면 int 자기 자신과 object가 출력됩니다.
# >>> int.mro()
# [<class 'int'>, <class 'object'>]
# 파이썬 3에서 모든 클래스는 object 클래스를 상속받으므로 기본적으로 object를 생략합니다. 다음과 같이 클래스를 정의한다면
# class X:
#     pass
# 괄호 안에 object를 넣은 것과 같습니다.
# class X(object):
#     pass
