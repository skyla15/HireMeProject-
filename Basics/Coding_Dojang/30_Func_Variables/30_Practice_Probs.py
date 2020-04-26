# 가장 높은 점수를 구하는 함수 만들기
korean, english, mathmatics, science = 100, 86, 81, 91

def get_max_score(*args) :
    print(args) # 튜플값으로 들어옴
    return max(args)

max_score = get_max_score(korean, english, mathmatics, science)
print('높은 점수 :', max_score)


# 가장 높은 점수, 가장 낮은 점수, 평균 점수 출력하기
korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args) :
    return min(args), max(args)

def get_average(**kwargs) :
    total = 0
    length = len(kwargs.keys())
    for v in kwargs.values() :
        total += v
    return total/length

min_score, max_score = get_min_max_score(korean, english, mathematics, science)

average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))