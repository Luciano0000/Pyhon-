# 产生10个随机数,将其保存到列表中

import random

# random_list = [] # 存放随机数

# for i in range(10):
#     ran = random.randint(1,50) #1-50个随机数
#     #保存到列表中,末尾添加apend
    
#     random_list.append(ran)
# print(random_list)



#   产生10个 不同 的随机数,将其保存到列表中,并求出最大值和最小值最后求和排序
random_list = []

i = 0
while i < 10:
    ran = random.randint(1,20)
    if ran not in random_list: #判断是否重复
        random_list.append(ran)
        i += 1
print(random_list)


# 系统函数  求最大值,最小值 求和 排序
print('系统提供的最大值:',max(random_list)) #系统的内置max()函数
print('系统提供的最小值:',min(random_list))
print('系统提供的求和:',sum(random_list))
#sorted()默认递增排列 ,reverse=True则递减
print('系统提供的排序:',sorted(random_list,reverse=True))


print('-'*20)

# 自定义 求最大值,最小值
mvalue = random_list[0] #假设列表中第一个元素就是最大值
minvalue = random_list[0] #假设列表中第一个元素就是最小值
# 拿第一个元素和其他的比较
for value in random_list: #从列表里抓取元素赋值给value
        #求最大值
    if value>mvalue: #  如果找到列表里有值比定义的mvalue大则
        mvalue=value # 把找到的值传给mavlue
        #求最小值
    if value<minvalue: # 并行if :两个if 都做判断
        minvalue = value

print('自定义的最大值是:',mvalue)
print('自定义的最小值是:',minvalue)

#自定义求和
sum_1 = 0
for value in random_list: #抓取列表所有的值
    sum_1 += value   #抓取的结果给sum_1
print('自定义的累加和是:',sum_1)

# 自定义 升序 降序(冒泡排序)
