# 34.3 비공개 속성 사용하기
# - 비공개 속성은 클래스 안의 메소드를 통해서만 접근 가능
# - 비공개 속성은 __속성과 같이 이름이 __(밑줄 두 개)로 시작
# - 단, __속성__처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이 아니므로 주의해야 합니다.

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        self.__wallet -= amount  # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
#
#
# maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# # maria.__wallet -= 10000  # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
# maria.pay(3000)


# 34.4 비공개 메소드 사용하기
# - 메서드 이름이 __(밑줄 두 개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 됩니다.
# - 보통 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 만듬
# - 예를 들어, 게임 내에서 캐릭터가 스킬을 쓰면 마나를 소비한다고 할 때,
#   스킬 : 퍼블릭 메소드, 마나 소비 : 프라이빗 메소드

class Person:

    def __greeting(self):
        print('Hello')

def hello(self):
        self.__greeting()  # 클래스 안에서는 비공개 메서드를 호출할 수 있음
james = Person()
# james.__greeting()  # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음