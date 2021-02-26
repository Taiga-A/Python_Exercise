import random

num = random.randint(0,2)
txt = ['剪刀','石头','布']
a = int(input('请输入数字：剪刀（0）、石头（1）、布（2）：'))
if a in (0,1,2) :
  print('我出的是',txt[num])
  if a==num:
    print('哼，这次打平了！')
  elif a==(num+1)%3 :
    print('可恶，算你赢了...')
  elif a==(num+2)%3 :
    print('哈，你输啦！')
else :
  print('请正确输入数字！！')
exit()
