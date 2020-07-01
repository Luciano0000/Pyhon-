''''''
'''
-单核CPU实现多任务原理: 操作系统轮流让各个任务交替执行,qq执行2us,切换到微信,在切换回到...执行2us,表面上看每个任务同时执行下去,但是CPU执行
 太快了,导致我们人类感觉所有任务都在同时进行一样
-多核CPU执行多任务原理: 真正的并行执行多任务只能在多核CPU上实现,但是由于任务数量远远多于CPU的核心数量,所以,操作系统也会自动把很多任务轮流
 调度到每个核心上执行

-并发和并行
    -**并发**:当有多个线程在操作时,如果系统只有一个CPU,则根本不可能真正同时进行一个以上的线程,它只能把CPU运行时间划分成若干个时间段,再将
    时间段分配给多个线程执行,在一个时间段的线程代码运行时,其他的线程处于挂起状态,这种方式称为:"并发"
    
    -**并行**:当系统有一个以上的CPU时候,则线程的操作有可能并发,当一个CPU执行一个线程的时候,另一个CPU可以执行另一个线程,两个线程互不抢占CPU资源
    可以同时进行,这种方式称为:"并行"
    
-实现多任务的方式:
-多进程
-多线程
-协程
进程>线程>协程

from multiprocessing import Process
process = Process(target=,name=进程名字,args=(给函数传递的参数))

对象调用方法:
process.start() #启动进程并执行任务
process.run() #只是执行了任务,但是没有启动进程
terminate() #终止进程
'''
# 进程创建:
from multiprocessing import Process
from time import sleep
import os


def task1():
    while True:
        sleep(1)
        print('任务一;;;;;;', os.getpid(), '----------', os.getppid())


def task2():
    while True:
        sleep(2)
        print('任务二;;;;;', os.getpid(), '----------', os.getppid())


if __name__ == '__main__':
    # 子进程p p1
    print(os.getpid())
    p = Process(target=task1, name='任务1')
    print(p)
    p.start()
    p1 = Process(target=task2, name='任务2')
    print(p1)
    p1.start()

# 在run当前.py文件的时候系统就已经开辟一个进程了 所以定义的p 和 p1都是子进程
