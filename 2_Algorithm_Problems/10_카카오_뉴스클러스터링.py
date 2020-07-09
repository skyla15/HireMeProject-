import re
import math
from collections import Counter

def solution(str1, str2):
    ### 다른 사람 풀이
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer

    ### 내 풀이 ㅅㅂ
    split_list1 = []
    split_list2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    regex = re.compile(r'[^a-z]')

    for i in range(0, len(str1) - 1):
        split_str1 = str1[i:i + 2]
        if not regex.findall(split_str1):
            split_list1.append(split_str1)

    for j in range(0, len(str2) - 1):
        split_str2 = str2[j:j + 2]
        if not regex.findall(split_str2):
            split_list2.append(split_str2)
    print( set(split_list1) | set(split_list2))
    union_counter = {}
    interaction_counter = {}

    for w1 in split_list1:
        union_counter[w1] = max(split_list1.count(w1), split_list2.count(w1))
        interaction_counter[w1] = min(split_list1.count(w1), split_list2.count(w1))

    for w2 in split_list2:
        union_counter[w2] = max(split_list1.count(w2), split_list2.count(w2))
        interaction_counter[w2] = min(split_list1.count(w2), split_list2.count(w2))

    union_sum = sum(union_counter.values())
    interaction_sum = sum(interaction_counter.values())

    J = interaction_sum / union_sum if union_sum != 0 else 1
    answer = math.floor((J * 65536))

    return answer

solution('FRANCE', 'french')