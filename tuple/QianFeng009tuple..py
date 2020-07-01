#元组(当成容器,且容器不能实现'增''删''改')
# 定义 : 变量=()   或者变量=tuple()
#特点  1.符号()   
#        2.元组中的内容不可修改
# 
# # tuple() 转换类型 

#查询:  也可以实现  index 和切片[:]

# 元组中的函数 :
#               1.index() 差元组元素下标
#               2.count() 差元组元素的的个数

#符号 :
# + * is not 
# is not in
# max() min() sum() len() 
# sorted() 排序 返回类型为""List"


t1 =()
print(type(t1))  #<class 'tuple'>

t2 = (1)
print(type(t2))  #<class 'int'>

t2_r = (1,)
print(type(t2_r)) #<class 'tuple'>

t3 = ('das','das')#<class 'tuple'>
print(type(t3))



import random
list1 = []
for i in range(10):
    ran = random.randint(1,20)
    list1.append(ran)
print(list1) #[10, 20, 14, 15, 15, 5, 4, 13, 3, 13]

# tuple()
t5 = tuple(list1)
print(t5)    #(10, 20, 14, 15, 15, 5, 4, 13, 3, 13)

#下标index 和切片[:]

print(t5[2:-3])

#最大值 最小值  求和
print(max(t5))
print(min(t5))
print(sum(t5))
#求长度
print(len(t5))

#               1. index()
#               2.count()
print(t5.count(4))  #t5元组中 4的数量
# print(t5.index(4))  #t5元组中 4的下标,若没有ValueError: tuple.index(x): x not in tuple


t4 = (4,5)+(1,2)
print(t4)

t8 = t4*2
print(t8)

print(t8 is t4)  #地址一样吗 ?  true false
print(t4 in t8) # t4 在 t8里吗?

print(sum(t4)) #4+5+1+2  返回值为整形
print(tuple(sorted(t4)))