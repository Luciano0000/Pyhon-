# 线程
'''
 创建线程
    模块:
 使用线程


线程状态:
新建------start--------->就绪----------------->cpu(运行)-------------->结束
                         就绪<--------------阻塞<----sleep------cpu(让出)
状态:
    新建 就绪 运行 阻塞 结束

线程允许 共享全局变量

'''
import threading
from time import sleep


def download(q):  # 放入队列
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    # 模拟下载图片
    for image in images:
        print('正在下载', image)
        sleep(0.5)
        print('下载{}成功', format(image))


def listenMusic():
    musics=['大碗款面','土耳其冰淇淋','烤面筋','烤馒头片']
    for music in musics:
        sleep(0.5)
        print('正在听:{}'.format(music))



if __name__ == '__main__':
    # 线程对象
    t = threading.Thread(target=download, name='第一线程', args=(1,))  # 新建状态
    t.start()   # 就绪状态  等待cpu分配

    t1 = threading.Thread(target=listenMusic(), name='第二线程')
    t1.start()

    n = 1
    while True: #主线程
        sleep(1)
        print(n)
        n += 1
