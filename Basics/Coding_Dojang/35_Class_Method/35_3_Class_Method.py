# 정적 메서드와 클래스 메서드 : 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 메서드
#######################################################
# 클래스 메서드 ( 클래스 속성, 클래스 메소드에 접근 시 사용 )     ##
######################################################
# @classmethod
# 클래스 메서드(cls, 매개변수.. )

# 클래스 외부에서 클래스 메소드 호출 방법 : 클래스이름.클래스 메소드()
# 이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 합니다
class Person:
    count = 0  # 클래스 속성

    def __init__(self):
        Person.count += 1  # 인스턴스가 만들어질 때
        # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근

james = Person()
maria = Person()

Person.print_count()  # 2명 생성되었습니다.


# 특히 cls를 사용하면 메서드 안에서 현재 클래스의 인스턴스를 만들 수도 있습니다.
# 즉, cls는 클래스이므로 cls()는 Person()과 같습니다.

class Person() :
    @classmethod
    def create(cls):
        p = cls()    # cls()로 인스턴스 생성
        return p