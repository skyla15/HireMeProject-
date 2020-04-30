# 피클링 & 언피클링
# https://dojang.io/mod/page/view.php?id=2327
# 피클링 : 파이썬 객체를 파일에 저장하는 과정
# 객체 -> 파일 : 피클링
# 파일 -> 객체 : 언피클링
# 언피클링 : 파일에서 객체를 읽어오는 과정


############################################
# 27.3.1 피클링 : 파이썬 객체를 파일에 저장하기    ##
# 피클링 : pickle 모듈의 dump 메서드           ##
###########################################

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean' : 10, 'english' : 20}

with open('james.p', 'wb') as file :    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


with open('james.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)