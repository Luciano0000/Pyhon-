'''
list 函数 
添加 :append   extend  insert

删除 del list[index]    
     remove(e) 移除列表中第一次出现的元素e,返回值是 None,如没有找到删除的指定元素 则报异常

pop()   弹栈  移除列表中的最后一个元素,返回值类是删除的那个元素

clear() 清除所有元素
      
翻转:  reverse()  #列表完全逆序

排序 : sorted()  --->sorted(list)
       sort()---->list.sort()

次数 : count()

枚举 : enumerate(list)  ---->index  value
'''

# 游戏 : '''
# 火锅 hotpot
# 
# '''
hotpot_list =['海底捞','呷脯呷脯','张良麻辣烫','热辣一号','宽板凳']

hotpot_list.append('张良麻辣烫')  #List末尾 加了一个张良麻辣烫


# result=hotpot_list.remove('张亮麻辣烫')  # 移除List中第一个张亮麻辣烫
# print(hotpot_list)

result = hotpot_list.pop()  # 默认删除List末尾元素 
print(result) # 返回被删除元素 
print(hotpot_list.pop(2)) # 也可以指定index(下标)删除
print(hotpot_list)

print(hotpot_list[::-1])  #只是 列表逆序输出打印 ,并没有完全逆序
#reverse()
result_reverse = hotpot_list.reverse()  #列表完全逆序

l=[1,23,4,56,6,6]
l.sort()  #升序
l.sort(reverse=True)  #降序
print(l)
print(l.count(6))


ls =  ['dsadsa','dsadsa',[11,12]]
enumerate(ls)