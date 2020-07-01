import os
# os models  os.path
# absolute 绝对的  c:\p1\Rose.jpg

# 相对路径
# ***************获取相对路径的前提需要在vsc的中lauch.josn文件中配置swd****************
#**************vsc的中使用os.path.abspath()会有bug建议不要使用,因为vsc默认读取文件方式
#与pycham有所不同,vsc读取的时文件根目录的相对路径方式,所以会有所差别.而debug能解决这个问题
#是因为debug的操作方式是从项目目录出发所以会没有Bug

#************解决方案 鼠标右键项目名选择 获取相对/绝对路径 即可**********s
'''
dict---
        文件1
        文件4s
file--- 
        文件1
for----
        文件1
#dict,file,for 是同级别文件
#文件1,文件4 是同级别


# 假如当前系统在for 文件夹下
r=os.path.isabs(r'../dict/文件4 ') # 找当前文件的上一级文件夹的文件4
print(r)     --->True(存在)
# ../ 代表 返回当前文件的上一级 .在上一级: ../../

r=os.path.isabs(r'dict/文件2 ') # 找跟同级别下的文件2
print(r)    ----->false(不存在)
'''
#获取本文件的目录 : directory  (dir):目录 文件夹
print(os.path.dirname(__file__))
#d:/QianFeng/file/os

#获取同级文件的绝对路径
print(os.path.abspath('test.txt'))
 #vscode 中返回的是当前文件目录同级别的绝对路径D:\QianFeng\[file/os]test.txt 
#[]中的内容vscode默认隐藏
#  而在pycham中返回的是绝对路径d:/QianFeng/file/os/test.txt

#获取当前文件的绝对路径
print(os.path.abspath(__file__))

print(os.getcwd())

