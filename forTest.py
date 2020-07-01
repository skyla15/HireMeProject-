import sys
print(sys.path)
sys.path.append('모듈 디렉토리')

prices = [7, 1, 5, 3, 4, 6]
print(prices)
print(prices[1:])
print(list(zip(prices, prices[1:])))
print([b - a for a, b in zip(prices, prices[1:]) if b - a > 0])
print(sum([b - a for a, b in zip(prices, prices[1:]) if b - a > 0]))