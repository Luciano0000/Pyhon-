# os 内置函数
# getcwd() 获取当前文件的目录
# listdir() 获取目录下的所有文件 保存在list中
# mkdir(目录\该目录要创建的文件夹名) 创建文件夹 一般和os.path.join(目录,文件名)一起连用
# rmdir() 删除空文件夹
# removedirs() 删除多个空文件夹
# remove() 删除文件
# chdir(目标目录) 改变当前目录到目标目录下 结合getcwd()使用
import os
resule_dir = os.getcwd()
print(resule_dir)


# listdir()
result_listdir = os.listdir(r'D:\QianFengPRGM\QianFeng')
print(result_listdir)


if not os.path.exists(r'D:\QianFengPRGM\ok\oktest'):
    # mkdir()
    result_mkdir = os.mkdir(r'D:\QianFengPRGM\ok\oktest')
    print(result_mkdir)


# rmdir()
# result_rmdir=os.rmdir(r'D:\QianFengPRGM\ok\oktest')
# print(result_rmdir)

# removedirs()
# os.removedirs(r'D:\QianFengPRGM\ok\oktest\tst')

# remove()
# os.remove(r'D:\QianFengPRGM\ok\as.txt')

#chdir()
# f=os.chdir(r'目标目录')
# print(os.getcwd())#查看当前目录
'''
综合:
'''
# path = r'D:\QianFengPRGM\ok\oktest\p4'
# filelist = os.listdir(path)  # 获取path目录下的所有文件
# print(filelist)  # ['aa.txt', 'bb.txt']

# for file in filelist:
#     path1=os.path.join(path,file)
#     os.remove(path1)
# else:
#     os.rmdir(path)

# print('删除成功')