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
