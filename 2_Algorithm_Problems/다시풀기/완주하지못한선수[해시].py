'''
    SIMPLE BUT NOT SIMPLE
'''
# 완주하지 못한 선수
# time complextiy with 'in' operator is O(N),
# if used, the worst time complexity would be O(n^2) which is not the goal of this problem.
# Here, you have to use the data structure 'hash' which is already implented in Python as dictionary.
# With dictionary, you can reach each element with time complexity of O(n).

def solution(participant, completion):
    hash = {}
    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1

    for c in completion:
        if c in hash:
            hash[c] -= 1
            if hash[c] == 0:
                del hash[c]
    return list(hash.keys())[0]