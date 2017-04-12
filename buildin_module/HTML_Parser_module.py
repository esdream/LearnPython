# coding: utf-8
'''
HTML解析
'''
from html.parser import HTMLParser
# from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    # 处理开始标签
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
        print('attr = %s' % attrs)
    # 处理结束标签
    def handle_endtag(self, tag):
        print('</%s>' % tag)

    # 处理开始和结束标签，例如单行标签
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    # 处理数据
    def handle_data(self, data):
        print('data:', data)

    # 处理注释
    def handle_comment(self, data):
        print('<!--', data, '-->')

    # 处理一些特殊字符，例如以&开头的
    def handle_entityref(self, name):
        print('&%s;' % name)

    # 处理特殊字符串，例如以&#开头的，一般是和内码表示的字符
    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
