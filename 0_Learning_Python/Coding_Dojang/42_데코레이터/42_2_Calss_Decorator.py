# 클래스로 데코레이터 만들기수
# __init__ : 인스턴스 초기화시
# __call__ : 인스턴스가 호출이 되었을 시 실행

# 매개변수가 없는 클래스 데코레이터
# 인스턴스 호출이 안되었기 때문에 __init__에 인스턴스들 받아옴
class trace :
    def __init__(self, func):                # 호출할 함수를 매개변로 받아옴 (호출하지않았음)
        self.func = func

    def __call__(self, *args, **kwargs):
        print('함수 호출 : {0}'.format(self.func.__name__))     # 호출할 함수의 매개변수
        r = self.func(*args)                 # 인자로 받은 함수 호출, () < 함술르 호출함
        print('함수 종료 : {0}'.format(self.func.__name__))


@trace
def multiple(*args):
    return sum(args)

multiple(1,2,3,4,5)


print('')

# 클래스로 매개변수를 받는 데코레이터 만들기
# x를 매개변수로 받으면서 인스턴스가 호출이 되기에
# __call__함수에서 func함수를 받아옴
class trace2 :
    def __init__(self, x):
        self.x = x

    def __call__(self, func):        # 호출할 함수를 매개변수로 받아옴 -> __call__이 데코레이터 역할
        def new_multiple(*args) :    # 내부 함수 생성
            r = func(*args)
            print('new_miultiple : {0}'.format(str(r * self.x)))
            return r                # func의 반환값 반환
        return new_multiple         # 새로 만든 함수 반환

@trace2(3)
def multiple(*args):
    return sum(args)

multiple(1,2)





