age = 35
name = 'liu'
def foo():
    pass
dictionary = {
    'addr': 'nanjing',
    'fate': [12, 23, 45]
}
# 定义函数，打印各种对象的.__class__和.__class__.__class__
def print_class(var):
    print(var.__class__.__class__)

print_class(age)
print_class(name)
print_class(foo)
print_class(dictionary)

print(dir(type))
