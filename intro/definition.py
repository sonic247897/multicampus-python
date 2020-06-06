import random

def hello() :
    return "Hello, world!"
string = hello()
print(string)

def add(num1, num2) :
    return num1+num2

num1 = 3
num2 = 4
number = add(3,4)
print(number)
number = add(num1, num2)
print(number)

def add_plus(num1, num2=10) :
    return num1 + num2
print(add_plus(3)) # 13
print(add_plus(3, 4)) # 7


