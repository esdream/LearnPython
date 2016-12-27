class Student():
    def __call__(self):
        print('some')

s = Student()
print(callable(s))
s()
print(callable(max))
