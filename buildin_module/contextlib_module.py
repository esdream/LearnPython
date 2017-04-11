# coding: utf-8
'''
上下文管理模块
'''
from contextlib import contextmanager
class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if(exc_type):
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()

class CreateQuery(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    m = CreateQuery(name)
    yield m
    print('End')

with create_query('Bob') as q:
    q.query()

from contextlib import closing
from urllib2 import urlopen

with closing(urlopen('https//www.python.org')) as page:
    for line in page:
        print(line)

dir(urlopen)
