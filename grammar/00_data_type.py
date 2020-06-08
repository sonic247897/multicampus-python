import sys
max_num = sys.maxsize
print(max_num) # 2^63-1 (64bit에서 부호비트 뺌)
super_max = max_num*max_num
print(super_max) # 오버플로 없이 잘 나옴
print(type(super_max)) # <class 'int'>


# 출력해보기
print('Hello, World!')

# 프로그래밍 언어의 기본 3가지
# 1. 변수 저장 - 무엇을 저장할 수 있을까?
number = 10
string = '10'
boolean = True

# 파이썬에는 값이 없음을 표현하는 None 타입이 존재
nothing = None
print(number, string, boolean) # 10 10 True
print(type(nothing)) # <class 'NoneType'>

# 1-1. 정수형
number = 10
float_num = 1.3
complex_num = (3+3j) # 복소수 타입
print(type(number), type(float_num), type(complex_num)) # <class 'int'> <class 'float'> <class 'complex'>
# 파이썬에서는 정수형에 길이 제한이 없어서 long 타입이 없다!

# 2. bool
print(type(True))
print(type(False)) # <class 'bool'>
# 0, 0.0, [], {}
print(False == 0) # True - 0이나 0.0, [], {}도 False로 사용할 수 있다.(조건문 편하게 사용)

# 3. 문자형
# '', ""
# convention: ''나 "" 둘 중 하나만 골라서 사용!
greeting = 'hi'
name = "kim"
print(greeting, name)

# 문자열 입력 받기
# input()
#age = input("나이를 입력해 주세요: ")
#print(age) # input()은 모두 문자열로 치환해서 입력받는다.
#print(type(age)) # <class 'str'>
#print(type(int(age))) # <class 'int'>: 숫자가 아니라 문자열이면 형변환 못한다.

# string interpolation(보간법: 데이터를 채워넣을 수 있는 한 지점을 만드는 것)
name = 'kim'
print('안녕하세요,', name)
print('{}, {}'.format(greeting, name)) # 3.5이하 버전
print(f'{greeting}, {name}') # 3.6 이상. f는 format

# 연산과 출력 형태 지정
pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름 = 2 원의 넓이는 {pi*2*2}') # 변수의 소수점 자리 지정 가능

