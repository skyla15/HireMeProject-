###########################
# 30.2 키워드 인수 사용하기  ##
###########################################################
# - 키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능
#   키워드=값 형식으로 사용합니다.
# - 인수의 순서 맞추지 않고 호출 가능
# - 참고로 print 함수에서 사용했던 sep, end도 키워드 인수입니다.
#
# 함수(키워드=값)

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')