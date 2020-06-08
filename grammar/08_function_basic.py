# 함수 만들어 보자.
# @ 함수 -> 무조건 리턴값이 있어야 한다! (없으면 None 반환)
# def hello() :
#     print("Hello, World!")
# print(hello())

# @@ 하나의 객체만 반환된다
def hello():
    greeting = "Hello World!"
    return greeting
print(hello())

def sum(num1, num2):
    return num1+num2
my_num = 3
my_num_2 = 4
sum(my_num, my_num_2)