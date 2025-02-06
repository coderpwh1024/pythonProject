print("---------------------- if ------------------------")

flag = False
name = 'test'

if name == 'python':
    flag = True
    print("welcome boss")
else:
    print(name)

num = 5

if num == 3:
    print("boss")
elif num == 2:
    print("user")
elif num == 1:
    print("worker")
elif num < 0:
    print("error")
else:
    print("roadman")

num = 9

if num >= 0 and num <= 10:
    print('hello')
else:
    print('undefine')

num = 8

if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')

var = 100

if (var == 100):
    print('变量var的值为100')
    print('Good bye!')

print("---------------------- while语句 ------------------------")
a = 1
while a <= 10:
    print(a)
    a += 2

count = 0
while (count < 9):
    print("The count is:", count)
    count += 1
print("Good Bye!")

print("---------------------- while偶数------------------------")

i = 1
while i <= 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

print("---------------------- while循环------------------------")

i = 1
while 1:
    print(i)
    i += 1
    if i > 10:
        break

print("---------------------- while死循环-----------------------")

# var = 1
# while var == 1:
#     num = raw_input("Enter a number:")
#     print("You entered:", num)
# print("Good bye!")

print("----------------------for循环-----------------------")

for letter in 'Python':
    print('当前字母:', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print('当前水果:', fruit)
print('Good bye')

print("---------------------------------------------")

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d 等于 %d * %d' % (num, i, j))
            break
    else:
        print('%d 是一个质数' % num)

print("---------------------------------------------")
for letter in 'Python':
    if letter == 'h':
        break
    print('当前字母 :', letter)

var = 10

while var > 0:
    print('当前变量 :', var)
    var = var - 1
    if var == 5:
        break
print("Good bye")

