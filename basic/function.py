def printme(str):
    print(str)
    return


printme("我要调用用户自定义函数")
printme("再次调用同一函数")

a = [1, 2, 3]
a = "Runoob"
print(a)

print("---------------------------------------------")


def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)

print("---------------------------------------------")


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值:", mylist)

print("-----------------------必备参数----------------------")


def printme(str):
    print(str)
    return


# 异常
# printme()

def printme(str):
    print(str)
    return


printme(str="您好,Python")

print("-----------------------多个参数----------------------")


def printinfo(name, age=35):
    print("name:", name)
    print("Age:", age)
    return


printinfo(age=50, name="张三")
printinfo(name="李四")

print("-----------------------不定长参数----------------------")


def printinfo(arg, *vartuple):
    print("输出: ")
    print(arg)
    for var in vartuple:
        print(var)
    return


printinfo(10)
print("----------------------------------------------------")
printinfo(60, 80, 90)

sum = lambda arg1, arg2: arg1 + arg2
print("相加后的值为:", sum(10, 20))
print("相加后的值为:", sum(20, 20))


def sum(arg1, arg2):
    total = arg1 + arg2
    print("函数内:", total)
    return total


total = sum(200, 34)
print("-------------------------全局变量与局部变量---------------------------")

totalResult = 0



def sum(arg1, arg2):
    totalResult = arg1 + arg2
    print("函数内局部变量为:", totalResult)
    return totalResult


sum(10, 20)
print("函数外全局变量为:", totalResult)
