>>> a, b = [10, 20]
>>> a
10
>>> b
20

>>> x = input().split()
>>> 1 2
>>> print(x) #[1,2]
a, b = x

Operator	Description	Example

+	더하기	a + b = 30
-	빼기	a - b = -10
*	곱하기	a * b = 200
/	나누기	b / a = 2.0
%	나머지	b % a = 0
**	제곱	a ** c = 1000
//	몫	a // c = 3


연산

& 비트 AND a & b a와 b의 비트를 AND 연산

| 비트 OR a | b a와 b의 비트를 OR 연산

^ 비트 XOR a ^ b a와 b의 비트를 XOR 연산(배타적 OR, Exclusive OR)

~ 비트 NOT ~x x의 비트를 뒤집음

<<  비트 왼쪽 시프트 a << b a의 비트를 b번 왼쪽으로 이동시킴

>> 비트 오른쪽 시프트 a >> b a의 비트를 b번 오른쪽으로 이동시킴

&= 비트 AND 연산 후 할당 a &= b a와 b의 비트를 AND 연산한 후 결과를 a에 할당

|= 비트 OR 연산 후 할당 a |= b a와 b의 비트를 OR 연산한 후 결과를 a에 할당

^= 비트 XOR 연산 후 할당 a ^= b a와 b의 비트를 XOR 연산한 후 결과를 a에 할당

<<= 비트 왼쪽 시프트 후 할당 a <<= b a의 비트를 b번 왼쪽으로 이동시킨 후 결과를 a에 할당

>>= 비트 오른쪽 시프트 후 할당 a >>= b a의 비트를 b번 오른쪽으로 이동시킨 후 결과를 a에 할당