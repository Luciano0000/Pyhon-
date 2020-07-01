# 字符串    s3地址对应的内存空间与s1,s2不同
s1 = 'abc'
s2 = 'abc'
s3 = '''abc   
'''

print(id(s1),s1)
print(id(s2),s2)
print(id(s3),s3)   # ''' 三引号占用的内存空间id 与单引号的不同


s4 = input('请输入')
s5 = input('请输入')
print(id(s4)==id(s5))  # s4 s5对应id是用户输入之后的内存id
print(s4 == s5)
print(s4 is s5)    #‘==’比较的是内容       'is'比较的是地址


name = 'abcde'
result = 'ce' in name     #  in 返回布尔类型   ce是否在'abcde'出现？  True/False
print(result)    # False

#not in 没有在...里面

name = 'abcde'
result = 'ce' not in name    
print(result) 

# % 字符串的格式化 '%s'%变量
num = int(input('输入一个数字:')) 
print('%s %d'%('重复上方输入的数字内容:',num))

# r 保留原格式   # /' /' 转义字符
print('%s 说: \' 哈哈 \' '%name)  #' \' 内容 \'  '--->打印结果为:'内容'
print(r'%s 说: \' 哈哈 \' '%name)  #  r的功能就是针对转义字符保留原格式

# []   索引值(下标)从0开始  # [:]切片   ******包前不包后*****
filename = 'picture.png'
print(filename[0]) #获取[i]中的i( 012346...)元素
print(filename[0:7])  #[0-7)-->0,1..,6七个数字
print(filename[3:7])  #截取字符串[start:end]不包括end

# 省略
print(filename[3:]) # 省略的是最后的,表示一直取到结尾
print(filename[:7]) # 省略前面,表示默认从0开始取值到end值

#负数
# p   i   c  t  u  r  e  .  p  n  g
# 0   1   2  3  4  5  6  7  8  9  10 正向
#-11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1  反向
print(filename[0:-2])
print(filename[0:9])

print(filename[-1:]) #-1 从右向左取值
print(filename[-5:-1])

#倒叙输出:[::]

     #[start:end:方向和步长]

str1 = 'abcdefg'
print(str1[:])    #正序从start - end  等价于print(str1)
print(str1[::-1])  #逆序从start - end
print(str1[-1:-5:-1])  #[start:end:方向]
print(str1[5:0:-1])    #-1:逆向取值
print(str1[0:5:-1]) #从0开始往左 ,取不到值5-->none
print(str1[5:0:1])  #从5开始往右 ,取不到值0--->none

'''
需求: hello world
1. 逆序输出world
2. 正向输出hello
3. 逆序输出整个hello world
4. 打印获取oll
5. 打印llo wo

'''
num_test = 'hello world'
#1
print(num_test[-1:-6:-1])
#2
print(num_test[:5])
#3
print(num_test[::-1])
#4
print(num_test[4:1:-1])
#5
print(num_test[2:5],' ',num_test[6:8])

# 总结: 1.看标号(空格 也算一个内存) 2. 看方向[±] 3. 看[]数值
  
print(num_test[::2])
print(num_test[::-3])

