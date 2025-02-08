import time
import calendar

ticsk = time.time()
print("当前时间为:", ticsk)

localtime = time.localtime(time.time())
print("本地时间为:", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为:", localtime)

print("当前时间为:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("当前时间为:", time.strftime("%Y-%m-%d %H:%M:%S %Y", time.localtime()))

a = "Sat Mar 28 22:24:24 2016"
print("转换结果为:", time.strptime(a, "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2016, 1)
print("输出2016年1月份的日历:")
print(cal)

print("---------------------------------------------------")

