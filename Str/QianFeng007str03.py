# isalpha() 字符串中 至少 有 一个 字符串且 所有的字符串 是 字母 则True否则False
# 重点:isdigit() 字符串只包含 数字 则返回True 否则返回False
# isnumeric() 字符串只包含 字符 则true 否则false
# isspace() 字符串只包含 空白  则true 否则false
# 重点:join(seq) 以指定的字符串作为分隔符,将 seq(队列)中所有的元素(的字符串表示)合并
#为一个新的字符串   如果join列表 最后返回字符串
# strip()左右两边空格都去除  lstrip()  去除字符串中左侧空格 rstrip()去除字符串右侧空格 
# splite('',切割次数) 分割字符串,将分割后的字符串   返回在列表 
# count('') 求字符串中''里面的内容的个数


#isalpha()用法
s = 'abcd6'
print(s.isalpha())  # 6--> False 

s = '1616'
print(s.isdigit())  #-->True

#join()用法
new_str = '-'.join('abc')
print(new_str)   # a-b-c
print('-'*10)
list1 = ['a','b','c','d']
result = '%'.join(list1)  #列表类型变为字符串类型
print(result)
print(type(result))

#strip()用法
c = '   hello  '
c = c.lstrip()
print(c+'8')
c = c.rstrip()
print(c+'6')


#splite()用法  返回列表类型
s = 'hello#world#hello#kitty'

rsult = s.split('#',2)  
print(rsult)  #--->['hello','world','hello#kitty']

#count()用法    python自带函数,别的语言需要做循环判断
result = s.count('#') #检索#的个数
print(result)
'''
需求:
    求三次的累加和 
    要求用户输入三次数字,若不是数字则重新输入,且不影响上一次的输入内存
    最后求出累加和 
'''
sum = 0
i = 1
while i<=3:
    num = input('请输入数字')
    
    if num.isdigit():  #判断用户输入的是否为数字字符串true 则进入
        num = int(num)  #转成Int类型,提供下列代码的数字运算
        sum += num   # sum = sum + num ,重复三次
        print('第{}数字数字累加和成功'.format(i)) #优化用户体验
        i += 1      #累加1次
    else:
        print('不是数字')
print('sum=',sum)
#总结 :先声明 sum i num 三个变量 sum用来做存储用户输入内容的容器  i作为循环变量  num作为用户输入的字符串变量(最后强转Int类型)

#for 循环无法控制用户输入的次数,所以不用For
# sum = 0
# for i in range(3):
#     num = input('请输入数字')  #用户错了 比如 字母l 0 
    
#     if num.isdigit():  #判断用户输入的是否为数字字符串true 则进入
#         num = int(num)
#         sum += num
#     else:
# print('sum=',sum)

