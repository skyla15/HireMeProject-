# 연,월,일 입력 / 연, 월, 일 따로 인풋 / 연 월 일 입력 시 => 요일을 구할 수 있다. / 윤달 윤년 파악
# 서기 1년 1월 1일은 월요일
# 4로 나누어지는 해는 윤년
# 100으로 나누어지는 해는 윤년이 아님
# 400으로 나누어지는 해는 윤년
cur_year= int(input('연도 : '))
last_year = cur_year - 1
month = int(input('월 : '))
day = int(input('일 : '))
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

leap_year_cnt = 0   # 윤년 카운트
no_leap_year_cnt = 0

year_cnt = 0        # 작년까지 총 일수
month_cnt = 0       # 이번 년도 달들에 대 일수 카운트
day_cnt = day       # 이번 년도 이번 달, 일수 카운트
total_days = 0      # 오늘까지 총 일수
ans = None          # days s인덱스

leap_year_cnt = last_year // 4 - last_year // 100 + last_year // 400
no_leap_year_cnt = last_year - leap_year_cnt
year_cnt = leap_year_cnt * 366 + no_leap_year_cnt * 365     # 작년까지 윤년 갯수 * 366 + 윤년 * 365

print(leap_year_cnt, year_cnt)

# 올해가 윤년인 경우
if cur_year % 4 == 0 and cur_year % 100 != 0 or cur_year % 400 == 0:
    # 1월부터 저번 달까지.
    for i in range(1, month):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            month_cnt += 31
        elif i == 2:
            month_cnt += 29
        else:
            month_cnt += 30
# 올해가 윤년이 아닌 경우
else:
    for i in range(1, month):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            month_cnt += 31
        elif i == 2:
            month_cnt += 28
        else:
            month_cnt += 30

# 총 일수 계산
total_days = year_cnt + month_cnt + day_cnt
ans = days[total_days % 7]
print(ans)

