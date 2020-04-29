# 6.1.3
import _6_0_ArrayStack as AS

def reverse_file(f):
    '''Overwrite given file with its contents line-by-line reversed'''
    S = AS.ArrayStack()
    with open(f) as original:
        for line in original:
            S.push(line.rstrip('\n'))
            print(line)
    with open(f,'w') as output:
        cnt = 0
        while not S.is_empty():
            output.write('new ' + str(cnt) + ' : ' + S.pop() + '\n')
            cnt += 1


reverse_file('test_6_1_2.txt')