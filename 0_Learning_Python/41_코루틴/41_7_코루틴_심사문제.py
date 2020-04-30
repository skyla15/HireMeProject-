def calc() :
    result = 0
    while True :
        expression = (yield result)
        if '+' in expression :
            n1, n2 = map(int, expression.split(' + '))
            result = n1+n2
        if '-' in expression :
            n1, n2 = map(int, expression.split(' - '))
            result = n1-n2
        if '*' in expression :
            n1, n2 = map(int, expression.split(' * '))
            result = n1*n2
        if '/' in expression :
            n1, n2 = map(int, expression.split(' / '))
            result = n1/n2


expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()

