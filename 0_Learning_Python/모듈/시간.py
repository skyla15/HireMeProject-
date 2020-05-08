import timeit
""" 코드의 실행시간 측정하기 timeit 모듈 
- 클래스 timeit.Timer 
    - class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>, globals=None)
        - 생성자 : stmt, stmt에 사용될 추가 문장, 타이머 함수를 받음.
        - stmt : ;를 이용해서 여러 인자 받을 수 있음 
    - 메소드 
        - timeit.Timer.timeit(number=1000000) 
          stmt를 number만큼 실행시키는 시간 측정 
    - Tip
        - collection 멤버들의 탐색 시간을 측정하고자 할 때는 'in' operator를 사용하면 됨 
        => Python's in operator lets you loop through all the members of a collection(such as a list or a tuple) 
           and check if there's a member in the list that's equal to the given item.
"""
t = timeit.Timer('random.randrange(%d) in x; print(random.randrange(%d) in x)'%(10000,10000), "from __main__ import x, random")
# timeit.Timer 클래스 객체 생성
# randrange(%d) ""in"" x 를 통해 x(리스트, 딕셔너리)의 모든 요소를 방문할 수 있도록 하여 시간측정
x = list(range(10000))               # 측정하고자 하는 요소1
xt = t.timeit(100)                   # 요소1 100번 실행 시간 측정
print('xt : ', xt)
x = {j: None for j in range(10000)}  # 측정하고자 하는 요소2
xt = t.timeit(100)                   # 요소2 100번 실행 시간 측정
print('xt : ', xt)


######################
## time moudule 사용 #
####################
""" """
""" time.time() 
        1970년 1월 1일 이후 경과한 초단위 시간( 초.마이크로초 )
"""
import time
print( time.time() )
# 1588760823.020421
# 1970년 1월 1일 이후 경과한 초단위 시간( 초.마이크로초 )

""" time.localtime()
        time 반환값을 현재 시간에 대한 정보로 반환 ( localtime(time.time() ) 
        반환값 : time.struct_time
        속성 : tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst
"""
lt = time.localtime((time.time()))
print( lt )
# time.struct_time(tm_year=2020, tm_mon=5, tm_mday=6, tm_hour=19, tm_min=10, tm_sec=27, tm_wday=2, tm_yday=127, tm_isdst=0)
print('tm_hour : ', lt.tm_hour, 'tm_mon : ', lt.tm_mon)


""" time.strftime(날짜 시간 포맷, struct_time 객체) 
        날짜 시간 포맷
            # 연도 
                - %y : 2자리 연도
                - %Y : 4자리 연도 
            # 요일
                - %a : Sun, Mon.. 
                - %A : Sunday, Monday..
                - %w : 요일을 숫자로 표시 ( 0 ~ 6 )
            # 일 
                - %d : 일 ( 01, 02, .. 31 )
            # 월  
                - %b : Jan, Feb..
                - %B : January, Febuary..
                - %m : 01, 02.. 12
            # 시
                - %H : 24시
                - %I : 12시 
            # 분, 초
                - %M : 분 
                - %S : 초
            # 종합세트 
                - %c : 날짜 요일 시간 출력 
                       Sat May 19 11:14:27 2018
                - %x : 날짜 출력 
                       05/19/18
                - %X : 시간 출력 
                       '11:44:22'
"""
print( time.strftime('오늘 날짜 : %Y-%m-%d', time.localtime()))
# 오늘 날짜 : Wed May  6 19:19:19 2020



######################
## datetime 모듈 사용 #
####################
import datetime
""" 날짜와 시간 차이 계산하기 
    - datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, 
                   minutes=0, hours=0, weeks=0)
    - datetime 객체간 날짜 계산 시 timedelta 객체 나옴  
            
        
"""
today = datetime.datetime.today()
print('timedelta : ', today - datetime.timedelta(days=20))
print('datetime - datetime : ', datetime.datetime(2020,4,3) - datetime.datetime(2018,4,1) )

""" datetime.datetime 객체 
        - datetime.datetime.today()
            현재 시간 반환 
        - 속성 
            - year, month, day, hour, minute, second, microsecond
"""
today = datetime.datetime.today()
print('today = datetime.datetime.today() : ', today)
# 2020-05-06 19:27:03.027109
print('today.year : ', today.year)
# 2020


""" 특정 날짜와 시간으로 객체 만들기 
    datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)
        - datetime.datetime(2020, 5, 6) 
"""
print('datetime.datetime(2020, 5, 6) : ', datetime.datetime(2020, 5, 6) )
# 2020-05-06 00:00:00


""" 문자열로 날짜/시간 객체 만들기 
    datetime.datetime.strptime('날짜문자열', '포맷') 
"""
d = datetime.datetime.strptime('2018-05-19', '%Y-%m-%d')
print('datetime.datetime.strptime(\'2018-05-19\', \'%Y-%m-%d\') : ', d)
# 2018-05-19 00:00:00

