# 35.2 정적 메서드 사용하기
# 정적 메서드와 클래스 메서드 : 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 메서드
#####################################################################
# 정적 메소드 ( 속성 접근이 필요없는 경우에 사용 : 값을 받아 덧셈, 뺄셈 등등 )     ##
###################################################################
# @staticmethod
# 메서드(매개변수,.. )  # self 사용 안함

# @시작하는 것(데코레이터) : 메서드(함수)에 추가 기능을 구현할 때 사용합니다
# - 정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없습니다
# 보통 정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용합니다.
# - 정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는
# 순수 함수(pure function)를 만들 때 사용

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)


Calc.add(10, 20)  # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)  # 클래스에서 바로 메서드 호출


