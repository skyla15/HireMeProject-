##########################################
# 39.3 인덱스로 접근할 수 있는 이터레이터 만들기  ##
##############################################################
# __iter__, __next__이 없어도
# __getitem__ 메소드만 있어도 클래스는 이터레이터가 됩니다.
# ####################################
# class 이터레이터이름:                  #
#     def __getitem__(self, 인덱스) :  #
#         코드                        #
###############################################################


class Counter:
    def __init__(self, stop):
        self.stop = stop            # 반복을 끝낼 숫자

    def __getitem__(self, index) :  # 인덱스를 받음
        if index < self.stop:       # 인덱스가 반복을 끝낼 숫자보다 작은 경우
            return index            # 인덱스 반환
        else:
            raise IndexError


print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end=' ')