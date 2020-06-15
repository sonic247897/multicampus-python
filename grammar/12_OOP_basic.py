class Person: # 클래스 객체 생성 (클래스 정의)
    name = '이름이란, 사람이 공통적으로 가지는 속성'
    age = '나이란, 태어나서 지금까지 살아온 세월'
    
    # 인스턴스 메소드 - 인스턴스만 접근 가능하다(Person.greeting()으로 사용 불가능)
    # self - 자기자신을 의미하는 convention
    def greeting(self):
        return f'{self.name}이 인사합니다. 안녕하세요!'
    
    def aging(self):
        return f'{self.name}은 {self.age}살 입니다.'

    #클래스 메소드(cls - class를 의미하는 convention)
    @classmethod
    def age_means(cls):
        return f'{cls.name}은 나라마다 다르다.'


# list_a = list() 와 같은 형태
p1 = Person()
p1.name ='김현정'
p1.age = 100
print(Person.name)
print(Person.age)
print(p1.name)
print(p1.age)
print(Person.age_means())
# 익명 인스턴스 생성해서 인스턴스 메소드로 접근
print(Person().greeting())
# 이름이란, 사람이 공통적으로 가지는 속성은 나라마다 다르다.
#
print(Person.age_means())
print(p1.age_means())