# 进程间的通信
from multiprocessing import Process
from time import  sleep
from multiprocessing import Queue


def download(q): # 放入队列
    images = ['girl.jpg','boy.jpg','man.jpg']
    #模拟下载图片
    for image in images:
        print('正在下载',image)
        sleep(0.5)
        q.put(image)

def getfile(q): # 从队列取值
    while True:
        try:
            file=q.get(timeout=3)
            print('{} 保存成功'.format(file))
        except:
            print('全部保存完毕')
            break



if __name__ == '__main__':

    q=Queue(5) # 队列长度为5
    p1 = Process(target=download,args=(q,))
    p2 = Process(target=getfile,args=(q,))

    p1.start()
    p1.join() # 插队 -->优先 p1.start()
    p2.start()
    p2.join()
