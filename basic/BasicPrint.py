print("Hello python!")
print("Hello python!")
print("Hello python!")
print("操！")
print("------------------------------------------------")

# 整型
counter = 100
# 复数
miles = 1000.0
# 字符串
name = "张三"

print(counter)
print(miles)
print(name)

a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, "李四"
print(a, b, c)

var1 = 1
var2 = 2
print(var1, var2)

s = "a1a2....an"

print(s)

str = 'Hello World!'

print(str)

print(str[0])

print(str[1:5])

print(str[2:])

print(str * 2)

print(str + "Test")

print("---------------------- Python 列表 ------------------------")
list = ['abc', 'bcd', 2.23, 'def', 12]
tinyList = [123, 'xyz']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinyList * 2)
print(list + tinyList)

print("---------------------- Python 元祖 ------------------------")

tuple = ('test', 786, 2.23, 'john', 70.2)
tinyTuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tinyTuple + tuple)

print("---------------------- Python 元祖与列表对比 ------------------------")

tuple = ('test', 786, 2.23, 'john', 70.2)
list = ['test', 786, 2.23, 'john', 70.2]
# tuple[2]=1000
list[2] = 1000

print(tuple[2])
print(list[2])

print("---------------------- 字典 ------------------------")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': '张三', 'code': 2234, 'dept': 'FBI'}

print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
