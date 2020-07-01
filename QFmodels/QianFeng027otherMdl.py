# 第三方模块 request  pip install requests
# requests 模拟浏览器
import requests

response = requests.get('https://www.baidu.com/')
print(response.text)
