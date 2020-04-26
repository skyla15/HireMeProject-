41.4 하위 코루틴의 반환값 가져오기
제너레이터에서 yield from을 사용하면 값을 바깥으로 여러 번 전달한다고 했습니다('40.3 yield from으로 값을 여러 번 바깥으로 전달하기' 참조).
하지만 코루틴에서는 조금 다르게 사용합니다.
yield from에 코루틴를 지정하면 해당 코루틴에서 return으로 반환한 값을 가져옵니다
(yield from은 파이썬 3.3 이상부터 사용 가능)

변수 = yield from 하위 코루틴()


def accumulate():
    total = 0
    while True:
        x = (yield)  # 코루틴 바깥에서 값을 받아옴
        if x is None:  # 받아온 값이 None이면
            return total  # 합계 total을 반환
        total += x


def sum_coroutine():
    while True:
        total = yield from accumulate()  # accumulate의 반환값을 가져옴
        print(total)


co = sum_coroutine()
next(co)

for i in range(1, 11):  # 1부터 10까지 반복
    co.send(i)  # 코루틴 accumulate에 숫자를 보냄
co.send(None)  # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄


41.4.1  StopIteration 예외 발생시키기

raise StopIteration(값)

코루틴도 제너레이터이므로 return을 사용하면 StopIteration이 발생합니다.
그래서 코루틴에서 return 값은 raise StopIteration(값)처럼 사용할 수도 있습니다(파이썬 3.6 이하).
이렇게 raise로 StopIteration 예외를 직접 발생시키고 값을 지정하면
yield from으로 값을 가져올 수 있습니다
(단, 파이썬 3.7부터는 제너레이터 안에서
raise로 StopIteration 예외를 직접 발생시키면
RuntimeError로 바뀌므로 이 방법은 사용할 수 없습니다.
파이썬 3.7부터는 그냥 return 값을 사용해주세요).

def accumulate():
    total = 0
    while True:
        x = (yield)  # 코루틴 바깥에서 값을 받아옴
        if x is None:  # 받아온 값이 None이면
            raise StopIteration(total)  # StopIteration에 반환할 값을 지정(파이썬 3.6 이하)
        total += x


def sum_coroutine():
    while True:
        total = yield from accumulate()  # accumulate의 반환값을 가져옴
        print(total)


co = sum_coroutine()
next(co)

for i in range(1, 11):  # 1부터 10까지 반복
    co.send(i)  # 코루틴 accumulate에 숫자를 보냄
co.send(None)  # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄