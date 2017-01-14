from threading import local

# local()会调用_localbase.__new__为data对象设置一些属性，然后将data的属性字典(__dict__)作为当前线程的一个属性值（这个属性的 key 是根据 id(data) 生成的身份识别码）
data = local()

data.name = "Thread 1(main)"
print(data.name)

del data.name
print(data.__dict__)
