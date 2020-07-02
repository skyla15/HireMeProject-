import sys
print(sys.path)
sys.path.append('모듈 디렉토리')

prices = [7, 1, 5, 3, 4, 6]
print(prices)
print(prices[1:])
print(list(zip(prices, prices[1:])))
print([b - a for a, b in zip(prices, prices[1:]) if b - a > 0])
print(sum([b - a for a, b in zip(prices, prices[1:]) if b - a > 0]))


## Map
a = [1,2,3,4,5]
b = 10, 20, 30, 40, 50

map_ab = list(map((lambda a, b : a * b), a, b))


users = [
    {'mail': 'gregorythomas@gmail.com',
     'name': 'Brett Holland',
     'sex': 'M',
     'age': 73},
 {'mail': 'hintoncynthia@hotmail.com',
  'name': 'Madison Martinez',
  'sex': 'F',
  'age': 29},
 {'mail': 'wwagner@gmail.com',
  'name': 'Michael Jenkins',
  'sex': 'M',
  'age': 51},
 {'mail': 'daniel79@gmail.com',
  'name': 'Karen Rodriguez',
  'sex': 'F',
  'age': 32}
]

from functools import reduce
mails = reduce(lambda prev_user, cur_user : prev_user +[cur_user['mail']], users, [])
print(mails)

accumulator = reduce(lambda x, y : x + y, a, 100)
print(accumulator)