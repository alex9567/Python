from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
 # 输入Email地址和口令:
from_addr = "715255995@qq.com"
password = "kgmfpsrudsvfbgag"
# 输入收件人地址:
to_addr = "891134726@qq.com"
# 输入SMTP服务器地址:
smtp_server = "smtp.qq.com"

import smtplib
#server = smtplib.SMTP(smtp_server, 25)
server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25,QQ邮箱的SSL用465
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print("OK")