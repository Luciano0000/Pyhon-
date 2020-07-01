#os.path  常用:
#os.path.split() 分割(目录,文件名)
#os.path.splitext() 分割(目录文件名,.扩展名)
#os.path.getsize() 获取文件大小 (单位时字节)
#os.path.isabs() 判断是绝对路径吗? 返回 true false
#os.path.isfile() 是一个文件吗?
#os.path.isdir() 是一个文件夹吗?
#os.path.join(,) 合并
#os.path.exists(目录) 这个目录存在吗? 
import os
path=r"D:\QianFengPRGM\QianFeng\file\os\QianFeng019file2.py"
#获取文件名的两种方法:
#1.用rfind()函数与切片结合
filename=path[path.rfind('\\')+1:]
print(filename)

#2.用os模块中的split()函数获取包含两个元素的tuple,然后找到脚标位文件名的即可
split=os.path.split(path)
print(split)
print(split[1])

#splitext()
result=os.path.splitext(path)
print(result)
print(result[1])

#getsize()
result_size=os.path.getsize(path)
print(result_size)

result_join=os.path.join(os.getcwd(),'a','a1.jpg')
print(result_join)