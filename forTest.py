import sys, gc


def delete_me(obj):
    # 자신을 참조하는 객체 리스트를 가져옴
    referrers = gc.get_referrers(obj)
    for referrer in referrers:
        # 그 중 자신에 대한 참조를 하는 '다른 객체'는 딕셔너리 형을 갖고있으므로
        if type(referrer) == dict:
            for k, v in referrer.items():
                # 참조하는 객체가 자신이라면
                if v is obj:
                    # 참조 해제 -> None
                    referrer[k] = None


def test():
    class A:
        pass

    class B:
        def __init__(self, obj):
            self.obj = obj

    a = A()
    b = B(a)

    print("before : ", b.__dict__)
    delete_me(a)
    print("after : ", b.__dict__)
    print("ref count : ", sys.getrefcount(a))
    gc.collect()
    print("ref count : ", sys.getrefcount(a))
    del (a)


# before :  {'obj': <__main__.test.<locals>.A object at 0x7fa4902f02b0>}
# after :  {'obj': None}
# ref count :  4
# ref count :  2
test()