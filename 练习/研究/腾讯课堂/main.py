from bs4 import BeautifulSoup as bs
import requests

# headers = {
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'cache-control': 'no-cache',
#     'pragma': 'no-cache',
#     'referer': 'https://ke.qq.com/',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'no-cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',

# }
# url = 'https://cgi.connect.qq.com/report/report_vm?monitors=[33593255,33593255,33593256,33593256]&_=,,,&t=0.6944623204718048'

# r = requests.get(url=url,headers=headers)
# print(r.text)
wd = input('关键词：')
r = requests.get(r'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='+wd+r'&fenlei=256&rsv_pq=aeb9b7e600105e44&rsv_t=4e9dSJiLp35iG9uhXw8SJFeXutBKqx7Vf4SIM1yT02scfJ23JOiDefb8U3k&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=10&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=4786&rsv_sug4=5818')
