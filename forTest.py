def solution1(n, m):
    a = ('*' * n + '\n')
    b = (m-1)
    print(a*b, len(a))


def solution2(a, b):
    for i in range(b):
        k = ''
        for j in range(a):
            k += '*'
            print(k, len(k))
            print('*', end='')
        print()


def solution(n, m):
    print(('*' * n + '\n') * (m-1)
          + '*' * n)


print('a', 'b', 'c', sep='\n', end = '\n\n')


# solution2(5,3)
solution1(5,3)
solution2(5,3)



