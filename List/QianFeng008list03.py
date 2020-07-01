#list 中可以用的符号
'''
+
*
in
'''
#list中的元素:
'''
整形
字符串类型
浮点型
列表
元组
字典
对象
'''
l = [5,8]
print(l*3)

result = 3 in [1,2,3,4]  #返回值为Trues
print(result)


l2 = [1,2,3,'','ad',[1,2],[8,8,4,7]] #二维列表
result = [1,2] in l2 # 返回True
print(result)


l_len = [[1,2],[5,63,4],[],[7,1]]
print(len(l_len))   #返回 4--->4  [[],[],[],[]]

e = l_len[0]   # 返回l_len里的第0个元素
print(e)
print(type(e)) #返回List类型

print(l_len[3][1])  #返回列表l_len中第3个元素(列表)中的第1个元素(整形)


'''
类型转换
str()
int()
list()  强转列表类型 将指定内容转成列表类型 (除了整形)
iterable(可迭代) --->只要能在for ....in...里面做循环就是可迭代
'''
print(list(range(1,10,3))) # [1,4,7]

print(list('abc'))  # ['a','b','c']
# print(list(10)) # TypeError: 'int' object is not iterable(迭代)

print(list(range(10,1,-1))) #[10,...,2] 9个数
print(list(range(5))) #[0,1,2,3,4]
print(list(range(1,10)))

s1 = 'this is a test of Python'
#取test
position = s1.find('t')

print(s1[s1.find('t',s1.find('t')+1,len(s1)-6):14]) #麻烦死了
a = s1.find('test') # 返回的是10
b = s1.find('test')+4 #返回14
print(a)
print(b)
print(s1[a:b]) #[10:14] 4个字母 即test
# 利用正则表达式
import re
result=re.search('test',s1)
print(result.group())

