
'''
当导入一个模块,Python 解析器对模块位置的搜索顺序是:
1.当前目录
2.如果不在当前目录,python 则搜索在shell变量 PYTHONPATH 下的每个目录
3.如果都找不到,python 会查看默认路径 . UNIX下,默认路径一般为/usr/local/lib/python
模块搜索路径存储在 system 模块中的 sys.path 变量中.变量里包含当前目录,PYTHONPTH和有安装过程决定的默认目录
'''

'''
自定义模块
系统模块
'''
import sys
print(sys.path)
print(sys.version)
print(sys.argv) #运行程序时的参数 argv是个列表
