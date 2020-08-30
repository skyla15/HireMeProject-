'''
    SIMPLE BUT NOT SIMPLE

'''
# 소수찾기
# 에라토스테네스의 체!
# n의 최대 약수 : sqrt(n) 이하
def solution(n):
    a = [False] * (n + 1)
    m = int(n**0.5)
    # sqrt(n)까지만 외부 반복
    for i in range(2, m+1):
        if a[i]: continue
        # 내부 반복 : n 까지 모든 수에 대해 True 값 -> 소수가 아님
        for j in range(i + i, n + 1, i):
            a[j] = True
    return len([x for x in range(2, n + 1) if a[x] == False])