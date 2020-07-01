# 文件的复制粘贴
# 批量文件的复制粘贴  os模块
'''
原文件:c\p1\Roes.jpg
目标文件: c\p2\Rose.jpg

使用 with ...as  可以帮助我们自动释放资源管道
'''
# 分析: 需要建立两个管道 (一个是读入in mode='rb',一个是写出Out mode='wb'
# 原文件----rb---> container-----wb----->目标文件
import os
with open(r'C:\P1\Rose.jpg', 'rb') as stream:  # 等价于stream=open(内容) 自动关闭流
    container = stream.read()  # 读取文件内容

with open(r'C:\P2\Rose.jpg', 'wb') as w_stream:
    w_stream.write(container)  # 将读取的文件放入write()中通过w_stream流写到目标文件

print('文件复制成功')

with open(r'C:\P1\Rose.jpg', 'rb') as stream:  # 等价于stream=open(内容)
    container = stream.read()  # 读取文件内容
    print(stream.name)  # 打印C:\P1\Rose.jpg
    file = stream.name
    filename = file[file.rfind('\\')+1]  # 截取文件名

    path = os.path.dirname(__file__)
    # os.path.dirname(__file__)当前文件目录(绝对路径)
    path_all = os.path.join(path, filename)
    # os.path.join(目录,文件名) 返回的是一个拼接后的新路径

    with open(path_all, 'wb') as wstream:
        wstream.write(container)

with open('wtest.txt', 'w') as wsteam2:  # 默认写道当前文件夹
    wsteam2.write('hello')
