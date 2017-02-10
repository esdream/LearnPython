class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score


ammy = Student('ammy', 35)
print(ammy.__name)
