from sklearn.preprocessing import LabelEncoder

items=['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']

# LabelEncoder를 객체로 생성한 후, fit()과 transform()으로 레이블 인코딩 수행
encoder = LabelEncoder()
encoder.fit(items) #문자열 데이터를 숫자로 변환
labels=encoder.transform(items)
print('인코딩 변환값:', labels)
# 인코딩 변환값: [0 1 4 5 3 3 2 2]

print('인코딩 클래스:', encoder.classes_)
# 인코딩 클래스: ['TV' '냉장고' '믹서' '선풍기' '전자레인지' '컴퓨터’]

print('디코딩 원본 값:', encoder.inverse_transform([0, 1, 4, 5, 3, 3, 2, 2]))
#디코딩 원본 값: ['전자레인지' '컴퓨터' '믹서' 'TV' '냉장고' '냉장고' '선풍기' '선풍기']
