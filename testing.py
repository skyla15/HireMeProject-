# 문제
# 1번 수포자 : 1,2,3,4,5 ... 답안지 제출
# 2번 수포자 : 2,1,2,3,2,4,2,5 ... 답안지 제출
# 3번 수포자 : 3,3,1,1,2,2,4,4,5,5, ... 답안지 제출
# 정답 answers[]가 주어졌을 때 가장 많이 맞춘사람은?


def solution():
    answers = [2,1,2,3,2,4,4,4,4,4,4,4,4]
    set_1 = [1, 2, 3, 4, 5]
    set_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    set_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    print(int((len(answers) / 5)))
    print(int((len(answers) % 5)))

    print(int((len(answers) / 8)))
    print(int((len(answers) % 8)))

    print(int((len(answers) / 10)))
    print(int((len(answers) % 10)))

    set_1a = set_1 * int(len(answers) / 5)
    set_1a.extend(set_1[0:(len(answers) % 5)])
    set_1 = set_1a

    set_2a = set_2 * int(len(answers) / 8)
    set_2a.extend(set_2[0:(len(answers) % 8 )])
    set_2 = set_2a

    set_3a = set_3 * int(len(answers) / 10)
    set_3a.extend(set_3[0:(len(answers) % 10)])
    set_3 = set_3a

    print(set_1)
    print(set_2)
    print(set_3)

    answer_sheet = {1: 0, 2: 0, 3: 0}
    for i in range(len(answers)-1):
        if set_1[i] == answers[i]:
            answer_sheet[1] += 1
        if set_2[i] == answers[i]:
            answer_sheet[2] += 1
        if set_3[i] == answers[i]:
            answer_sheet[3] += 1


    answer = []
    count = []
    for v in answer_sheet.values() :
        count.append(v)


    count.sort(reverse=True)
    print(count)


    for i in range(len(count)):
        for k, v in answer_sheet.items() :
            if v == count[i] :
                answer.append(k)

    print(answer_sheet)
    print(answer)

solution()

