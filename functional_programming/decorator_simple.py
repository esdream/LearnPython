def log(func):
	def add_words():
		print('add my word')
		func()
	return add_words

@log
def func():
	print('name')

func()
print(func.__name__)
