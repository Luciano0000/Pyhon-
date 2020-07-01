# 匿名函数  切记不要用格式化快捷键
'''
作用:
    简化函数定义
格式:
    lambda 参数1,参数2...  : 返回结果
'''

s = lambda a,b: a+b
# 变量=lambda 参数1,参数2:return a+b

print(s) # 地址<function <lambda> at 0x007677C0>
result=s(1,2) # result接收返回值
print('result:',result)

s1 = lambda x,y: x*y
result1=s1(2,5)
print('result1:',result1)


#匿名函数作为参数
def func(x,y,func):
    print(x,y)
    print(func)#<function <lambda> at 0x03869580>
    s=func(x,y)
    print(s)
#调用
func(1,2,lambda a,b: a+b)