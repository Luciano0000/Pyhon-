'''
greenlet 已经实现了协程,但是这个是人工切换,太麻烦
python 还有一个比greenlet更强大的能够自动切换的任务模块 gevent
其原理是当一个greenlet遇到IO(指的是 input output)输入输出,比如网络,文件操作,访问网络,就自动切换到其他的greetlet
等到IO完成,在适当的时候切换回来继续执行

由于IO操作非常耗时,经常使程序处于等待状态,有了gevent我们自动切换协程,就保证总有greelet在运行,而不是等待IO

**************猴子补丁**********
    
'''
import time
import gevent
import greenlet
from gevent import monkey

monkey.patch_all() #猴子补丁(替换系统time,变成gevent中的time) 实现自动切换协程

def a():  # 任务a
    for i in range(5):
        print('a' + str(i))
        time.sleep(0.1) # 此时的time.sleep是gevent里面的time.sleep()


def b():
    for i in range(5):
        print('b' + str(i))
        time.sleep(0.1)


def c():
    for i in range(5):
        print('c' + str(i))
        time.sleep(0.1)


if __name__ == '__main__':
    g1=gevent.spawn(a)
    g2=gevent.spawn(b)
    g3=gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()