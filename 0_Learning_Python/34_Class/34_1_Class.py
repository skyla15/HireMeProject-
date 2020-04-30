# 참고 : 모든 클래스는 object 클래스를 상속받음
# class X : 와 class X(object) : 는 같은 의미

# 34.1 클래스와 메서드 만들기, 호출하기
# 메서드의 첫 번째 매개변수는 반드시 self를 지정해야 합니다.
# class 클래스:
#     def 메서드(self):
#         코드
#
# 인스턴스 = 클래스()
# 인스턴스.메서드()
#
# 34.1.3  인스턴스와 객체의 차이점?
# 객체만 지칭할 때는 그냥 객체(object)라고 부릅니다.
# 하지만 클래스와 같 말할 때는 인스턴스(instance)라고 부릅니다.
# 그래서 다음과 같이 리스트 변수 a, b가 있으면 a, b는 객체입니다.
# 그리고 a와 b는 list 클래스의 인스턴스
# a = list(range(10))
# b = list(range(20))
#
#
# 참고 | 메서드 안에서 메서드 호출하기
# 메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 합니다.
# self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이 되므로 주의해야 합니다
#
# def greeting(self):
#     print('Hello')
#
# def hello(self):
#     self.greeting()  # self.메서드() 형식으로 클래스 안의 메서드를 호출
#
# james = Person()
# james.hello()  # Hello
#
#
# 참고 | 특정 클래스의 인스턴스인지 확인하기
# isinstance(인스턴스, 클래스)
# 현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용합니다.
# 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환합니다.
#
# - 주로 객체의 자료형을 판단할 때 사용
# - 예를 들어 팩토리얼 함순느 1부터 n까지 양의 정수를 차례대로 곱해야합니다.
#   하지만 실수와 음의 정수는 계산할 수 없습니다.
#   이럴 때 isinstance를 사용하여 숫자가 정수일 때만 계산하도록 함

def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)