###############################
# 30.4 매개변수에 초깃값 지정하기  ##
##########################################
# def 함수이름(매개변수=값):
#     코드
##########################################


#############################################
# 30.4.1  초깃값이 지정된 매개변수의 위치         ##
# 초깃값이 지정된 매개변수는 뒤쪽에 몰아주어야 합니다  ##
###########################################
def personal_info(name, age, address='비공개'):
    pass
def personal_info(name, age=0, address='비공개'):
    pass
def personal_info(name='비공개', age=0, address='비공개'):
    pass


# 정리
# def personal_info(고정 인수, 가변 위치 변수, 가변 키워드 변수)