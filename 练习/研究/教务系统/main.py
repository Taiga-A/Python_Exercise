import requests
import webbrowser as web

headers = {
'Origin': 'http://urp.hebau.edu.cn',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9', 
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
"Content-type": "application/x-www-form-urlencoded; charset=utf-8",
'Content-Type': 'application/x-www-form-urlencoded',
'Referer':'http://urp.hebau.edu.cn/'
}
r_ = requests.post('http://urp.hebau.edu.cn',headers=headers)
web.open('http://urp.hebau.edu.cn/validateCodeAction.do?random=1')

yzm = input('请输入验证码')
data = {
    'dzslh':'',
    'eflag':'',
    'evalue':'',
    'fs':'',
    'lx':'',
    'mm':'zhuan0264',
    'tips':'',
    'zjh':'2020984130604',
    'zjh1':'',
    'v_yzm':yzm
}
headers['cookie'] = str(r_.cookies).split(' ')[1]



def login():
    r = requests.post('http://urp.hebau.edu.cn/loginAction.do',data=data,headers=headers)
    print(r.text)

def getClassText():
  params = {
    'actionType':'6'
  }
  # cookie = {'key': 'UM_distinctid=175622adfba5a4-084f968b88df1-7d677f6e-144000-175622adfbb5a1; JSESSIONID=ead1CVM1k8g406l3mfUFx'}

#   r = requests.get('http://urp.hebau.edu.cn/xkAction.do?actionType=6',params={'actionType':'6'},cookies=r_.cookies)

  return r



if __name__ == '__main__' :
  login()
#   classText = getClassText()
#   print(classText.text)