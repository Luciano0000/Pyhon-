#内置字符串函数()
#查找相关的,  替换
#查询字符串脚标:find() rfind()  index() rindex() lindex()   
#替换相应位置上的字符串:replace()
#编码和解码 :encode() decode()
#判断某字符串是否为xxx开头或或结尾的,返回值True False
#startswith()  endswith()  返回值为波尔类型


#find(str,beg=初始位置0,end=len(string))
s1 = 'index lucy lucky goods'

result = 'l' in s1
print(result)

position = s1.find('R')  #默认从0开始找结束
print(position)  # 返回-1 ---没找到

position = s1.find('l')
print(position)   #如果可以找到,则返回相同字母第一次出现的位置

# find ('要查找的位置',start,end)
p = s1.find('l',position+1,len(s1)-5) #指定开始位置去查找
print(p)
#找到lucky并打印
p2 = s1.find('lucky')
print(s1[p2:p2+5])

#rfind
url = 'https://www.bilibili.com/video/BV1Y741177H8?p=44'
#截取BV1Y741177H8?p=44
a = url.rfind('/') #从右往左找'/'的脚标
print(url[a+1:])

# index()和find()功能一样,不同的是 如果要查找的位置不在字符串上会报异常而find()只会报-1
# p =  'abcde'.index('f')
# print(p)  
#---> ValueError: substring not found

#替换函数 replace(old,new,替换次数)
s1 = 'index lucy lucky goods'
s2 = s1.replace(' ','#')  #' ' 替换成'#'
print(s2)

s2 = s1.replace(' ','')
print(s2)

# 编码: encode()
# 解码 :decode ()
#gbk为中文 gbk2312简体中文  #国际版utf-8
msg = '上课啦!认真听讲'
result = msg.encode('utf-8')  #编码 
#二进制b:b'\xe4\xb8\x8a\xe8\xaf\xbe\xe5\x95\xa6!\xe8\xae\xa4\xe7\x9c\x9f\xe5\x90\xac\xe8\xae\xb2'
print(result)
  
print(result.decode('utf-8')) #解码



#startswith()判断是否以xxx开头的 或者endswith()判断是否以xxx结尾的

filename ='笔记.doc'
result = filename.endswith('txt') #fielname是否是以txt结尾的
print(result)   #-->False


s = 'hello'
result = s.startswith('H') #开头是否为大写的H
print(result)   # -->False

'''
需求:
文件上传:
只能上传图片(jpg)
'''
#分析:要上传的文件路径path--->找到文件名-->通过文件名在判断是否是图片类型
# file = input('请输入要上传的图片文件路径:') #D:\Rose.jpg
# #开始找文件名 注意转义字符\ 
# tagit = file.rfind('\\')  #找到文件名开头
# #切片文件名
# filename_picture = file[tagit+1:] #找到文件名
# #利用做判断 endswith()来判断文件类型
# if filename_picture.endswith('.jpg'):   #若找到结尾是.jpg文件的话 则为True即进入if:
#     print('{}文件已上传'.format(filename_picture))
# else:
#     print('不是图片格式,请上传图片格式的路径')
'''

练习:
     给定一个路径,上传文件(记事本.txt或者图片jpg.png)
     如果不是对应格式的,允许重新指定上传文件
     如果符合上传的规则,提示上传成功
     常用:
while True:   没有上传次数的限制 
      break    结束循环 
'''
#\n  换行   
#\r 回车 
#\t 制表位
#r'\内容'这种格式r才会使''里的字符不转译
j = ' i love you'
print(j.rfind('ov'))

while True:
    file = input('请输入要上传的图片文件路径:') #D:\Rose.jpg
#开始找文件名 注意转义字符\ 
    tagit = file.rfind('\\')  #找到文件名开头  \\:转义字符--->'\'
#切片文件名
    filename_picture = file[tagit+1:] #找到文件名
#利用做判断 endswith()来判断文件类型
    if filename_picture.endswith('.jpg') or filename_picture.endswith('.txt'):   #若找到结尾是.jpg文件的话 则为True即进入if:
        print('{}文件已上传'.format(filename_picture))
        break
    else:
        print('不是图片格式和记事本格式,请上传图片格式的路径')
   



    