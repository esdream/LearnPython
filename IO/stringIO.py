from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world'))
print(f.getvalue())
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read())

file2 = StringIO('good bye Yam')
print(f.tell())
print(f.readline())
