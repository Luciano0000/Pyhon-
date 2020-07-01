''''''
'''
阻塞式:

    特点: 添加一个任务执行一个任务 , 如果一个任务不结束,下一个任务就进不来 (压根就没有并发....)
    
    进程池:
    pool = Pool(max)  创建进程池
    pool.apply()   阻塞式
    pool.apply_async()  非阻塞式
    
    pool.close()
    pool.join()    让主进程让步
    
    
'''
from multiprocessing import Pool
import time
import random
import os


# 非阻塞式 :

def task(task_name):
    print('开始做任务!', task_name)  # 创建任务
    # 模拟工作时间--------
    start = time.time()
    # 使用 sleep
    time.sleep(random.random() * 2)  # random.random() ---> 0,1之间的随机数
    end = time.time()
    # 模拟时间结束---------

    print('完成任务{} 用时:{},进程id{}'.format(task_name, (end - start), os.getpid()))


# 阻塞式:
if __name__ == '__main__':
    pool = Pool(5)

    tasks = ['听音乐', '玩游戏', '敲代码', '看电视', '散步', '写作业', '工作']  # 七个要执行的工作
    for i in tasks:
        pool.apply(task, args=(i,))

    pool.close()
    pool.join()
    print('over!!!!')
