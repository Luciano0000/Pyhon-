#字符串的内建函数 :声明一个字符串,默认可以调用内建函数(系统准备好的一些函数)

#第一部分:大小写相关的(英文)
#capitalize() title() upper() lower()


message = 'zhaorui is a beautiful girl'
#1 capitalize()
msg_capitalize = message.capitalize() #将第一个字符转换为大写
print(msg_capitalize)

#2  title()
msg_title = message.title()  #返回的是 每个单词的首字母大写
print(msg_title)

#3 istitle()  判断是否为以title()返回的值,True False
result = msg_title.istitle() 
print(result)

result_cap = msg_capitalize.istitle()
print(result_cap)

#4 upper()  将字符串全部转成大写的形式  lower()将字符串全部转成小写的形式
msg_upper = message.upper()
print(msg_upper)
a = 'abc'
print(len(a))
a[0:len(a)]
'''
需求: 验证码案例
'''

'''
#注意事项 :
s = 'abc'
print(s[3]) #-->IndexError :string index out of range
#下角标错误:字符串类型的下角标 超出了总长度 
# a b c对应的下角标 -->0 1 2  没有3所以s[3]>总长度 结果就是报错
'''


#开始
# len()函数 字符串长度 返回值是一个整形的数值
import random
s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
# print(len(s)) #62
#四个随机数
code = ''
for i in range(4):
    ran = random.randint(0,len(s)-1)  
    #random.randint(0,61)-->(0,1...61)62个数
    code += s[ran]  # code=s[ran]+r[ran]+s[ran]+s[ran]
print('验证码:'+code)
#提示用户输入验证码
user_input = input('请输入验证码:')
if user_input.lower() == code.lower(): #无论用户输入大写或小写系统都用lower()转成小写来比较
    print('验证码正确')
else:
    print('验证码错误') 
#argument 参数