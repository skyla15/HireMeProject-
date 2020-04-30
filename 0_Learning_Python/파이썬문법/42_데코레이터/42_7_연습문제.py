
def type_check(type_a, type_b) :
    def decorator(func) :
        def check(a,b) :
            if type_a != type(a) or type_b != type(b) :
                raise RuntimeError('Unexpected Error Occured')
            else :
                return func(a,b)
        return check
    return decorator

@type_check(int,int)
def add(a,b) :
    return a + b

print(add(10,20))
# print(add('10','20'))



def decorator2(func) :
    def check(*args, **kwargs) :
        print('decortor created : {}'.format(func.__name__))
        ''' 
        기능 추가하고 싶은 함수 추가 
        '''
        print(func(*args))
        print('decortor ended : {}'.format(func.__name__))
    return check

@decorator2
def add2(*args) :
    return sum(args)

r = list(map(int,input().split()))
add2(*r)




def kwargs_testing(**kwargs) :
    print(kwargs)

kwargs = { 'a' : 1, 'b' : 2, 'c' : 3 }
kwargs_testing(**kwargs)




