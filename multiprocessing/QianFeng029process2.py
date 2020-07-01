from multiprocessing import Process
from time import sleep
import os


def task1(s, name):
    while True:
        sleep(s)
        print('任务一;;;;;;', os.getpid(), '----------', os.getppid(), name)


def task2(s, name):
    while True:
        sleep(s)
        print('任务二;;;;;', os.getpid(), '----------', os.getppid(), name)


number = 1
if __name__ == '__main__':
    # 子进程p p1
    print(os.getpid())
    p = Process(target=task1, name='任务1', args=(1, 'aa'))  # arg是可迭代的对象传入函数中
    print(p)
    p.start()
    p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
    print(p1)
    p1.start()

    while True: # 主进程
        number += 1
        sleep(0.2)
        if number==100:
            p.terminate()
            p1.terminate()
            break
        else:
            print('-------------number',number)
# 在run当前.py文件的时候系统就已经开辟一个进程了 所以定义的p 和 p1都是子进程
