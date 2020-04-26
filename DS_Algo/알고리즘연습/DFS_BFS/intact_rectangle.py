import math


def solution(w, h):
    answer = 1

    # 최대공약수 찾기 위함
    G = 1  # 최대공약수 / 분할된 큰 사각형의 갯수
    nw = 0  # 분할된 작은 사각형의 밑변 크기
    nh = 0  # 분할된 작은 사각형의 세로 크기
    total = w * h  # 총 박스의 갯수

    G = math.gcd(w-h, h)

    # 분할된 직사각형의 가로 세로
    nw = int(h / G)
    nh = int(w / G)

    # 분할된 직사각형에서 각 x 축에서 1단위마다 박스수 계산
    # 내립(y1) - 올림(y2)
    # i == nw 일 경우 끝
    sum = 0
    for i in range(nw):
        if i == nw:
            break
        else:
            sum += math.floor((nh * i) / nw) - math.ceil((nh * (i + 1)) / nw)

    answer = total - (abs(sum) * G)

    return answer

print(solution(8,12))