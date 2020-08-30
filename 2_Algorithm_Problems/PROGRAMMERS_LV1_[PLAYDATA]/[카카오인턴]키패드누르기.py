# 심심해서 풀어보는 문제 - [카카오 인턴] 키패드 누르기 / O(n) 풀이, 30분
# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    keyboard = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        '*': (3, 0),
        0: (3, 1),
        '#': (3, 2)}

    # distance = |low index1 - low index2| + |col index1 - col index2|
    r_stack, l_stack = list(), list()
    l_stack.append('*')
    r_stack.append('#')
    for n in numbers:
        left_distance = 0
        right_distance = 0
        if n in [1, 4, 7]:
            answer += 'L'
            l_stack.append(n)
        elif n in [3, 6, 9]:
            answer += 'R'
            r_stack.append(n)
        elif n in [2, 5, 8, 0]:
            l = l_stack[-1]
            r = r_stack[-1]

            for i in range(2):
                left_distance += abs(keyboard[l][i] - keyboard[n][i])
                right_distance += abs(keyboard[r][i] - keyboard[n][i])

            if left_distance > right_distance:
                answer += 'R'
                r_stack.append(n)
            elif left_distance < right_distance:
                answer += 'L'
                l_stack.append(n)
            elif left_distance == right_distance:
                if hand == 'right':
                    answer += 'R'
                    r_stack.append(n)
                elif hand == 'left':
                    answer += 'L'
                    l_stack.append(n)
    return answer