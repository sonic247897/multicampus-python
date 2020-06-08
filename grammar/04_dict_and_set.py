# 04_dict_and_set
# 1. dictionary
# 사전 - 단어: 설명 (JSON, map)
# key, value로 이루어져 있음
dict_a = {}
dict_b = dict()
# key가 중복이 불가능하다.[고유값]
dict_a = {'삼성':100, '역삼':50, '삼성':30}
print(dict_a) # {'삼성': 30, '역삼': 50} 뒤에 넣어준 값이 앞에 있는 값을 덮어쓴다.

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items()) # key, value 동시에 가져옴
# dict_items([('삼성', 30), ('역삼', 50)]) : ('삼성', 30) => tuple이 내부적으로 사용된다.

print(dict_a['삼성'])
print(dict_a.get('삼성'))

# .get과 [] 접근 차이점
dict_a = {'삼성':100, '역삼':50}
#print(dict_a['선릉']) # 오류 발생 - 그 키 값이 없으면 멈춰야 하는 경우 사용
print(dict_a.get('선릉')) # None: 값이 없음 - 없었을 때도 코드가 계속적으로 진행되어야 할 때 사용

# 2. set
# set는 순서가 없이 저장된다. 
# (dictionary는 순서는 보장되는데 set은 그것조차 없어서 index로 접근 불가능)
set_a = {1,1,1} # {}는 dictionary가 이미 선점해서 {}로는 빈 set(공집합)로 못 만듬
dict_b = {}
set_b = set() # 따라서 공집합 이렇게 만들어야 한다.
print(set_a) # {1}

# 수학의 집합과 같으므로 연산도 같게 동작
set_a = {1,2,3}
set_b = {3,6,8}
print(set_a - set_b) # 차집합 - {1, 2}
print(set_a | set_b) # 합집합 - {1, 2, 3, 6, 8}
print(set_a & set_b) # 교집합 - {3}

# 간단하게 list의 중복 전부 제거하기 - set 형변환
list_a  = [1,1,1,1]
print(list(set(list_a)))

string = "immutable" # sequence이므로 index접근 가능
list_a = ['immutable?', 'real?']

print(string[0]) # i
print(list_a[0]) # immutable?
#string[0] = 'a' # 컴파일 에러
list_a[0] = 'mutable' # 값 변경
print(list_a) # ['mutable', 'real?']
list_a = ['mutable'] # 값을 변경한 것이 아니라 재할당

list_a = ['immutable?', 'real?']
list_b = list_a 
print(list_a, list_b) # 동일
list_b[0] = 'mutable'
print(id(list_a), id(list_b)) # 동일한 객체를 가리키고 있으므로 두 리스트 모두 값이 변한다.

string_a = 'immutable'
string_b = string_a
print(id(string_a), id(string_b)) # 2098449531952 2098449531952
string_b += 'e' # => string_b가 재할당됨
print(string_a, string_b) # immutable immutablee
print(id(string_a), id(string_b)) # 2098449531952 2098449540272



