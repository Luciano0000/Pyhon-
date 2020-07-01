# time 模块
# 1.时间戳
import time

t = time.time()
print(t)  # 1587734060.261333

time.sleep(1)
t1 = time.time()
print(t1)

#将时间戳转成字符形式
s = time.ctime(t)
print(s)  # Fri Apr 24 21:14:20 2020

#将时间戳转成元组的方式
t=time.localtime(t)
print(t)
print(t.tm_hour)
print(t.tm_wday)
#将元组转成时间戳
tt=time.mktime(t)
print(tt)

#将元组的时间转成字符串
s=time.strftime('%Y-%m-%d %H : %M:%S')
print(s)

#将字字符串转成元组的方式
r=time.strptime('2019/06/20','%Y/%m/%d')
print(r)

'''
time模块 :
重点:
time()
sleep()
strftime('格式') -->去看源码
'''