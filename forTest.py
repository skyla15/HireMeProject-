#
#
# # 프로그래머스 쇠막대기
# from collections import deque
#
# def solution2(arrangement):
#     answer = 0
#     cnt = 0
#     s = deque()
#     #
#
#
# '''ㅏ
# ( ( ( ) ) )
#      |
#   ___ ___
# _____ _____
#
#
# '''
#
# def main():
#     arr = [1, 2, 3, 3, 3, 3, 3, 4, 4]
#     arrangement = "()(((()())(())()))(())"
#     # print( solution1(arr) )
#     solution2(arrangement)
#
# main()
#
#


# test = 'a&b&c'
# a = test.split('&')
# print(a)

a = 'apple'
b = 'pine'
k = [b, a]
res = '&'.join(k)
print(res)
print('-'*100)

a = '짝홀짝홀짝홀'
print(a[::2])

H = '010-1234-5678'
print((H.split('-')[1]))

lst = ['We', 'are', 'the', 'World']
ans = ' '.join(lst)
print(ans)

a = [8, 8, 8]
b = [1, 5]
c = a + b

movie = ['Aladin', 'ToyStory', 'Parasite']
movie.insert(2, 'Superman Returns')
print(movie)

num = [1, 2, 3, 4, 5]
print( sum(num) / len(num) )

num1 = [1,2,3,4,5,6,7,8]
print(num1[::2], num1[1::2], num1[::-1])


wish = ('구글', '아마존' )
print(type(list(wish)))


# 백준문제
# from collections import deque
# n = int(input())
# D = deque(range(1,n+1))
# print(D)
# while len(D) > 0:
#     # 1. 맨 위의 카드를 버림
#     print(D.popleft())
#     D.rotate(-1)
#     print(D)


a = {'gender':'female', 'age':30, 'name':'Kim'}
print(a)


d = {(1,2,3) : 'data'}
print(d[(1,2,3)])


d2 = {'a' : [1,2,3]}
print(d2['a'][0], d2['a'][1], d2['a'][2])


icecream = { '올때메로나': 1000, '폴라포':1200, '빵빠레':1800 }
icecream.update(올때메로나 = 1200)


stock = {'메로나' : { '가격' : 300, '재고' : 20 },
         '비비빅' : { '가격' : 400, '재고' : 3 },
         '죠스바' : { '가격' : 250, '재고' : 100}
         }


print(stock)


print(stock.values())


for k, v in stock.items():
    print('{} - 가격 : {}, 재고 : {}'.format(k, v['가격'], v['재고']))


