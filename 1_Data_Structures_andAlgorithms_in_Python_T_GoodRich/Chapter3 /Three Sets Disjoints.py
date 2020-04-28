import time
import random

# 결과값
# set_1 3.3669999996988054e-06
# set_2 1.5570000000408868e-06
def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        print("{0} {1}".format(func.__name__, time.perf_counter()-t))
    return wrapper


# set_1 : O(n^3)
@benchmark
def set_1(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


# set_2 : O(N^2)
@benchmark
def set_2(A, B, C):
    for a in A:                 # For loop for A : O(n)
        for b in B:             # For loop for B : Total of O(n^2)
            if a == b:          # Therefore, a == b 테스팅 시간 : O(n^2)
                for c in C:
                    if a == c:  # if a == b -> at most n pairs
                                # C 루프에서 사용되는 시간은 따라서 O(n^2)
                        return False
    return True


def main():
    A, B, C = set()

    for i in range(10000):
        r1 = random.randint(0, 1000000000)
        r2 = random.randint(0, 1000000000)
        r3 = random.randint(0, 1000000000)
        A.add(r1)
        B.add(r2)
        C.add(r3)

    set_1(A, B, C)
    set_2(A, B, C)


main()

