def getSplitGroup(s,i) :
    idx = 0
    split_group = []

    while len(s[idx:]) >= i :
        split_group.append(s[idx:idx+i])
        idx += i

    split_group.append(s[idx:len(s)])

    return split_group


def splitString(s,i) :
    split_group = getSplitGroup(s,i)    # 문자열을 i개씩 자른 문자열 리스트를 가져옴
    # print(split_group)
    result_group = []                   # 압축한 문자열을 저장할 리스트
    current_unit = ''                   # split_group에 있는 앞의 인덱스의 단위 문자와 비교하기 위한 현재 문자열
    last_unit = ''                      # result_group에 집어넣을 문자열
    count = 1                           # 중복 문자열 카운터
    # print('split group : ', split_group)
    for j in range(len(split_group)) :
        current_unit = split_group[j]                               # 현재 인덱스의 문자열을 비교 대상 문자열로 지정
                                                                    ## 비교 문자열들이 같을 경우 ## => 첫바퀴에는 들어가지 않음
        if current_unit == last_unit and j != len(split_group)-1:   # (1) 마지막 인덱스가 아닌 경우 카운터만 증가시켜줌
            count += 1
        elif current_unit == last_unit and j == len(split_group)-1: # (2) 마지막 인덱스인 경우, 리스트에 들어가지 않고, 루프빠져나감.
            count += 1                                              #     따라서, 마지막 인덱스인 경우, 결과 리스트에 카운트와 같 저장
            result_group.append(str(count))
            result_group.append(last_unit)

        elif current_unit != last_unit :                       ## 비교 문자열이 다른 경우 ## => 첫바퀴에 들어감
            if j != 0 and count != 1 :                         # (1) 첫번째 인덱스가 아니면서, 카운트가 1이 아닌 경우
                                                               #     카운트와 문자열을 저장
                result_group.append(str(count))
                result_group.append(last_unit)
            if j != 0 and count == 1 :                         # (2) 첫번째 인덱스가 아니면서, 카운트가 1인 경우,
                result_group.append(last_unit)                 #     문자열만 저장 (문제 조건 : 1인 경우 넣지 않음)
            count = 1                                          # (3) 카운트 초기화
            last_unit = current_unit                           # (4) 현재 문자열은 앞의 문자열과 중복되지 않으므로 비교 대상 문자열로 저장
                                                               # (5) last_unit이 마지막 인덱스인 경우, 결과 리스트에 저장
            if j == len(split_group)-1 :
                result_group.append(last_unit)

    return ''.join(result_group)


if __name__ == '__main__' :
    answer_string = ''
    size = []
    sizeDict = {}
    s = input().strip()
    i= 0
    for i in range(1, len(s)+1) :
        # 문자열을 1부터, 문자열의 길이까지 자르도록 함
        answer_string = splitString(s,i)
        size.append(len(answer_string))
        string_length = len(answer_string)
        sizeDict.setdefault(str(i).rjust(2) + ' ' + answer_string, string_length)


    if i == len(s) :
        for k, v in sizeDict.items() :
            print('{0:<25} : {1:<10}'.format(k, v))

    print("********* Min Value **********")
    for k, v in sizeDict.items():
        if v == min(sizeDict.values()):
            print('{0:<25} : {1:<10}'.format(k, v))
            break





