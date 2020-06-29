### 순위 매기기
exam = [
    {'num': 1, 'name': '김철수', 'kor': 90, 'eng': 80, 'math': 85, 'total': 255, 'avg': 85.0, 'order': 0},
    {'num': 1, 'name': '김철수', 'kor': 90, 'eng': 80, 'math': 85, 'total': 255, 'avg': 85.0, 'order': 0},
    {'num': 2, 'name': '박제동', 'kor': 90, 'eng': 85, 'math': 90, 'total': 265, 'avg': 88.3, 'order': 0},
    {'num': 3, 'name': '홍길동', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 80.0, 'order': 0},
    {'num': 4, 'name': '김씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 80.0, 'order': 0},
    {'num': 5, 'name': '똥씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 80.0, 'order': 0},
    {'num': 6, 'name': '말씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 80.0, 'order': 0},
    {'num': 7, 'name': '박씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 82.0, 'order': 0},
    {'num': 8, 'name': '홍씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 83.0, 'order': 0},
    {'num': 9, 'name': '정씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 84.0, 'order': 0},
    {'num': 9, 'name': '정씨', 'kor': 80, 'eng': 80, 'math': 80, 'total': 240, 'avg': 50.0, 'order': 0}
]

exam = sorted(exam, key = lambda x : x['avg'], reverse = True)
for i in range(len(exam)):
    exam[i]['order'] = i + 1
    if i > 0 :
        if exam[i-1]['avg'] == exam[i]['avg']:
            exam[i]['order'] = exam[i-1]['order']

for k in range(len(exam)):
    print(exam[k])



### 암호 풀기
dic = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.':'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z'
}

code = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
for word in code.split('  '):
    for c in word.split():
        print(dic.get(c), end='')
    print(' ',end='')
print()




### 해쉬태그
title = """
        On top of the world! 
        Life is so fantastic if you just let it. 
        I have never been happier. 
        #nyc #newyork #vacation #traveling
        """

for w in title.split():
    if w[0] == '#':
     print(w, end = ' ')

print([w for w in title.split() if w[0] == '#'])    # if w.startswith('#')]






















