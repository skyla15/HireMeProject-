import os
from collections import Counter

# path 디렉토리 파일들 읽기
path = './nk/'
file_names = os.listdir(path)       # 디렉토리 내용 가저옴

# os.rename 이용 파일 이름 변경
# rename 사용 시 path 쓸 것
for filename in file_names:
    if filename[-3:] == 'pdf':
        os.rename(path + filename, path + filename.replace('pdf', 'txt'))

# 변경된 이름의 파일 읽기
new_file_names = os.listdir(path)    # 디렉토리 내용 가져옴
word_collection = list()             # 단어들 저장해줄 리스트

for filename in new_file_names:
     f_name = path + filename
     if f_name[-3:] == 'txt':
         f = open(f_name, 'r')
         data = f.read()              # string으로 각 파일의 내용을 string으로 저장
         word_collection.extend(data.split())
         f.close()

for w in word_collection:
    if not w.isalnum():
        word_collection.remove(w)

# print(word_collection)
c = Countter(word_collection)
print(c)



#  rename - 인코딩 문제 발생
'''
    Traceback (most recent call last):
    File "/Users/jaeyeopchung/HireMeProject-/forTest.py", line 29, in <module>
    with open('./nk/20191229_북한방송_주요내용.txt', 'r', encoding='utf-8') as f:
    FileNotFoundError: [Errno 2] No such file or directory: './nk/20191229_북한방송_주요내용.txt'
'''
