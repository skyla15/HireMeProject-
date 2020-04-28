######################################
# 성능 테스트 timeit모듈, Timer 객체 이용  #
#####################################
# 아래 테스트에서는 timeit 모듈의 Timer 객체를 생성해 사용한다.
# Timer 객체의 첫 번째 매개변수 는 우리가 측정하고자 하는 코드이며,
# 두 번째 매개변수는 테스트를 위한 설정 문 이다.
# imeit 모듈은 명령문을 정해진 횟수만큼 실행하는 데 걸리는 시간을 측정 한다(기본값은 number = 1000000이다).
# 테스트가 완료되면 문장이 수행된 시간(ms)를 부동소수점 값으로 반환


import timeit

# for i in range(10000,1000001,20000):
#     t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     x = {j: None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
# print("random.randrange(%d) in x" % 1000)
#
#
def test():
    l = []
    for i in range(1000):
        print('test')
        l.append(i)


def banchmarking(func):
    t = timeit.Timer("%s"%str(func), "from __main__ import test")
    print(t.timeit(number=100000))


banchmarking(test())