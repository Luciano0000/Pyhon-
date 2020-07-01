
# 锁
# 共享数据
# 同步:一个一个完成,排队-->效率低,但是共享数据安全


'''
lock = threading.Lock()
lock.acquire()  请求得到锁
.....
lock.release()  释放锁

只要不释放锁,则其他的线程无法进入运行状态
'''
import threading
import random
import time

lock = threading.Lock()

list1=[0]*10 # 10个0   可变类型 函数可以直接使用

def task1():
    # 获取 线程锁,如果已经上锁,则等待锁释放
    lock.acquire() # 阻塞功能
    for i in range(len(list1)):
        list1[i]=1
        time.sleep(0.5)
    lock.release() #释放锁

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('--->',list1[i])
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)

    t1.start()
    t2.start()

    t2.join()
    t1.join()


