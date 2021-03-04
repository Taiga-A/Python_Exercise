import requests

header = {
    # POST / epidemic/student/sign HTTP/1.1
    'Host': '211.68.191.30',
    'Connection': 'keep-alive',
    'Content-Length': '953',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; VOG-AL00 Build/HUAWEIVOG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 yiban_android',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://211.68.191.30',
    'Referer': 'http://211.68.191.30/epidemic/student/sign',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
    ,'Cookie': 'client=android; JSESSIONID=03AD6A1864C90A7540F11CB23B0F8E96'
}


data = {
    'data': '''{"realName":"王宇泽","collegeName":"渤海校区","className":"计算机科学与技术2006班","studentId":"2020984130604","answer":"{\\"q1\\":\\"是\\",\\"q2\\":\\"是\\",\\"q3\\":\\"是\\",\\"q4\\":\\"是\\",\\"q4_1\\":\\"\\",\\"q5\\":\\"是\\",\\"q6\\":\\"是\\",\\"q6_1\\":\\"\\",\\"position\\":\\"河北省石家庄市裕华区天山南大街32号靠近中国农业银行(天山大街分理处)\\"}"}''',
    'captcha': input('验证码:')
}

# 'data': '''{"realName":"王宇泽","collegeName":"渤海校区","className":"计算机科学与技术2006班","studentId":"2020984130604","answer":"{\\"q1\\":\\"是\\",\\"q2\\":\\"是\\",\\"q3\\":\\"是\\",\\"q4\\":\\"是\\",\\"q4_1\\":\\"\\",\\"q5\\":\\"是\\",\\"q6\\":\\"是\\",\\"q6_1\\":\\"\\",\\"position\\":\\"河北省石家庄市裕华区天山南大街32号靠近中国农业银行(天山大街分理处)\\"}"}''',
# "answer":"{\"q1\":\"是\",\"q2\":\"是\",\"q3\":\"是\",\"q4\":\"是\",\"q4_1\":\"\",\"q5\":\"是\",\"q6\":\"是\",\"q6_1\":\"\",\"position\":\"河北省石家庄市裕华区天山南大街32号靠近中国农业银行(天山大街分理处)\"}"}

r = requests.post('http://211.68.191.30/epidemic/student/sign',data=data,headers=header,verify=False)
print(r.text)
