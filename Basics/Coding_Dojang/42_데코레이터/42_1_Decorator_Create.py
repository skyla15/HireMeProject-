# 데코레이터란?
# 하나의 함수를 취해서 다른 함수를 반환하는 함수
# 1) 내부 함수
# 2) 함수 인자
# 3) *args, kwargs
# 데코레이터 실행 -> 함수 인자 '호출' -> 내부함수에 새로운 함수 정의 -> 새로운 함수 반환



# 1 데코레이터 객체를 직접 받아 사용하기
#####
def trace(func):                        # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):        # 내부함수 및 func 매개변수 받음
        print(func.__name__, '함수 시작') # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')

    return wrapper  # wrapper 함수 반환

def hello():
    print('hello')
trace_hello = trace(hello)   # 데코레이터에 호출할 함수를 넣음
trace_hello()                # 데코레이터를 통해 새로운 함수를 받음 (wrapper)



# 2 데코레이터 @ 사용
def trace2(func):                        # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):        # 내부함수 및 func 매개변수 받음
        print(func.__name__, '함수 시작') # __name__으로 함수 이름 출력
        print('max :', max(args))
        print('args : {0:<10}'.format(str(args)))
        print(func.__name__, '함수 끝')

    return wrapper  # wrapper 함수 반환

@trace2                     # @데코레이터
def get_max(*args):         # 위치 인수를 사용하는 가변 인수 함수
    return max(args)

get_max(1,2,3,4,5,6)        # get_max에 데코레이터 적용



# 3 데코레이터에 인자 전달하기 -> 2개의 내부 함수를 이용
# 가장 밖의 함수는 매개변수를 받기위해 사용
# 내부 함수 2개 다 반환
def trace3(x) :
    def real_decorator(func) :
        # 기존의 함수 결과 ( 두 수의 합 )에 x를 곱하여 반환
        def new_func(*args, **kwargs) :
            if args :
                r = func(*args)
                print('multiple : {0}'.format(str(r*x)))
            if kwargs :
                print(kwargs)
        return new_func     # 새로운 함수 객체 반환
    return real_decorator   # 데코레이터 객체 반환

@trace3(3)
def multiple(*args) :
    return sum(args)

multiple(1,2)               # (1+2)*3



