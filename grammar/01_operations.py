# 01_operations.py
# 논리 연산자
# and, or, not
print("___and___")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("___or___")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("___not___")
print(not True)
print(not False)
print(not []) # True
print(not 0) # True

# in, not in (그 안에 들어 있는지, 아닌지 확인)
print("___in___")
print('a' in 'apple')
print(1 not in [1,2,3])

# 단축 평가
print('' or 'Text' or 'Text_2') # 빈 문자열('')도 False, 나머지는 True
# Text 출력. 파이썬에서 or는 하나만 True가 되어도 뒤에 계산X
print('Text' and '' or 'Text_2') # False와 Text_2 비교해서 Text_2가 True이므로 Text_2 출력




