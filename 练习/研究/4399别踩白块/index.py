# http://www.4399.com/flash/179519_2.htm




import pyautogui as gui

gui.PAUSE = 0.05
# opengame = gui.locateOnScreen('./开始.png')
# if opengame:
#   x,y = gui.center(opengame)
#   gui.click(x=x,y=y)
while True:
  if gui.screenshot().getpixel((550, 930)) == (2, 2, 2):
    gui.click(x=550,y=930)
  elif gui.screenshot().getpixel((700, 930)) == (2, 2, 2):
    gui.click(x=700,y=930)
  elif gui.screenshot().getpixel((850, 930)) == (2, 2, 2):
    gui.click(x=850,y=930)
  elif gui.screenshot().getpixel((1000, 930)) == (2, 2, 2):
    gui.click(x=1000,y=930)