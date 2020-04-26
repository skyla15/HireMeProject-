#####################
# 34.2 속성 사용하기  ##
##########################################
# __init__ 메서드 안에서 self.속성에 값을 할당합니다
# __init__ 메서드는 인스턴스(객체)를 초기화합니다.
# 매직 메서드 ( 스페셜 메서드 )
# -> 밑줄 두개(__)가 붙은 메소드
# -> 파이썬이 자동으로 호출해주는 메서드
##########################################
print('34.2')
class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

def greeting(self):
    print(self.hello)

james = Person()
james.greeting()  # 안녕하세요.

########################
# 34.2.1  self의 의미   ##
##########################################
# self는 인스턴스 자기 자신을 의미합니다.
# 즉 위의 예제에서 self = Person() 자기 자신을 의미
# james = Person() 호출 시
# __init__(self)의 매개변수 self에 Person() 들어감
#
#
# 34.2.2  인스턴스를 만들 때 값 받기
# class 클래스이름:
#     def __init__(self, 매개변수1, 매개변수2):
#         self.속성1 = 매개변수1
#         self.속성2 = 매개변수2



#####################################################################
# 참고 | 특정 속성 사용 제한하기 : __slots__ = ['속성이름', '속성이름'..]     ##
####################################################################################
print('__slots__ = [ 속성 ] 사용하여 속성 비활성화 시키기')
class Person:
    __slots__ = ['name', 'age']
    # name, age 속성만 사용. # address 속성은 Person의 속성으로 인식 안됨

    def __init__(self, name='셀프', age=0, address='한'):  # 키워드 인수
        self.name = name
        self.age = age
        self.address = address

maria = Person()
maria.name = '마리아'
maria.age = 30
# maria.address = '서울'
print('name : {0}, age : {1}, address : {2}'.format(maria.name, maria.age))


########################################
# 참고 | 클래스의 위치 인수, 키워드 인수 사용   ##
############################################
# 위치인수와 리스트 언패킹 사용
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])

# 키워드 인수와 딕셔너리 언패킹 사용
class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})