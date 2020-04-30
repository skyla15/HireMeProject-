
# 27.1 파일 문자열 읽기, 쓰기
# 파일 열기 쓰기 닫기
file = open('hello.txt', 'w')
file.write('Hello, World!') # 파일에 문자열 저장
file.write('Hello, World!') # 파일에 문자열 저장
file.write('Hello, World!') # 파일에 문자열 저장
file.write('Hello, World!') # 파일에 문자열 저장
file.write('Hello, World!') # 파일에 문자열 저장
file.close()                # 파일 객체 닫기

# 파일에서 문자열 읽기
file = open('hello.txt', 'r')
s = file.read() # 파일에서 문자열 읽기
print(s)        # Hello, World!
file.close()

# 자동으로 파일 객체 닫기 : 파일 사용이 끝나면 자동으로 파일 닫힘
with open('hello.txt', 'r') as file :
    s = file.read()     # 파일에서 문자열 읽기
    print(s)            # Hello, World!



