class Student():
    __slots__ = ('set_name', 'game')
    def __init__(self, arg1, arg2):
        self.set_name = arg1
        self.game = arg2
    right = 20
def set_name():
    print('s')
game = 10
s = Student(set_name, game)
s.set_name()
print(s.game)

print(dir(Student))
