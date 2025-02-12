import math

from sympy import content

Money = 2000


def AddMoney():
    global Money
    Money = Money + 1


print("Money=", Money)
AddMoney()
print("Money=", Money)

print("----------------------------------------------------")

content = dir(math)
print(content)

print("----------------------------------------------------")


def runoob1():
    print("Hello World!")


def runoob2():
    print("I am runoob")


runoob1()
runoob2()
