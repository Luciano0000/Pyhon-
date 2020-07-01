#写文件
# 特点: 若mode='w' 则是写操作
#   write(内容) 每次都会将原来的内容清空,然后写当前的内容 不换行
#   writelines(内容) 清空原来内容, 当前内容可迭代['','']
#   
#   若mode='a'  --> (a)是append --->不会清空原来的内容,在原来内容基础上写
stream=open(r'C:\P1\tt.txt','w') 
print(stream.writable()) #true
s='''
  你好! 
            欢迎来到澳门博彩赌场,赠送给你一个粑粑
                    赌神:高进


'''
rusult=stream.write(s) 
print(rusult) #68
stream.write('老八爱吃粑粑')
stream.close() #释放资源管道



stream1=open(r'C:\P1\xie.txt','a')
stream1.write('欢迎来到博彩体验')
stream1.writelines(['赌神:高进\n','赌侠:小刀\n','赌圣:周星星'])
stream1.close()

