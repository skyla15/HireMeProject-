# 다음 소스 코드에서 동물 클래스 Animal과 날개 클래스 Wing을 상속받아
# 새 클래스 Bird를 작성하여 '먹다', '파닥거리다', '날다', True, True가 각 줄에 출력되게 만드세요.

class Animal:
    def eat(self):
        print('먹다')

class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing) :
    def fly(self):
        print('날다')


b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))