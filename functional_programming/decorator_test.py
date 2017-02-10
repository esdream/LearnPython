# coding:utf-8

import functools

def decorator(param):
    if(not isinstance(param, str)):
        @functools.wraps(param)
        def wrapper(*args, **kw):
            print('Begin call')
            print('Call %s():' % param.__name__)
            print('End call')
        return wrapper

    else:
        def realDecorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('Begin call')
                print('%s Call %s():' % (param[0], func.__name__))
                print('End call')
            return wrapper
        return realDecorator

@decorator
def f():
    pass
f()
