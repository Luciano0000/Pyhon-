# 死锁
'''
开发过程中使用线程,在线程间共享多个资源的时候
如果两个线程分别占有一部分资源并且同时等待对方的资源,就会造成死锁
尽管死锁很少发生,但是一旦放生就会造成应用停止响应,程序不做任何事情


避免死锁:
    解决:
    1,重构代码
    2,使用acquire(timeout=)
'''
from threading import Thread,Lock
import time

lockA=Lock()
lockB=Lock()


#自定义线程:
class myThread(Thread):

    # 重写父类 run() 方法
    def run(self): # start()
        if lockA.acquire(): #acquire()返回值是一个bool类型 , 如果可以获取到锁则返回True
            print(self.name+'获取了A锁') #name是父类Tread类中的变量
            time.sleep(0.1) #转让执行权
            if lockB.acquire(timeout=2): # 阻塞等待
                print(self.name+'又获取了B锁,原来还有A锁')
                lockB.release()
            lockA.release()


class myThread1(Thread):
    def run(self): # start()
        if lockB.acquire():
            print(self.name+'获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=2):
                print(self.name+'又获取了A锁,原来还有B锁')
                lockA.release()
            lockB.release()

if __name__ == '__main__':
    t1=myThread()
    t2=myThread1()

    t1.start() #执行run()函数
    t2.start()
