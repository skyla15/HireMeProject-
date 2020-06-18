def selection_sort(l):          # 선택정렬
    n = len(l)
    for i in range(n-1):        # 외부 루프
        least = i               # 현재 인덱스
        for j in range(i+1, n):
            if l[j] < l[least]: # 뒤의 원소 중 가장 작은 값의 인덱스 찾음
                least = j
        l[i], l[least] = l[least], l[i]
        printStep(l, i + 1)

def printStep(l, val):
    print( 'Step %2d = ' % val, end='')
    print(l)


arr = [5,3,8,4,9,1,6,2,7]
print('start  : ', arr )
selection_sort(arr)
print('sorted : ', arr)

