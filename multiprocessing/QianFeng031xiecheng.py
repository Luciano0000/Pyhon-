# 协程: 微线程 python独有
# 耗时操作 : 网络请求  网络上传/下载(爬虫)  IO:文件的读写
# 第三方模块:greenlet  完成协程任务
import greenlet
import time


def a():  # 任务a
    for i in range(5):
        print('a' + str(i))
        gb.switch()
        time.sleep(0.1)


def b():
    for i in range(5):
        print('b' + str(i))
        gc.switch()
        time.sleep(0.1)


def c():
    for i in range(5):
        print('c' + str(i))
        ga.switch()
        time.sleep(0.1)


if __name__ == '__main__':
    ga = greenlet.greenlet(a)
    gb = greenlet.greenlet(b)
    gc = greenlet.greenlet(c)

    ga.switch()
