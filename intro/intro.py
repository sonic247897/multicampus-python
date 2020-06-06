print("Hello, world!")

print('철수가 말했다. "안녕하세요"')

# 저장, 조건, 반복
# 1. 저장하는 방법 - List, Dictionary (set, tuple은 장고 시간에)
number = 13
string = '13'
boolean = False

print(number, string, boolean)
print(type(number), type(string), type(boolean))

# List
arr = [number, 13, '13', True, [string]] # 대괄호!
print(arr) # print: 리스트 안에 들어 있는 것들은 자료형을 정확하게 표현해준다.
print(arr[0], arr[1])
arr.append('값')  # 리스트 추가
print(arr)
arr.pop()
print(arr)

# dictionary
# key, value
mask = {
    '키값' : '밸류값',
    string : number

}
print(mask)
# 파이썬 딕셔너리 - 내가 입력한 순서대로 순서가 보장되지만 index로 접근은 불가능
#print(mask['없는 값']) # 값이 없으면 오류 - 값이 없으면 절대 안될 때 사용
print(mask.get('없는 값')) # 값이 없으면 None 출력(함수에서 None 리턴) - 프로그램 그대로 돌아야 할 때


