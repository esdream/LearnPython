# coding: utf-8
'''
WIP 需要继续编码完成
抓取https://www.python.org/events/python-events/ 中发布的会议时间、名称和地点
'''
from html.parser import HTMLParser

class CrawlerEvent(HTMLParser):
    '''
    '''
    self.flag = False
    def handle_starttag(self, tag, attrs):
        if(tag == 'h3' and attrs['class'] == 'event-title'):
            self.flag = True

    def handle_endtag(self, tag):
        if(tag == 'h3' and self.flag == True):
            self.flag = False

    def handle_data(self, data):
        if(self.flag == True):
            print(data)

if(__name__ == '__main__'):
    crawler = CrawlerEvent()
    crawler.feed()
