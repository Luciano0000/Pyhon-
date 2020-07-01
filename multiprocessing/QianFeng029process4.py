# 进程 : 自定义
from multiprocessing import Process


class MyProcess(Process):  # 继承Process类

    def __init__(self, name):
        super(MyProcess, self).__init__()  # 调用Process 的__init__方法 <---------这一步 必须有 进程的执行方式都在Process的__init__中
        self.name = name

    # 重写run方法
    def run(self):
        n = 1
        while True:
            print('-------->自定义进程,n:{}{}'.format(n, self.name))  # 调用Process 的 name
            n += 1


if __name__ == '__main__':
    p = MyProcess('小明')  # 调用自定义进程函数
    p.start()  # 开子进程 开始

    p1 = MyProcess('小红')
    p1.start()
