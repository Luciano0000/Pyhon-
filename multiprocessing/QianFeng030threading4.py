# 生产者 , 消费者 : 两个线程之间的通信
''''''
'''
python的queue模块中提供了同步的,线程安全的队列,包括FIFO(先进先出)队列Queue
LIFO(后进先出) 队列LifoQueue,和优先级队列 PriorityQueue , 这些队列都实现了锁原理(
可以理解位原子操作,即要么不做,要么做完),能够在多线程中直接使用
可以使用队列来实现线程间的同步
'''
import threading
import queue
import random
import time


def produce(q):
    i = 0
    while i < 10:
        num = random.randint(1, 100)
        q.put('生产者产生数据:%d' % num)
        print('生产者产生数据:%d' % num)
        time.sleep(1)
        i += 1
    q.put(None)
    # 完成任务
    q.task_done()


def consume(q):
    while True:
        item = q.get()
        if item is None:
            break
        print('消费者获取到:%s' % item)
        time.sleep(4)

    # 完成任务
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(10)  # 长度位10的队列
    arr = []

    # 创建生产者
    th = threading.Thread(target=produce, args=(q,))
    th.start()

    tc=threading.Thread(target=consume,args=(q,))
    tc.start()

    th.join()
    tc.join()

    print('END')