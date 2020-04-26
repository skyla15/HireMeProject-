################################
# 딕셔너리 만들기 (1)
# 1) dic = { '키' : 쌍 .. }
# 2) dic = dict(zip(['키'..], [값..]))
# 3) dic = dict(키=값...)
# 4) dic = dict( [ (키,값)... ] )
# 5) dic = dict( 딕셔너리 )
################################
dict_1 = {'a' : 1, 'b' : 2, 'c' :3}
# zip([] [])
dict_2 = dict(zip(['a','b', 'c'], [1, 2, 3]))

# dict(key = value)
# key 따옴표 사용 x
dict_3 = dict(a=1, b=2, c=3)

# dict([튜플])
# 딕셔너리 캐스팅
dict_4 = dict([('a',1), ('b',2), ('c',3)])

# dict(dictionary)
dict_5 = dict({'a' : 20, 'b' : 20, 'c' :30})

print(dict_1, dict_2, dict_3, dict_4, dict_5, sep='\n')
print()
print()

################################
# 딕셔너리 만들기 (2)
# dict.fromkeys(리스트/튜플)
# 키.. : None v
################################
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)

#############################
# 25.3 딕셔너리표현식 사용하기
# 응용
# -> 키-값 자리 바꾸기
# -> 키/값만 가져온 뒤 특정값과 쌍 만들기 등
# ★ 특정 키-쌍을 지우는 메소드 : pop, del ★
# --> for 문으로 키-쌍 삭제 불가능!!!!
# -> if 문을 사용하여, 특정 값을 갖는 키를 삭제!!!!
#############################
print('1) 표현식으로 딕셔너리 만들기')
keys = ['a', 'b', 'c', 'd']
new_dic = { k : v for k, v in dict.fromkeys(keys).items() }
print(new_dic)
print()

print('2) 표현식으로 딕셔너리 특정값 삭제하기')
print('original dictionary : ' + str(dict_5))
dict_5 = { k : v for k, v in dict_5.items() if v != 20}
print('updated dictionary : ' + str(dict_5))
print()
print()



################################
# 딕셔너리 수정하기 (1)
# (1) update(키=값)
#     => 키에 따옴표 사용 x
# (2) update(리스트)
#     => 리스트 = [ [키, 값]]..]
# (3) update(zip([키..],[값..])
################################
dict_1 = {'a' : 1, 'b' : 2, 'c' :3}
print('1) 딕셔너리 수정하기 : update(키=값) ')
print('dict_1 : ', dict_1)
dict_1.update(a=10)
print('dict_1 : ', dict_1)
print()

print('2) 딕셔너리 수정하기 : update( [ [\'키\', 값], .. ] ) ')
dict_1.update([ ['a',100] ])
print('dict_1 : ', dict_1)
print()

print('3) 딕셔너리 수정하기 : update(zip([키 리스트],[값 리스트])')
dict_1.update(zip(['a'],[1000]))
print('dict_1 : ', dict_1)
print()
print()


################################
# 딕셔너리 쌍 삭제하기
# (1) pop('키'), pop('키', 기본값)
#     => 키 삭제후 값 반환, 키 없을 때 기본값 없는 경우 0, 설정 시 기본값 반환  #
#     => 키 없을 시, 기본값 설정 안하면 에러 발생
# (2) del dictionary['키']
#     => 반환값 없음
# (3) .popitem()
#     => 임의 쌍  삭제
# (4) .clear()
#     => 모든 쌍 삭제
# (5) 딕셔너리는 for 문을 사용하면 안되며,
#     "딕셔너리 표현식에서 if 조건문ㅇ 사용하여 삭제하여야 함"
##############################

# pop
dict_1 = {'a' : 1, 'b' : 2, 'c' :3}
print('1) 딕셔너리 삭제하기 : pop(\'키\',값)')
print('dict_1 : ', dict_1)
print(dict_1.pop('a', 1000))
print('dict_1 : ', dict_1)
print()

# del dictionary['키']
print('2) 딕셔너리 삭제하기 : del 딕셔너리[\'키\']')
del dict_1['b']
print('dict_1 : ', dict_1)
print()
print()


################################
# 딕셔너리 키의 값 / 모든 쌍 가져오기
# 1) .get('키') .get('키', 기본값)
#    => 기본값 성정 안하면, 키 없을 시 None 반환
# 2) .items()
# 3) .keys()
# 4) .values()
################################
print('1) 딕셔너리 키의 값 가져오기 : get(\'키\') / .items() / .keys() / .values()')
print(dict_1.get('z',0))
print()
print()


################################
# 25.4 중첩 딕셔너리
# 딕셔너리1 = { 딕셔너리2 }
# 값 호출 : 딕셔너리1['키1']['2']
################################

print('1) 중첩 딕셔너리 사용 ')
solar_system = {
    'Mercury' :
        {
            'mean_radius' : 2439.7,
            'mass' : 3.3022E+23,
            'orbital_period' : 87.969
        }
}
print(solar_system['Mercury'])
print(solar_system['Mercury']['mean_radius'])
print()
print()



################################
# 25.5 딕셔너리 할당 및 복사 ( 옅은 복사 / 깊은 복사 ) 
# '=(등호)' 사용 시, 같은 객체를 가르킴 : 따라서 한 쪽이 변경 시 다른 것 변경
# --> x = y
# --> x is y ; True 같은 객체
# --> x == y ; True 같은 값

# .copy() 메소드 사용 시, 서로 다른 객체로 복사
# x = y.copy()
# --> x is y ; False 다른 객체
# --> x == y ; True  같은 값

# 25.5.1 중첩 딕셔너리 복사
# import copy
# y = copy.deepcopy(x) 메소드 사용
################################


################################
# 25.7 연습문제
# 풀이
maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)
print()
print()

a,b,c = 1,2,3

# 25.7 연습문제2
# 입력값
# alpha bravo charlie delta
# 10 20 30 40
#
# alpha bravo charlie delta echo foxtrot golf
# 30 40 50 60 70 80 90
keys = input().split()
values = map(int, input().split())
x = dict(zip(keys, values))
x = { k : v for k, v in x.items() if ( k != 'delta' and v != 30 ) }
print(x)













