def solution(p, l):
    answer = 0
    m = max(p)
    while True:
        v = p.pop(0)
        # 인쇄 대기목록의 가장 앞에 있는 문서를 대기목록에서 꺼낸다
        if v == m:
            answer += 1
            if l == 0:
                break
            else:
                l = (len(p) + l - 1) % (len(p))
            m = max(p)
        else:
            p.append(v)
            l = (len(p) + l - 1) % (len(p))



    return answer



print(solution([2,1,3,2], 2))
print(solution([1,1,1,1,1], 0))
print(solution([1,1,2,2,3,3], 5))
print(solution([1,1,2,2,3,3,9,9,9,9,9,9,9,9], 0))
print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 0 ))
'''
1 2 2 3 3 1
2 2 3 3 1 1
2 3 3 1 1 2
3 3 1 1 2 2 -> 1, 3
3 1 1 2 2 -> 2, 3 : cur
'''