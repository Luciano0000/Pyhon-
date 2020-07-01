# datatime : time 模块升级
'''
datatime 模块:
    time  时间
    data  日期    (data数据)
    datatime 日期时间  now()
    timedelta 时间差  timedelta(day='',weeks=''....)

'''
import datetime
import time

print(datetime.time.hour)
print(time.localtime().tm_hour)

d = datetime.date(2020, 6, 20)
print(datetime.date.day)
print(time.time())
print(datetime.date.ctime(d))

# datatime  timedelta
print(datetime.date.today())  # 2020-04-24

#时间差
timedel = datetime.timedelta(days=3,hours=2)
print(timedel)

now = datetime.datetime.now()
print(now)
result = now + timedel
print(result)
