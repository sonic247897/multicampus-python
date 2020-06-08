# 특정 범위 혹은, 시퀀스 같은
# 반복가능한 객체의 요소들을 순차적으로
for num in [1,2,3,4,5] : 
    print(num)
print("끝")

for num in range(10): # 0~9
    print(num)

# 조건과 같이 사용
for num in range(1,31):
    # 연산자 중에 나머지만 구해주는 %
    # 0 == False 이므로 나머지가 0이 나오면(짝수이면) 동작X
    # 0이 아닌 나머지 == True
    if num % 2 : 
        print(num)
print("끝")

# for_dictionary
dict_a = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30
}


# key값만 출력!
for data in dict_a :
    print(data) # 삼성 역삼 선릉
# => 근데 이렇게 쓰면 list를 쓰는지 dictionary를 쓰는지 구별이 안 가므로 keys() 사용
list_a = ['삼성', '역삼', '선릉']
for data in dict_a.keys():
    print(data)
for data in dict_a.values():
    print(data)
for data in dict_a.items():
    print(data)  # tuple형태로 출력 => 사용하기 힘드므로 key, val로 나눠서 받을 수 있다.
for key, val in dict_a.items():
    print(key, val) 

# 추가
num1, num2 = 3, 4
print(num1, num2)