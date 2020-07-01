# 文件操作
'''
文件上传:

系统函数: open()
mode: 
    r   w 纯文本
    rb  wb 二进制
纯文本文件:
    r:read 读
    w:write 写
二进制文件
    b:binary二进制


底层机制
pycham中的open() ------ 流/管道(stream)-------->C:\P1\aa.txt
container<--------------stream---------------<C:\P1\aa.txt
'''
# 读:

# read()
stream = open(r'C:\P1\aa.txt')  # open(path/filename,mode='rt'(默认))--->返回值 :stream (流)
container = stream.read()  # --->读取管道中的内容
print(container)

# readable()
result = stream.readable()  # 判断是否可以读取  True false
print(result)

# readline()
stream2 = open(r'C:\P1\tt.txt')
while True:
    line = stream2.readline()  # 读取一行内容
    print(line)
    if not line:
        break


# readlines()
stream3 = open(r'C:\P1\bb.txt')
lines = stream3.readlines()
print(lines)  # ['adadad\n', 'eqwewq\n', 'qwewq\n']
for i in lines:
    print(i)


# 读图片
# 注意:不要使用默认的读取方式,会一直运行二进制
# stream_photo=open(r'C:\P1\Rose.jpg','rb')
# container_photo=stream_photo.read()
# print(container_photo)

