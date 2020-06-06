# 반복문
# 1. while
n = 0
while n < 3 :
    print(n)
    n += 1

# 2. for
arr = [10,30,20,40,100]
for i in arr :
    print(i)

# 내장함수(built-in fuction)
number = list(range(10)) # range형(그냥 sequence) -> list형
print(number) # range: range(0, 10)/ list: 0~9 출력
number = list(range(1, 10, 2)) # 시작, 끝+1, 간격
print(number)

# 반복문에 넣기 - range는 반복가능한 객체
for i in range(10):
    print(i)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])

print(enumerate(arr)) # <enumerate object at 0x0000014E03C9C6D8>
for idx, item in enumerate(arr, 3) : # 3부터 출력
    print(idx, item) # tuple
    print(arr[idx])

# dictionary
mask =  {
    '삼성' : 100,
    '역삼' : 50
}

arr = ['삼성', '역삼']

# value값 출력
for i in mask:
    print(i)
# 동일한 결과 - 명확한 표현이므로 더 선호됨
for i in mask.keys() :
    print(i) 
    print(mask[i]) #value

for key, val in mask.items():
    print(key,val)

for i in mask.values():
    print(i)
