# 입력값 : 재밌는 알고리즘 문제 풀이
# 결과값 : 풀이 문제 알고리즘 재밌는
# 문자열 이용
if __name__ == '__main__' :
    string1 = input().split() # 입력받은 문자열이 strings에 공백단위로 저장됨
    result = ' '.join(string1[::-1])
    print(result)


# 포인터 이용
def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1)-1
    while p1 < p2:
        string1[p1], string1[p2] = string1[p2], string1[p1]
        p1 += 1
        p2 -= 1
    print(string1)

def reversing_words_setence_logic(string1):
    # 먼저, 문장 전체를 반전한다.
    reverser(string1)
    # print(string1)
    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020":
            # 단어를 다시 반전한다(단어를 원위치로 돌려놓는다).
            reverser(string1, start, p-1)
            # print(string1)
            start = p+1
        p += 1
    # 마지막 단어를 반전한다(단어를 원위치로 돌려놓는다).
    reverser(string1, start, p-1)
    # print(string1)
    return ''.join(string1)


if __name__ == "__main__":
    str1 = "파이썬 알고리즘 정말 재미있다"
    str2 = reversing_words_setence_logic(list(str1))
    print(str2)


