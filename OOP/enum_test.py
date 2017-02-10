from enum import Enum, unique
Month = Enum('Test', ('Jan', 'Feb', 'Mar', 'Apr', 'May'))

for name, member in Month.__members__.items():
    print(name, member, member.value)

N = {'name': 'liu', 'age': 23}
for key in N:
    print(key, N[key])

class Weekday(Enum):
    Sun = 23
    Mon = True
    Tue = (6, 7)
    Web = 'like'
    Thu = 'like'
    Fri = [1, 5]
    Sat = {'dict': 'rou'}

for name, member in Weekday.__members__.items():
    print(name, member, member.value)
