import poplib
import logging
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from datetime import datetime

logging.basicConfig(level=logging.INFO)

def get_email():
    # 输入邮件地址，口令和POP3服务器地址
    email = 'badixue@163.com'
    password = 'fuMG1627049'
    pop3_server = 'pop.163.com'

    # 连接到POP3服务器(是否使用SSL?)
    server = poplib.POP3_SSL(pop3_server, '995')
    # 打开调试信息
    server.set_debuglevel(1)
    # 打印POP3服务器的欢迎文字
    print(server.getwelcome().decode('utf-8'))

    # 身份认证
    server.user(email)
    server.pass_(password)

    # stat()返回邮件数量和占用空间
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号
    resp_one, mails, octets_one = server.list()
    # 查看返回的列表
    print(mails)
    logging.info('''%s
                    resp_one: %s
                    octets_one: %s''' % (datetime.now(), resp_one, octets_one))

    # 获取最新一封邮件，注意索引从1开始
    index = len(mails)
    resp_two, lines, octets_two = server.retr(index)
    logging.info('''%s
                resp_two: %s
                octets_two: %s''' % (datetime.now(), resp_two, octets_two))
    # lines存储了邮件的原始文本的每一行
    # 获取整个邮件的原始文本
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 解析出邮件
    msg = Parser().parsestr(msg_content)
    logging.info('''%s
                msg: %s
                ''' % (datetime.now(), msg))
    # 可以根据邮件索引号直接从服务器删除邮件
    # server.dele(index)
    # 关闭连接
    server.quit()
    print_info(msg)


# 递归打印出Message对象的层次结构
def print_info(msg, indent = 0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('    ' * indent, header, value))
    if(msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('    ' * indent, n))
            print('%s--------------' % ('    ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

# 邮件中Subject或Email中包含的名字都是经过编码后的str，要正常显示，必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
        return value

# 文本邮件的内容也是str，需要检测编码
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

if(__name__ == '__main__'):
    get_email()
