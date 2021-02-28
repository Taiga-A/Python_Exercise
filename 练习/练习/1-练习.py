import math
import random
import pyautogui as gui

# print(random.randint(1,5))
# print(random.choice(['白云浩','倪晓宇','梁子航','王宇泽','段泽旋','王博洋']))
# print(str(random.randint(1,255)))

# test1 = '1\number'
# test2 = r'\number' # 全部转义
# test3 = b'number' # 二进制打开
# test4 = 'number'
# print(test1)
# print(test2)
# print(test3)
# print('b' in test4)

# print('-'*20)
# text = 'abcdef'
#   #索引与切片
# print(text[-1])
# print(text[1:3])
# text = '123.txt'
# print(text[-3:])
# print(text[:-4])
# print(text[:])

# text1 = 'Hello_'
# text2 = 'World'
# num = 123
# print(text1+text2+' '+str(num))
# print(text1+text2+' 123'

# str1 = 'strang'
#   #str1[3] = 'A'
# str2 = str1[:3]+'A'+str1[4:]
# print(str2)

# gui.moveTo(x=2667,y=754)

# for i in range(10000):
#   print(i)
# for i in range(0,10):
#   print(i)
# # 0 开始<12条件，每次+3
# for i in range(0,12,3):
#   print(i)

# name = 'abcdefg'
# for i in name:
#   # print(i)
#   print(i,end='\t')

# list 列表
# a = ['aa','bb','cc','dd']
# # for i in range(len(a)):
# #   print(a[i])
# for i in a:
#   print(i)

# i = 0
# num = 0
# while i < 100 :
#   num += i+1
#   i+=1
# print(num)

# pass #空语句

# for a in (1,2,3,4,5,6,7,8,9,10):
#   if a%2 == 0:
#     pass
#   else:
#     print(a)

# for i in range(1,10):
#   for j in range(1,i+1,):
#     print('%d*%d=%d '%(i,j,i*j),end=' ')
#   print('')

# 切片
# grops = [1,2,3,4,5,6,7,8,9]
# print(grops[2:5:2]) => [3,5]


# products = [["iphone", 6888], ["MacPro", 14800], ["小米6 ", 2499], ["Coffee", 31], ["Book   ", 60], ["Nike   ", 699]]
# print('-'*8,' ','商品列表 ','-'*8,end='\n')
# for i in range(len(products)) :
#   print(i,'\t',products[i][0],'\t',products[i][1])
# list1 = []
# while True:
#   num = input('请输入商品编号,q退出：')
#   if num not in ['0','1','2','3','4','5','q']:
#     print('请正确输入！！')
#   elif num == 'q':
#     break
#   else:
#     list1.append(products[int(num)])
# print('退出-结账')
# print('-'*30,end='\n')
# for i in range(len(list1)) :
#   print(i,'\t',list1[i][0],'\t',list1[i][1])
# print('-'*30,end='\n\n')

# Tuple元组 tup = (part1,) / tup = (part1,part2,part3) 一个元素必须加',' 若不加则为基础数据类型
# 元组数据不可修改，但可以加入可变对象（列表），或链接两个元组 Tuple1 = Tuple2 + Tuple3

# dict 字典(类似js里的对象)
# info = {
#   'name':'白云浩',
#   'age':18,
#   'sex':'女'
# }
# # print(info['type']) => 报错
# print(info.get('type')) => None
# print(info.get('type','没有')) => '没有' #可设默认值

def readText():
    try:
        f = open('./txt.txt')
        f.close
    except FileNotFoundError:
        print("未发现‘txt.txt’文件,已创建")
        f = open('./txt.txt','w')
        f.close()
        exit()
    except PermissionError:
        print("没有‘txt.txt’文件权限,请尝试重新创建")
        exit()

    with open('./txt.txt','r') as f :
      data = f.read()
    return data

text = readText()
print(text)