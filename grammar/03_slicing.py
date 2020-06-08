sample_list = list(range(31)) # 0~30
print(sample_list)
print(sample_list[3])
print(sample_list[3:24]) # a:b => a에서 b 전까지
print(sample_list[5:]) # -1을 사용할 때 -1 전까지라 마지막에서 두 번째까지 출력하는
# 문제 발생하므로 -1 대신 숫자를 안 쓰는 방법 사용
print(sample_list[3:len(sample_list): 2])

# 생략하기 응용
print(sample_list[3 : : 2])
print(sample_list[ :13:2]) # 0부터 12까지 2단계 씩 출력
print(sample_list[::-1]) # 뒤에서부터 반대로 출력