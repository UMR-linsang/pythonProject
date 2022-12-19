# 安装requests
# pip install requests
# 国内源
# pip  install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests

# query = input("输入一个你喜欢的明星")
# url = f'https://www.sogou.com/web?query={query}'

url = 'https://www.sogou.com/web?query=周杰伦'
dic = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"

}
resp = requests.get(url, headers=dic)  # 处理一个小小的反爬

print(resp)
print(resp.text)  # 拿到页面源代码
