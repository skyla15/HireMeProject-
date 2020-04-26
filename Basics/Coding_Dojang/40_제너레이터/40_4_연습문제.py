# 다음 소스 코드에서 words.txt 파일을 한 줄씩 읽은 뒤
# 내용을 함수 바깥에 전달하는 제너레이터를 작성하세요.
# 파일의 내용을 출력할 때 파일에서 읽은 \n은 출력되지 않아야 합니다
# (단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

def file_read():
    with open('words.txt') as file:
        while True :
            line = file.readline()
            if line == '' :
                break
            yield line.strip('\n')


for i in file_read():
    print(i)




# 표준 입력으로 정수 두 개가 입력됩니다
# (첫 번째 입력 값의 범위는 10~1000, 두 번째 입력 값의 범위는 100~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요.
# 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수입니다.

# def prime_number_generator(n1, n2) :
#     cnt = 1
#     for i in range(n1,n2+1) :
#         for j in range(2,i+1) :
#             if i % j == 0 and i != j :
#                 cnt += 1
#         if cnt == 1 :
#             yield i
#         cnt = 1

def prime_number_generator(n1, n2) :
    for i in range(n1, n2) :
        is_prime = True
        for j in range(2,i) :
            if i % j == 0 :
                is_prime = False
                break
        if is_prime == True :
            yield i

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g :
    print(i, end=' ')



