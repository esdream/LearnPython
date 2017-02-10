from io import BytesIO
f = BytesIO()
s = f.write('忽如一夜春风来'.encode('utf-8'))
print(s)
print(f.getvalue())
