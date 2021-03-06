############################
# 33.3 클로저 사용하기        ##
############################
# 클로저
# - 함수를 둘러싼 환경(지역변수, 코드)를 "유지"하다 호출 시 사용하는 함수
#   => 클로저를 사용하면 지역변수를 변경하여도 값 유지됨 => 연습문제 !!!!!!!
# - 클로저에 속한 지역 변수는 외부에서 직접 접근 불가능 => 지역 변수(데이) 숨기기
# - 보통 람다로 사용


################################################
# (1) 함수 클로저 : 함수를 반환  ##
############################
# def calc():
#     a = 3
#     b = 5
#     def mul_add(x):
#         return a * x + b
#         # 함수 바깥쪽에 있는 지역 변수 a, b 사용하여 값 반환
#         # 하지만 a, b에 직접 접근 불가능
#     return mul_add
#         #mul_add 함수를 반환
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))
################################################


################################################
# (2) 람다 클로저 : 람다를 반환  ##
#############################
# a = 3
# b = 5
# return lambda x: a * x + b  # 람다 표현식을 반환
#
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))
################################################


#################################################
# 33.3.2  클로저의 지역 변수 변경하기                ##
# 클로저의 지역 변수를 변경하고 싶다면 nonlocal을 사용  ##
###############################################
# def calc():
#     a = 3
#     b = 5
#     total = 0
#
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#
#     return mul_add
#
# c = calc()
# c(1) # 8 : total = 0 + 3 * 1 + 5
# c(2) # 19 : total = 8 + 3 * 2 + 5
# c(3) # 33
############################################################


#########################################################
# 33.1.1  함수 안에서 전역 변수 변경하기터                    ##
# 함수의 단계 상관없이 global 키워드는 무조건 전역변수 사용       ##
# global 전역변수                                      ##
######################################################
# x = 10          # 전역 변수
# def foo():
#     global x    # 전역 변수 x를 사용하겠다고 설정
#     x = 20      # x는 전역 변수
#     print(x)    # 전역 변수 출력
#
#
# 참고 | 네임스페이스 : locals() - 네임스페이스 딕셔너리 형태로 출력
# 파이썬 변수는 네임스페이스(namespace, 이름공간)에 저장
# locals 함수를 사용하면 현재 네임스페이스를 딕셔너리 형태로 출력
##############################################################


#######################################
# 33.2 함수 안에서 함수 만들기          ##
# 파이썬에서는 함수에서 변수를 만들면     ##
# 항상 현재 함수의 지역 변수가 됩니다.  ##
################################
# def 함수이름1():
#     코드
#     def 함수이름2():
#         코드
#######################################


################################################################################
# 33.2.2  지역 변수 변경하기(현재 함수 밖의 지역 변수 값 변경)                           ##
# nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 먼저 찾습니다   ##
# nonlocal 지역변수                                                          ##
############################################################################
# def A():
#     x = 10
#     y = 100
#     def B():
#         x = 20
#         def C():
#             nonlocal x
#             nonlocal y
#             x = x + 30
#             y = y + 300
#             print(x)    # 50
#             print(y)    # 400
#         C()
#     B()
# A()
##############################################################################







# 연습문제
# 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 호출 횟수가 출력되게 만드세요.
# 여기서는 함수를 클로저로 만들어야 합니다.
def counter() :
    i = 0
    def count() :
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10) :
    print(c(), end=' ')

# 심사문제 : 카운트다운 함수 만들기
# 표준 입력으로 정수가 입력됩니다.
# 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 숫자가 1씩 줄어들게 만드세요.
# 여기서는 함수를 클로저로 만들어야 합니다.
print('\n심사 문제 : ')
def countdown(n) :
    count = n + 1

    def cnt_dwn() :
        nonlocal count
        count -= 1
        return count
    return cnt_dwn

n = int(input())
c = countdown(n)
for i in range(n) :
    print(c(), end=' ')
