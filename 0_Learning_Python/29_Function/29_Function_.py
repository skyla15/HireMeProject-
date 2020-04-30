# 참고 | 빈 함수 만들기
# 내용이 없는 빈 함수를 만들 때는 코드 부분에 pass를 넣어줍니다.
# def hello():
#     pass

#####################################
# 29.4 함수에서 값을 여러개 반환하기      ##
####################################
# def 함수이름(매개변수):
#     return 반환값1, 반환값2
#
# def add_sub(a, b):
# ...     return a + b, a - b
####################################


################################
# 참고 | 값 여러 개를 직접 반환하기  ##
###############################
# return에 튜플/리스트 반환
#
# def one_two():
# ...     return [1, 2]
#
# def one_two():
# ...     return 1,2 # 괄호 없이 값을 콤마로 구분시 튜플
#
# def one_two():
# ...     return (1,2)
####################################


###########
# 연습문제 ##
####################################
# 회문 판별하기 ( 유전자 염기 서열에서 많이 사용 )
# word = input('단어 입력 : ')
# for i in range(len(word)-1) :
#     if word[i] != word[-1-i] :
#         print(False)
# print(True)

# N-gram 만들기
word = input('단어 입력 : ')
N = int(input('N : '))
cnt = 0
for i in range(len(word)-1) :
    for j in range(N) :
        print(word[cnt+j], end='')
    cnt += 1

    if i == len(word)-N :
        break;
    print()
print()
print()

# 재귀호출로 회문 판별하기
def palindrome(word) :
    # 재귀호출 종료 조건 1
    if(len(word) < 2) :
        return True
    # 재귀호출 종료 조건 2 : 양 끝 단어 다른 경우
    elif word[0] != word[-1] :
        return False
    else :
        palindrome(word[1:-1])
        # 슬라이싱으로째 2번째 단어부터 맨 끝에서 2번째 단어까지 전달

print(palindrome('hello'))
print(palindrome('level'))

# 재귀호출로 피보나치 구하기
# 다음 번 피보나치 수는 바로 앞의 두 피보나치 수의 합
def fib(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1

    if n >= 2 :
        return fib(n-2) + fib(n-1)

n = int(input())
for i in range(n) :
    print(fib(i))