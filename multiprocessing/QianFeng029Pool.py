''''''
'''
    当需要创建的子进程数量不多的时候,可以直接利用multiprocessing中Process手动生成多个进程
但是如果是上百甚至上千个目标,手动的去创建进程的工作量非常大,此时就可以用到multiprocessing模块提供的Pool方法.
初始化Pool时,可以指定一个最大进程数,当有新的请求提交到Pool中时,如果池还没有满,那么就会创建一个新的进程用来执行请求;
但是如果池中的进程已经达到指定的最大值,那么该请求就会等待,直到池中有进程结束,才会创建新的进程来执行.


阻塞式

非阻塞式: 
    特点: 全部添加到队列中 , 立刻执行 并没有等待其他进程执行完毕,但是回调函数是等待任务完成之后才调用
'''
from multiprocessing import Pool
import time
import random
import os


# 非阻塞式 :

def task(task_name):

    print('开始做任务!', task_name)# 创建任务
    # 模拟工作时间--------
    start = time.time()
    # 使用 sleep
    time.sleep(random.random() * 2)  # random.random() ---> 0,1之间的随机数
    end = time.time()
    # 模拟时间结束---------

    # 创建回调函数内容:
    return '完成任务{} 用时:{},进程id{}'.format(task_name, (end - start), os.getpid())


container = []


def callback_func(n):  # 回调函数  n接受 return 值
    container.append(n)
    # 解释 : 正常来说这么写是没有办法接受返回值的 , 但是下面代码有apply_async函数的里面如果调用回调方法,则
#我们就需要创建带参数的回调函数,用参数来接受返回值 -------> 就是规定 不用去琢磨.....



# 非阻塞式:
if __name__ == '__main__':
    pool = Pool(5)  # 池子容量 5个子进程

    tasks = ['听音乐', '玩游戏', '敲代码', '看电视', '散步', '写作业', '工作']  # 七个要执行的工作
    for i in tasks:
        pool.apply_async(task, args=(i,), callback=callback_func)
        # apply_async(目标任务,args=(目标任务的参数,),callback=回调方法)-->非阻塞式
        # 回调函数 用来接受 目标函数的返回值

    
    # close 和 join 一定要写在 主进程 前面
    
    pool.close()  # 添加任务结束
    pool.join()  # 堵住主进程 插队在主进程前面

    for c in container:
        print(c)
    print('over!!!!')  # 主进程
