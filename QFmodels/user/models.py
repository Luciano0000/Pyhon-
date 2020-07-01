__all__ = ['User']


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登陆成功')
        else:
            print('登陆失败')

    def publish_article(self,article):#对象
        print(self.username,'发表了文章:',article.name)

    def show(self):
        print(self.username, self.password)

if __name__=='__main__':
    print('--------user--------')