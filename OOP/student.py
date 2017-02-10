from types import MethodType
class Student(object):
    __slots__ = ('name')
    def get_name(self, name):
        self.name = name
        print(self.name)

s = Student()
s.name = 'Michael'
print(s.name)

def set_name(self, name):
    self.name = name
    print(self.name)
s.get_name('Wang')
# s.set_name = set_name
# s.set_name(s, 'Li')
# s.set_name = MethodType(set_name, s)
# s.set_name('kao')

def set_age():
    pass
Student.set_age = MethodType(set_age, Student)
