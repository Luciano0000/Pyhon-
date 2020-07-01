# 猴子补丁 案例:爬虫
import requests
import gevent
from gevent import monkey
import urllib.request # 网络请求

monkey.patch_all()

def download(url):
    response = urllib.request.urlopen(url)  # 耗时操作 : 网络请求

    context = response.read()

    print('下载了{}网站的数据,长度:{}'.format(url, len(context)))


if __name__ == "__main__":
    urls = ['http://www.163.com', 'http://www.baidu.com', 'http://www.qq.com']
    g1=gevent.spawn(download, urls[0])
    g2=gevent.spawn(download, urls[1])
    g3=gevent.spawn(download, urls[2])

    # gevent.joinall(g1,g2,g3) # 类似 g1.join().g2...
    g1.join()
    g2.join()
    g3.join()