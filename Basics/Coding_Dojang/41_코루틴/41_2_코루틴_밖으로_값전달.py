# 41_2_코루틴 밖으로 값 전달하기
# (yield 변수) 형식으로 yield에 변수를 지정한 뒤 괄호로 묶어주면
# 값을 받아오면서 밖으로 값을 전달
# 전달된 값은 next와 send메소드의 반환값으로 나옴
#
# 값을 받으면서 반환 : 변수 = (yield 변수)
# 코루틴으로 값 받음 : 변수 = next(코루틴객체)
# 코루틴으로 값 받음 : 변수 = 코루틴객체.send(값)

def sum_coroutine() :
    total = 0
    while True :
        x = (yield total)   # 코루틴 바깥에서 값을 받아오면서 바깥으로 값 전달
        total += x

co = sum_coroutine()
print(next(co))         # 코루틴 초기 실행
print(co.send(1))
print(co.send(2))
print(co.send(3))