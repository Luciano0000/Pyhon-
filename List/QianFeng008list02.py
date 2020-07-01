# 列表的切片
#['abc','kkokok','dasd','geeww',99,80.8]
list1 = ['abc','kkokok','杨幂','胡一菲',666,68.8]  
#列表里允许任意类型
print(list1)
print(list1[2:4])  #杨幂 胡一菲 脚标:2 3 同样包前不包后  [2:4]
#截取的结果再次保存在一个列表中 ['','']

print(list1[::2])  #支持步长
print(list1[-1::-2]) #支持逆序

# list 列表的添加:
# 临时的小数据库: list 
# list的添加函数 :1.append()追加 2.extend()列表的合并 3.insert()指定位置插入元素
# list的删除函数 : 1.remove()  2.pop()  3.clear() 4.del()
names = ['黑嘉嘉','孙俪','功利','王丽坤']
girls = ['杨幂']
while True:
    name = input('请输入你心目中的美女')
    if name == 'quit':
        break
    girls.append(name)
print(girls)


#extend():合并 或 一次添加多个元素

girls.extend(names)  #合并两个列表
print(girls)

# 符号 +
girls = girls+names  # + 也用于列表的合并 等价于extend()函数
print(girls)

#insert(位置,'')
girls.insert(1,'刘涛') #
print(girls)