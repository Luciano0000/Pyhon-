# 用户发表文章
# 创建用户对象

#发表文章 ,文章对象

from QianFeng.QFmodels.user.models import User
from QianFeng.QFmodels.articale.models import Article

from QianFeng.QFmodels.calculate import add
user = User('admin', '123')

article = Article('个人总结', '邹旭尧')
user.publish_article(article)

list1=[1,3,4,56,2]
result=add(*list1)
print(result)

MAX=1212