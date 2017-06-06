from email import encoders
from email.mime.base import MIMEBase
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

import smtplib
import os

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令
from_addr = '' # 发送方Email地址
password = ''   # 163,qq等邮箱提供口令进行SMTP发送，与密码区别开
# 输入收件人地址
to_addr = ''    # 收件方Email地址
# 输入SMTP服务器地址
smtp_server = 'smtp.163.com'

# 邮件对象
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr('Python Learner <%s>' % from_addr)
msg['To'] = _format_addr('Administrator <%s>' % to_addr)
msg['Subject'] = Header('From SMTP call...', 'utf-8').encode()

# 邮件正文
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<h1>hello</h1>, send by <p><a href="http://www.python.org">Python...</a><br><img src="cid:0"></p>', 'html', 'utf-8'))

# 添加附件
file_dir = os.path.join(os.path.abspath('.'), 'test.jpg')
with open(file_dir, 'rb') as f:
    # 设置附件的MIME和文件名
    mime = MIMEBase('image', 'jpg', filename = 'test.jpg')
    # 加上头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header("Content-ID", '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
# server.starttls()

server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
