import time

# prefix_average1, 4.465381860733032
# prefix_average2, 0.6748650074005127
# prefix_average3, 0.0021581649780273438

def benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('{}, {}'.format(func.__name__, end_time-start_time))
        return result
    return wrapper



@benchmark
def prefix_average1(S):
    n = len(S)
    A = [0] * n                     # Each entry is muliplied by [0] => O(n)
    for j in range(n):
        total = 0
        for i in range(j+1):        # nested Loop (j+1), j, j-1 ... 0 -> n (( n+1 ) + 1) / 2
            total += S[i]           # O(n^2)
        A[j] = total / (j + 1)


@benchmark
def prefix_average2(S):
    n = len(S)
    A = [0] * n                         # Each entry is muliplied by [0] => O(n)
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j + 1)  # Using sum function -> O(j+1)
                                        # Using slicing -> O(j+1)
                                        # Slicing, sum function
                                        # -> construct a new list and store a new list
                                        # O(n^2)


@benchmark
def prefix_average3(S):
    n = len(S)              # constant time
    A = [0] * n             # O(n)
    total = 0               # constant time
    for j in range(n):
        total += S[j]        # constant time
        A[j] = total / (j + 1) # constant time
                             # O(n)


def main():
    S = []
    for i in range(10000):
        S.append(i)

    prefix_average1(S)
    prefix_average2(S)
    prefix_average3(S)


main()




