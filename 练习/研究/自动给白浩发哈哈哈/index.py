import pyautogui as gui

gui.PAUSE = 0.2
# 打开QQ搜索
gui.hotkey('ctrl','alt','z')
gui.moveTo(1500,155)
gui.click()

#切换输入法
gui.hotkey('alt','shift')
if gui.locateOnScreen('./输入法.png'):

  gui.hotkey('alt','shift')
  gui.hotkey('alt','shift')
else:
  gui.hotkey('alt','shift')

# 搜索白大大
gui.typewrite(message="baidada",interval='0.1')
gui.press('space')

#根据头像查找联系人
png = gui.locateOnScreen('./白浩头像.png')
x,y = gui.center(png)
gui.click(x=x,y=y,clicks=2,interval=0.1)

#发送消息
gui.typewrite(' ahhhhhhhh',interval=0.1)
gui.press('space')
# gui.hotkey('alt','s')