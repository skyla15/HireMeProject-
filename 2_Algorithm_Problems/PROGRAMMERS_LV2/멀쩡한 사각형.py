import math

def solution(w,h):
    answer =  1

    # 최대공약수 찾기 위함
    G = 1   # 최대공약수 / 분할된 큰 사각형의 갯수
    nw = 0  # 분할된 작은 사각형의 밑변 크기
    nh = 0  # 분할된 작은 사각형의 세로 크기
    total = w * h # 총 박스의 갯수 

    # 유클리드 호제법을 이용하기 위해, h를 더 큰 값으로 둠 
    # -> 유클리드 호제법 안쓰고 math.gcd(w,h) 시 시간초과 발생
    if h > w :
        h, w = w, h
    G = math.gcd(w-h,h) # gcd(w,h) == gcd(w-h,h)

    # 분할된 직사각형의 가로 세로
    nw = int(h/G)
    nh = int(w/G)

    # 분할된 직사각형에서 각 x 축에서 1단위마다 박스수 계산 
    # x축 한칸마다 못사용하게 되는 사각형으 수 : 내립(y1) - 올림(y2)의 절대값 
    # i == nw 일 경우 나눠진 작은 박스 끝 
    sum = 0
    for i in range( nw ) :
        if i == nw :
            break
        else :
            sum += math.floor((nh * i)/nw) - math.ceil((nh * (i + 1))/nw)

    answer = total - ( abs(sum) * G )

    return answer
  
