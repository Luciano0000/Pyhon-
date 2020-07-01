'''
线程是可以共享全局变量的

*************但是 当全局变量数值非常大的时候,多线程会出现一个问题 :*************
n-=1  这个操作 在解释器中是分为两步进行的 : 先n-1 然后 把n-1 赋值给n  ,而恰恰在这两步之间会存在时延,这时其它的线程
会占有当前线程状态,这样下来 实际的运行线程之后的n值要远远比理想数值要小的多 即:共享数据不安全(线程不同步)

解决方案:
GIL : 全局解释器锁

    将每个进程加锁,只有当 当前cpu分配的线程结束后 其他线程才能进入状态

    cpu判断线程计算量 ,当没有达到临界计算量的时候GIL会一直存在,当线程计算量超过临界状态,GIL会自动释放,
    虽然这样真正的实现了多线程并且达到了很快的速度,但是就会出现问题: --->"线程不同步" 共享数据不安全
GIL缺点: 速度慢

'''
'''
进程:计算密集型
线程:耗时操作的时候(网上下载,爬虫,IO)
'''
import threading
from time import sleep

ticket = 0


def run1():
    global ticket
    for i in range(1000000):
        # sleep(0.0001)
        ticket += 1


def run2():
    global ticket
    for i in range(1000000):
        ticket += 1


if __name__ == '__main__':
    sp1 = threading.Thread(target=run1, name='抢票线程1')
    sp2 = threading.Thread(target=run2, name='抢票线程2')

    sp1.start()
    sp2.start()

    sp1.join()
    sp2.join()

    print('ticket:', ticket)
