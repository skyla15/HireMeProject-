#####################
# 38.4 예외 만들기   ##
#####################################################
# - 모든 예외는 Exception 클래스를 상속 받아서 만듬
# - 사용자 정의 예외 또한 Exception 클래스를 상속 받아서 새로운 클래스 생성하여 사용
# ####################################################
# class 예외이름(Exception):                           #
#     def __init__(self):                           #
#         super().__init__('에러메시지')               #
#####################################################

class NotThreeMultipleError(Exception):  # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:  # x가 3의 배수가 아니면
            raise NotThreeMultipleError  # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)

three_multiple()


# 참고 | 다음과 같이 Exception만 상속받고 pass를 넣어서 아무것도 구현하지 않아도 됩니다.

class NotThreeMultipleError(Exception):    # Exception만 상속받고
    pass                                   # 아무것도 구현하지 않음