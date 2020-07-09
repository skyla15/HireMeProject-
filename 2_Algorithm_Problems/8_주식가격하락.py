def solution(prices):
    answer = []
    for i in range(len(prices)):
        drop = False
        for j in range(i + 1, len(prices)):
            if prices[j] < prices[i]:
                drop = True
                answer.append(j - i)
                break
        if not drop:
            answer.append(len(prices)-1 - i)

    print(answer)
    return answer

solution([1,2,3,2,3,2])

