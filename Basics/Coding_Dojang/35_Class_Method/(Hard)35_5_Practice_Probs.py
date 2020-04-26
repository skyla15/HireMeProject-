class Date:
    @staticmethod
    def is_date_valid(str) :
        year, month, day = map(int, str.split('-'))
        if year <= 12 and day <= 31 :
            pass
        elif year <= 0 and day <= 0 :
            return False
        else :
            return True


if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')



# 심사문제 :
# 표준 입력으로 시:분:초 형식의 시간이 입력됩니다.
# Time클래스를 완성하여 시, 분, 초가 출력되게 만드세요.
# from_string은 문자열로 인스턴스를 만드는 메소드이며
# is_time_valid는 문자열이 올바른 시간인지 검사하는 메소드.
# 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다.

class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <=59 and second <= 60
    # 클래스에 접근할 필요없이 True, False만 확인하면 되므로,
    # 정적 매소드로 선언

    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        # time = Time(hour, minute, second)
        # Time객체 만들고 반환
        return time

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    # 클래스 내의 메소드에 객체 선언없이 접근하여,
    # Time 객체를 받아 출력
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')