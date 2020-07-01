#字典 
# 定义 : 变量 ={} 或者 变量=dict()


# dict() 强转类型  
# 注意:dict((key,value),(key,value)) 且 key是唯一的
#      list可以转成字典 ,但是前提:列表中的元素都要成对出现
#       字典当中没有下标一说,任何的操作都离不开key



# dict 的增查
'''
特点 : 1.符号{} 2.关键字 dict 3.保存的元素(element)是:key:value
列表    元组    字典    
[]      ()      {}
list    tuple   dict
ele     ele     key:value


'''

dict1 = {} #常用
dict2 = dict()# 二者相同  都是空字典

dict3 = {'ID':'123456789','nane':'lucky','age':18}
print(dict3)
#key1=ID : value1=12345789  
#key2=name : value2=lucky
#key3=age : value2=18
dict4 = dict([('name','lucky'),('age',18)])
print(dict4)
#列表可以转成字典 但是前提:列表中的元素要成对出现
dict5 = dict(((1,2),(3,4),(5,6),(7,8)))
print(dict5)



#dict 添加:# dict6[key]=value

#特点 :如果字典中存在同名的Key,则发生值的覆盖(后面的值覆盖原来的)
#       如果没有同名的Key,则实现的添加功能(key:value添加到字典)

dict6 = {}

dict6['brand'] = 'huawei' #{'brand': 'huawei'}
print(dict6)

dict6['brand'] = 'mi' #{'brand': 'mi'}  覆盖上一层brand
print(dict6) 

dict6['type'] = 'p30 pro'
dict6['price'] = 9000
dict6['color'] = 'red'
print(dict6) 

