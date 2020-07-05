
'''
버블정렬
항상 O(n^2)
'''
def bubble_sort(a):
    seq = list(a)
    print('bubble sort')
    print('==========================')
    length = len(seq) - 1
    for i in range(length, 0, -1):
        for j in range(i):
            if seq[j] >= seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
                print(seq)
    print('==========================')
    return seq


'''
선택정렬 
리스트에서 가장 적거나 큰 항목을 찾아서 첫번째 항목과 위치를 바꾼다.
그 다음 항목을 찾아서 두 번째 항목과 위치를 바꾼다.
이 과정을 리스트의 끝까지 반복한다. 
항상 O(n^2)
'''
def selection_sort(a):
    seq = list(a)
    print('selection sort')
    print('==========================')
    length = len(seq)
    for i in range(length-1):
        small = i
        for j in range(i+1, length):
            if seq[small] > seq[j]:
                small = j
        seq[i], seq[small] = seq[small], seq[i]
        print(seq)
    print('==========================')
    print()
    return seq


'''
삽입정렬 
최선 : O(n)
평/최악 : O(n^2) 
배열의 처음 부분을 계속하여 정렬시키고 
정렬되지 않은 뒤쪽의 원소를 배열된 부분에 삽입하는 정렬 
데이터가 작고, 이미 정렬되어있는 경우라면, 병학/퀵 정렬보다 성능이 좋다 
'''
def insertion_sort(a):
    seq = list(a)
    print('insertion sort')
    print('==========================')
    for i in range(1, len(seq)):
        while j > 0 and seq[j-1] > seq[j]:
            # for 문을 쓰게 될 경우, O(n^2) 이 되므로 while문으로 들어간다
            seq[j-1], seq[j] = seq[j], seq[j-1]
        print(seq)
    print('==========================')
    print()
    return seq


'''
놈정렬 
앞으로 이동하면서 값을 비교하고 
정렬이 되어있지 않다면 뒤로 이동하면서 다시 정렬시키고 앞으로 이동하는 정렬최소 
O(n)
최악 / 평균 : O(n^2) 
'''
def gnome_sort(a):
    seq = list(a)
    i = 0
    print('gnome sort')
    print('==========================')
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
            print(seq)
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1
        print(seq)
    print('==========================')
    print()
    return seq


def main():
    test_list = [31,13,22,4,43,11,2]
    print(test_list)
    print( bubble_sort(test_list) )
    print( selection_sort(test_list) )
    print( insertion_sort(test_list))
    print( gnome_sort(test_list))

main()
