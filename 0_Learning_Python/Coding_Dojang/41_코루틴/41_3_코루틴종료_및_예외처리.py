41.3 코루틴을 종료하고 예외 처리하기
코루틴을 강제 종료하기 위해서는 코루틴객체.close() 사용
코루틴 객체에서 close 메서드를 사용하면 코루틴이 종료됩니다.
=> 이 때 GeneratorExit 예외 발생
사실 파이썬 스크립트가 끝나면 코루틴도 끝나기 때문에 close를 사용하지 않은 것과 별 차이가 없습니다.
하지만 close는 코루틴의 종료 시점을 알아야 할 때 사용하면 편리합니다.


def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')


co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()  # 코루틴 종료


41.3.1  GeneratorExit 예외 처리하기
코루틴 객체에서 close 메서드를 호출하면 코루틴이 종료될 때 GeneratorExit 예외가 발생합니다.
따라서 이 예외를 처리하면 코루틴의 종료 시점을 알 수 있습니다.


def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:  # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')


co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()


41.3.2  코루틴 안에서 예외 발생시키기
코루틴 안에 예외를 발생시켜 코루틴을 종료해보겠습니다.
코루틴 안에 예외를 발생 시킬 때는 throw 메서드를 사용합니다

코루틴객체.throw(예외이름, 에러메시지)

코루틴 바깥에서는 co.throw(RuntimeError, '예외로 코루틴 끝내기')와 같이
throw 메서드에 RuntimeError 예외와 에러 메시지를 지정하면 코루틴 안에서 예외가 발생합니다.
그리고 코루틴 안의 except에서 yield를 사용하여 바깥으로 전달한 값은 throw 메서드의 반환값으로 나옵니다

try:
    total = 0
    while True:
        x = (yield)
        total += x
except RuntimeError as e:
    print(e)
    yield total  # 코루틴 바깥으로 값 전달

co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))  # 190
# 코루틴의 except에서 yield로 전달받은 값


