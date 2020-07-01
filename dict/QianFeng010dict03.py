'''
查询:1. print(变量[key])------>value   若找不到key则 ERor
     2. print(变量.get(key))---->valus 若找不到key 则None 
      #get(key,default) 若找到key 则返回字典中的值,若找不到则返回default值


字典里的函数

items()     返回[(key,value),(,)...]  的list嵌套多个包含'键值对'的tuple

values()    返回[value,value,....]  包含多个value的list

keys()      返回[key,key,.....] 包含多个key的list

get()

in 
'''

dict1 = {'1':'张三','2':'李四','3':'王五',4:'赵六'}
print(dict1['2'])
print(dict1[4])



print('-'*20)



dict2 = {'张三':100,'李四':98,'王五':89,'赵六':99}
#尝试对dict遍历
for i in dict2:
    print(i) 
#遍历的结果:dict所有的key   #失败


print('-'*20)

#items()
print(dict2.items()) 
# dict_items([('张三', 100), ('李四', 98), ('王五', 89), ('赵六', 99)])
#考试分数>90分的人
for key,value in dict2.items():  #for key,value in [(),()...]:
    # print(key,value) 
    if value>90:
        print(key)
   
print('-'*20)

# values():
result = dict2.values()
print(result)       #dict_values([100, 98, 89, 99])
print('-'*10)
#遍历所有的value
for score in dict2.values():
    print(score)



#求所有考试成绩的平均分
scores = dict2.values() #所有value
totle = sum(scores) #score的和
avg = totle/len(scores)
print(avg)

print('-'*20)

#keys():
names = dict2.keys()
print(names)  #dict_keys(['张三', '李四', '王五', '赵六'])
print('-'*10)
for name in dict2.keys():
    print(name)


# in 
print('王五' in dict2.keys()) # True

#get()
print(dict2.get('赵飞')) #None
print(dict2.get('赵飞',89))#
#get(key,default) 若找到key 则返回字典中的值,若找不到则返回default值