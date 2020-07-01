'''
删除
    1.del 
    #若没有找到key则 报错

    内置函数:
       2. pop()
    注意:pop(key,[default])  
        # [default]的意思是 "default可有可无"
        根据Key 删除字典中的'键值对',只要删除成功,则返回键值对中的value
        如果没有找到Key,则返回default值

        3.popitem():随机删除字典中的键值对(一般大概率删除末尾)

        4.clear():  清空字典
'''
'''
其他的内置函数
1.update()   类似与列表中'+' 指的是两个字典合并
2.fromkeys(seq,[default]) 将seq转成dict的形式,
'''
dict1 = {'张三':100,'李四':98,'王五':89,'赵六':99}
del dict1['张三']
print(dict1)

# del dict1['hah']
# print(dict1)    #KeyError: 'hah'

#pop()
dict1 = {'张三':100,'李四':98,'王五':89,'赵六':99}
dict1.pop('王五')
print(dict1)
result = dict1.pop('邹旭尧','====>没有此值')
print(result)

print('-'*30)

#popitem()
result = dict1.popitem()
print(result)

#update():
dict2 = {'张三':7,'小猪佩奇':67}
result = dict1.update(dict2)
print(dict1)

#fromkeys()
list1 = ['aa','bb','cc']
new_dict = dict1.fromkeys(list1,10)
print(new_dict)