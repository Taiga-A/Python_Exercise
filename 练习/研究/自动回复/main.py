import win32gui
import win32api
import win32clipboard as w
import pyautogui as gui
import time

#############百度识图###################################################################################

import sys
import json
import base64

# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode


# 防止https证书校验不正确
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'q0C1XpQQzOriQ0ur6gr5X19p'

SECRET_KEY = '3B1rYn05tRZAijLa6tQ5ICrySLnvtb4H'


OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()


    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


    # token = fetch_token()
    # image_url = OCR_URL + "?access_token=" + token
    # text = ""
    # file_content = read_file(imgUrl)
    # result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
    # result_json = json.loads(result)
    # for words_result in result_json["words_result"]:
    #     text = text + words_result["words"]

#################百度识图####################################################################################

titleName = input('请输入ID：')

def speak(string1):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(string1)
    w.CloseClipboard()
    gui.hotkey('ctrl','v')
    gui.hotkey('alt','s')


def inPrintText(winxy):
    gui.click(winxy[0][0]+10,winxy[1][1]-120)


def inWindow(winObj):
    win32gui.SetForegroundWindow(winObj)
    winx1, winy1, winx2, winy2 = win32gui.GetWindowRect(winObj)
    win = [[winx1, winy1], [winx2, winy2]]
    return win


def findLastTalk(winxy):
    xy = [winxy[0][0],winxy[0][1],winxy[1][0],winxy[1][1]]
    png = gui.locateOnScreen('./表情.png',xy)
    x1, y1 = gui.center(png)
    x1 += 50
    y1 -= 50
    cy1 = y1
    y1_ = 0
    png = gui.locateOnScreen('./时间.png',xy)
    x2, y2 = gui.center(png)
    x2 -= 50
    y2 -= 50
    cy2 = y2
    y2_ = 0
    
    while True:
        if gui.screenshot().getpixel((x1, y1)) == (255,255,255):
            y1 -= 10
        else :
            y1 += 5
            y1_ = y1-10
            while True:
                if gui.screenshot().getpixel((x1, y1_)) != (255,255,255):
                    y1_ -= 10
                else:
                    break
            break
    
    while True:
        if gui.screenshot().getpixel((x2, y2)) == (255,255,255):
            y2 -= 10
        else :
            y2 += 5
            y2_ = y2-10
            while True:
                if gui.screenshot().getpixel((x2, y2_)) != (255,255,255):
                    y2_ -= 10
                else:
                    break
            break
    # gui.moveTo(x2,y2_)
    xy = [[x1,y1,y1_],[x2,y2,y2_],[cy1,cy2]]
    return xy
    
    
def toEnd(winxy):
    gui.moveTo(x=winxy[0][0]+10, y=winxy[0][1]+120)
    # time.sleep(0.2)
    gui.click()
    gui.press('end')


def inText(imgUrl):
    token = fetch_token()
    image_url = OCR_URL + "?access_token=" + token
    text = ""
    file_content = read_file(imgUrl)
    result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
    result_json = json.loads(result)
    for words_result in result_json["words_result"]:
        text = text + words_result["words"]
    return text


# main


winObj = win32gui.FindWindow(0, titleName)
if winObj != 0:
    pass
else:
    gui.hotkey('ctrl', 'alt', 'z')
    speak(titleName)
    time.sleep(0.5)
    gui.press('enter')
    winObj = win32gui.FindWindow(0, titleName)
    time.sleep(0.5)
    if winObj == 0 :
        print('无效ID')
        exit()
# 获取窗口xy
print('捕获窗口句柄:',winObj)
winxy = inWindow(winObj)
toEnd(winxy)
print('开始进行数据截取')
a = 0
text = []
retext = []
# 包含的关键词及回复
retalk = [
    ['笑','hhhhh'],
    ['早','困'],
    ['睡','呕'],
    ['?','？？？'],
    ['起','起屁'],
    ['不说了','Bye'],
    ['宇哥我','...'],
    ['宇哥','哦'],
    ['就这','害，就这'],
    ['屏蔽','？？？别吧']
]
while True:
    talkxy = findLastTalk(winxy)
    # 比较前后
    if talkxy[0][2] > talkxy[1][2] :
        gui.screenshot('./聊天记录/'+str(a)+'.png',region=(talkxy[0][0],talkxy[0][2],talkxy[1][0]-talkxy[0][0],talkxy[0][1]-talkxy[0][2]))
        print('捕获到聊天内容，正在识别')
        time.sleep(1)
        text.append(inText('./聊天记录/'+str(a)+'.png')) 
        print('此次对话内容:',text[a])
        for i in range(len(retalk)) :
            if retalk[i][0] in text[a] :
                print('查询到关键词:',retalk[i][0])
                retext.append(retalk[i][1])
                break
        if len(retext) != a+1 :
            print('未指定相应关键词回复')
            retext.append('我不知道怎么说')

        print('回复语句:',retext[a])
        inPrintText(winxy)
        speak(retext[a])

        if text[a] == '不说了' :
            print('指定结束语句，程序停止')
            print('总结对话：')
            print('*'*15)
            for i in range(a+1) :
                print('检测:',text[i],'\t回复:',retext[i])
            print('共取得对话次数:',len(text))
            print('*'*15)
            print('感谢使用,再见！！')
            exit()
        a += 1
    else :
        time.sleep(1)
    
