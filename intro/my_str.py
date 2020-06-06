import re

my_str = "Life is too short, you need phyton"
print(re.sub('a|e|i|o|u', '', my_str))

#for char in my_str:
#    print(char)

new_str = my_str.split(' ')
# 아무것도 안 넣었을 때도 공백 기준으로 split
#new_str = my_str.split(()
#print(new_str)

print(my_str.find('i')) # i인 index 반환(0부터 시작)
print(my_str.find('a')) # 문자열 안에 없으면 -1 반환
#print(my_str.index('a')) # 문자열 안에 없으면 오류 발생
print(new_str[0][0])

new_str = my_str.replace('Life', 'Time')
print(my_str)
print(new_str)

# 모음을 모아둔 리스트
vowels = ['a', 'e', 'i', 'o', 'u']

for char in vowels :
    if char in my_str:
        # .replace()는 원본은 바꾸지 않고 리턴값만 주기 때문에 원본에 그대로 넣어주면 된다.
        my_str = my_str.replace(char, '')

result = ''
for char in my_str:
    if char not in vowels:
        result += char
print(result)

for char in my_str :
    if char in vowels :
        pass
    else :
        result += char
print(result)
