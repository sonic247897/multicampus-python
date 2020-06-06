import random

pick = random.choice(range(10)) # 0~9 중 무작위 하나 고름
print(pick)
#print(dir(random))

numbers = random.sample(range(10),3) # 3개 숫자 무작위로 뽑기
print(numbers)

lotto = random.sample(range(1,46), 6)
print(sorted(lotto))


# 1. 5번 반복을 해야 한다.
for num in range(5):
    print(random.sample(range(1,46), 6))

print(lotto)
print(sorted(lotto)) # 출력할 때만 정렬되어서 출력
print(lotto) # 원본이 변하지 않음
print(lotto.sort()) # None 출력 - 원본이 변경되고 None 반환
print(lotto) # 원본이 변경됨

# range와 list 담을 수 있음
station = ['삼성', '역삼', '선릉', '강남']
mask = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30,
    '강남' : 10

}
pick = random.choice(station)
print(mask[pick])

# 1. 가게 이름이 키 값, 전화번호 밸류값인 딕셔너리 하나
tel = {
    '던킨도너츠' : '012-345-6789', 
    '소풍': '000-111-222', 
    '순남시래기' : '333-444-555', 
    '아지매국밥' : '666-777-888'
}
# 2. 그 딕셔너리에서 무작위 값을 뽑아서 (같은 키 값을 가진 리스트 하나)
store = ['던킨도너츠', '소풍', '순남시래기', '아지매국밥']
# 3. 점심 메뉴를 추천해주는 코드
pick = random.choice(store)
#print(tel.keys())
pick = random.choice(list(tel.keys())) # 딕셔너리를 바로 넣을 수는 없다.(class 'dict_keys') 
# => list로 형변환

# 출력: 가게이름, 전화번호
# fstring - format 지원 : {}안에 변수명 넣기 가능(String interpolation)
print(f'가게 이름은 {pick} 전화번호는 {tel[pick]}')

if pick == '순남시래기' :
    print('떡볶이 무한리필!!!')

