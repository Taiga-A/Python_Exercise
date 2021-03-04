import requests
import time
import datetime

r_head = {
  'Host': 'www.yiban.cn',
  'Connection': 'keep-alive',
  'Cache-Control': 'max-age=0',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}


r = requests.post('https://www.yiban.cn/ HTTP/1.1',headers = r_head)
print(r.headers['Set-cookie'])

login_header = r_head
login_header['cookie'] = r.headers['Set-cookie']



data = {
  'account': '13068753010',
  'password': 'zhuan020604',
  'is_rember': '1',
  'keysTime' : round(time.time(),2),
  'captcha' : '久'
}
loginweb = requests.post('https://www.yiban.cn/login?go=https%3A%2F%2Fwww.yiban.cn%2F',data=data)
print(loginweb.text)

# print(r.headers['Set-Cookie'])

# header = {
#     "Accept":"application/json, text/javascript, */*; q=0.01",
#     "Accept-Encoding":"gzip, deflate, br",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "Connection":"keep-alive",
#     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#     "Host":"q.yiban.cn",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
#                  "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#     'cookie': r.headers['Set-cookie']
# }

# user = '13068753010'
# password = 'zhuan020604'

# def login(user,password) :
  


