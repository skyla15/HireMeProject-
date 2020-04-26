import math

# 클래스로 두 점 사이의 거리 구하기

class Point2D :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 2D 좌표 점

p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2

print('p1: {} {}'.format(p1.x, p1.y))
print('p2: {} {}'.format(p2.x, p2.y))

a = p2.x-p1.x
b = p2.y-p1.y

c = math.sqrt((a*a) + (b*b))
c = math.sqrt(a**2 + b**2)
c = math.sqrt(math.pow(a, 2) + math.pow(b,2))
print('%.2f' % c)


# namedtuple 사용 하기 (collections 모듈)
# 클래스 = collections.namedtuple('자료형이름', ['요소이름1', '요소이름2'])
# namedtuple로 생성한 클래스는 값을 넣어서 인스턴스를 만들 수 있으며
# 인스턴스.요소이름 또는 인스턴스[인덱스] 형식으로 요소에 접근할 수 있습니다.
# 인스턴스 = 클래스(값1, 값2)
# 인스턴스 = 클래스(요소이름1=값1, 요소이름2=값2)
# 인스턴스.요소이름1
# 인스턴스[인덱스]

import math
import collections

Point2D = collections.namedtuple('Point2D', ['x', 'y'])  # namedtuple로 점 표현

p1 = Point2D(x=30, y=20)  # 점1
p2 = Point2D(x=60, y=50)  # 점2


a = p1.x - p2.x  # 선 a의 길이
b = p1.y - p2.y  # 선 b의 길이

c = math.sqrt((a * a) + (b * b))
print(c)  # 42.42640687119285