import pickle
# 序列化
d = ('name', True, 53)
pickle_obj = pickle.dumps(d)
print(pickle_obj)
# 输出b'\x80\x03X\x04\x00\x00\x00nameq\x00\x88K5\x87q\x01.'
# 使用dumps方法，序列化后输出内容仍在内存中

with open('dump.txt', 'wb') as f:
	x = ('name', True, 53)
	pickle.dump(x, f)
# 使用dumps方法，序列化后内容直接可以写入文件中

# 反序列化
unpickle_obj = pickle.loads(pickle_obj)
print(unpickle_obj)
with open('dump.txt', 'rb') as f:
    unpickle_file = pickle.load(f)
    print(unpickle_file)
