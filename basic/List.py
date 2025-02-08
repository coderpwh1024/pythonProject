list1 = ['pysics', 'chemistry', 1977, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print('list1[0]:', list1[0])
print('list2[1:5]:', list2[1:5])

list = []
list.append('Google')
list.append('Runoob')
print("list:", list)

list1 = ['physics', 'chemistry', 1977, 2000]

print(list1)
del list1[2]
print("After deleting value at index 2:")
print(list1)

print("---------------------元祖------------------------")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34, 56)
tup2 = ('abc', 'xyz')

tup3 = tup1 + tup2
print("tup3: ", tup3)

print("---------------------元祖删除------------------------")

tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup

print("After deleting tup:")
# 报错异常
# print(tup)

print("---------------------字典------------------------")
tinydict = {'a': 1, 'b': 2, 'b': '3'}
print('tinydict[b]:', tinydict['b'])

tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("tinydict['Name']:", tinydict['Name'])
print("tinydict[Age]:", tinydict['Age'])

print("---------------------------------------------")
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# key值不存在
# print("tinydict['Alice']: ", tinydict['Alice'])

tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8
tinydict['School'] = 'RUNOOB'

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

print("----------------------删除元素-----------------------")
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del tinydict['Name']
tinydict.clear()
del tinydict

# key 删除,tinydict 删除报错
# print("tinydict['Age']:", tinydict['Age'])
# print("tinydict['School']:", tinydict['School'])

print("----------------------字典特性-----------------------")
tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': 'Manni'}
print("tinydict['Name']:", tinydict['Name'])

tinydict = {['Name']: 'Zara', 'Age': 7}
print("tinydict['Name']:", tinydict['Name'])


