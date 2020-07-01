'''
set集合(无序不重复的元素)
作用:                        *****去重*******
声明:                        set()
集合                        {元素1,元素2,...}

增(随机性): add()           添加一个元素或一组元素()
            update()        可以添加多个元素

删:         remove()        元素如果存在则删除,若不在则(key error)
            pop()           随机删除(一般大概率删集合中的第一个元素)
            clear()         清空
            dicard()        类似remove(),除了在移除不存在的元素的时候(不报错)
in not in 

#注意:当list强转set时 会自动排序并去重
'''
s1 = set()          #创建空集合

s2 = {1,2}
print(type(s2))     #<class 'set'>

list1 = [1,3,4,51,1,50,4,1,3,2]
s3 = set(list1)
print(s3)  
 #s3 = {1, 2, 3, 4, 50, 51}

#增加:随机位置添加
t1 = ('林志玲','言承旭')
#add()
s3.add(t1)
print(s3)
#{1, 2, 3, 4, 50, 51, ('林志玲', '言承旭')}

#update()
s3.update(t1)
print(s3)
#{'言承旭', 1, 2, 3, 4, '林志玲', 50, 51, ('林志玲', '言承旭')}

#remove()
s3.remove('言承旭')
print(s3)
# s3.remove('道明寺')
# print(s3)#KeyError: '道明寺'


'''
1.产生10个1~20的随机数,去除里面的重复项
2.键盘输入一个元素.将此元素从不重复的集合中删除
'''


import random
#方式一
#思路:生成随机数放入列表,然后在转成不重复的集合
list1 = []

for i in range(10):
    ran = random.randint(1,500)
    list1.append(ran)

set1 = set(list1) #把list转成set且自(动排序,自动去重)
print(set1)

# num = int(input('删除一个数字:'))
# set1.discard(num)
# print('删除之后结果为:',set1)

#方式二:
#思路 生成的随机数直接用set中的add()函数逐一遍历增加
set1 = set()
for i in range(10):
    ran2 = random.randint(1,500)
    set1.add(ran2)
print(set1)

