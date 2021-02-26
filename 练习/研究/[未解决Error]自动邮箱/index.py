# 负责发送邮件
import email
# 负责邮件格式
import smtplib
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮箱域名
mail_host = "foxmail.com"
# 发件人邮箱
mail_sender = "zedada264@foxmail.com"
# 授权码
mail_license = "eonetlcbwlmrdfjc"
# 收件人邮箱
mail_receivers = ['2738890162@qq.com']

# 新建邮箱对象
mm = MIMEMultipart('related')

# 设置邮件内容  html/plain
message_text = MIMEText('''
这是一个测试
''','plain','utf-8')

# 以下四项显示在邮件里
# 邮件主题
subject_content = """Python邮件测试"""
# 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
mm["From"] = "A某澤<zedada264@Foxmail.com>"
# 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
mm["To"] = "城市□流芳百世<2738890162@qq.com>;"
# 设置邮件主题
mm["Subject"] = Header(subject_content,'utf-8')

  # # 二进制读取图片
  # image_data = open('图片.后缀','rb')
  # # 设置读取获取的二进制数据
  # message_image = MIMEImage(image_data.read())
  # # 关闭刚才打开的文件
  # image_data.close()
  # # 添加图片文件到邮件信息当中去
  # mm.attach(message_image)

  # # 构造附件
  # atta = MIMEText(open('文件.后缀', 'rb').read(), 'base64', 'utf-8')
  # # 设置附件信息
  # atta["Content-Disposition"] = 'attachment; filename="文件.后缀"'
  # # 添加附件到邮件信息当中去
  # mm.attach(atta)

# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱的域名和端口，端口地址为25
stp.connect(mail_host, 25)  
# set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
stp.login(mail_sender,mail_license)
# 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
# 关闭SMTP对象
stp.quit()