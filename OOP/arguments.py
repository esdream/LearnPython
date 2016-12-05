import inspect

def all_arguments(arg1, arg2):
    pass
print(inspect.getargspec(all_arguments))

class Test():
    name = 'Anna'
    def myfunc():
        pass

t = Test()
setattr(Test, 'test', lambda x:x*x)
# print(t.test(5))
print(inspect.getargspec(t.myfunc))
t.name = 'liu'
print(t.name)
print(Test.name)
del t.name
print(t.name)
