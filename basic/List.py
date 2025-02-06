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
print(tup)

>>> tinydict = {'a': 1, 'b': 2, 'b': '3'}
