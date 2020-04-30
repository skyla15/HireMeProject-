##############################
# 36.6 추상 클래스 사용하기     ##
####################################################
# 파이썬은 추상 클래스(abstract class)라는 기능을 제공합니다.
# 추상 클래스는 메서드의 목록만 가진 클래스이며
# 자식 클래스에서 반드시 구현해야 할 메소드를 정해 줄 때 사용
#####################################################
# from abc import *                                 #
#                                                   #
# class 추상클래스이름(metaclass=ABCMeta):              #
#     @abstractmethod                               #
#     def 메서드이름(self):                            #
#         코드                                       #
#####################################################
# 여기서는 from abc import *로 abc 모듈의 모든 클래스와 메서드를 가져왔습니다.
# 만약 import abc로 모듈을 가져왔다면
# abc.ABCMeta, @abc.abstractmethod로 사용해야합니다.

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')


james = Student()
# james.study()          # 에러 발생, go_to_school 메서드 구현 안했기때문


# 36.6.1  추상 메서드를 빈 메서드로 만드는 이유
# 데 추상 클래스는 인스턴스로 만들 수가 없다는 점입니다.
# 추상 클래스인스턴스를 만들면 에러가 발생

# james = StudentBase()          # 에러 발생, 추상클래스는 객체화 안됨