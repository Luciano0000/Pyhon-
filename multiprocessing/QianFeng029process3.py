from multiprocessing import Process
from time import sleep
import os

m = 1 #不可变类型
list = []  # 可变类型

def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list.append(str(m)+'task1')
        print('任务一;;;;;;',m,list)


def task2(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list.append(str(m)+'task2')
        print('任务二;;;;;',m,list)


number = 1  # 主进程
if __name__ == '__main__':
    # 子进程p p1 
    print(os.getpid())     
    p = Process(target=task1, name='任务1', args=(1, 'aa'))  # arg是可迭代的对象传入函数中
    print(p)
    p.start()
    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    print(p1)
    p1.start()

    while True:
        sleep(1)
        m+=1
        print('---------mian',m)
# 在run当前.py文件的时候系统就已经开辟一个进程了 所以定义的p 和 p1都是子进程
