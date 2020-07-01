#数组:数字字母字符串..的组合
#符号:[ ] 或者 变量=list()

names = ['cmptioan','spaderman','airman'] 


#地址 
print(id(names))

#元素获取:脚标(下表,索引,index)
print(names[0],'love ',end='') #正向0开始
print(names[-3])               #逆向从-1开始
print()

print(names[len(names)-1])  #names[数组长度-1]

#结合循环遍历数组
for name in names:
    print(name)

# 查询names里面有没有保存钢铁侠
for name in names:
    if name == 'airman':
        print('找到钢铁侠')
        break
# 简便方式:
if 'airman' in names:  
    #-->True False
    print('有钢铁侠')
else:
    pass


brands = ['hp','dell','thinkpad','支持华为','lenvovo','mac','神州']

#改神州
# brands[-1] = 'FUCK'  #fuck 赋值给旧数组元素
# print(brands)

# 当数组元素特别多,改华为
for i in range(len(brands)): #i是0,1...脚标
    if '华为' in brands[i]:
        brands[i] = 'huawei'
        break
print(brands)

#删除  del         --不能用for来遍历
del brands[2]
print(brands)

#删除 hp 和 mac
l = len(brands)
i = 0
while i<l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]  
        l -= 1    #由于删除一个元组列表长度就会-1,所以需要人工l=l-1,否则会报错

    i+=1 
print(brands)


# 练习:生成一个数组,用户输入一个字符串,如果在数组中则删除
list1 = ['hello','goods','good','world','digot','alphago',]
user = input('输入要删除的一个单词') #go
i = 0
l = len(list1)
while i<l:
    if user in list1[i]:
        print('删除成功')
        del list1[i]
        l -= 1
        i -= 1 #防止错位漏删
    i += 1
print(list1)
#第二种方法
list1 = ['hello','goods','good','world','digot','alphago',]
user = input('输入要删除的一个单词') #go
i = 0
l = len(list1)
while i<l:
    if user in list1[i]:   
        del list1[i]
        l -= 1
        continue # 
    i += 1
    print('{}'.format(l))
print(list1)