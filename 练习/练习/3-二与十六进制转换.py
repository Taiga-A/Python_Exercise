def type_2():
  num = input('请输入一个二进制数字')
  for i in num :
    if i not in ('0','1','.') :
      print('输入不合法，请重新输入！')
      return
    if
  








if __name__ == '__main__' :
  while True :
    mod = input('请选择转换二进制还是十六进制(2/16/exit):')
    if mod not in ('2','16') :
      print('输入不合法，请重新输入！')
      continue
    elif mod == '2' :
      type_2()
    elif mod == '16' :
      type_16()
    elif mod == 'exit' :
      break
  print('感谢使用！')
