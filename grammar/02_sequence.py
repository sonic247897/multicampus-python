# 02_sequence.py
# 데이터가 순차적으로 나열이 되어있다.
# 주의할 점> 정렬되어 있다는 뜻은 아님
# list, tuple, range, string
# 1. list(배열. array와 동일)
list_a = [] # 보통 생성하는 방법
list_b = list() # 이것도 가능
list_a = ['삼성', 23, True]
# 1-1. idx로 접근하기
print(list_a[0])
print(list_a[-1]) # 맨 뒤의 원소 출력
print(list_a[-2]) # 뒤에서부터 2번 째 원소

# 2. tuple
tuple_a = ()
tuple_a = (1, 2)
tuple_b = tuple(list_a) #가능
#tuple_c = tuple() #불가능. tuple만으로 tuple 생성 불가능
print(tuple_a)
# 값을 하나만 넣고자 한다면
tuple_b = (1,) # 쉼표 꼭 넣어줘야 한다.
tuple_c = (1)
print(type(tuple_b)) # <class 'tuple'>
print(type(tuple_c)) # <class 'int'>

# => 내가 직접 사용할 일은 거의 없고 파이썬 내부적으로 튜플이 사용되고 있음

# 3. range
print(range(10)) # range(0, 10) - 시퀀스
print(type(range(10))) # <class 'range'>
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(3,10,2))) # [3, 5, 7, 9]

