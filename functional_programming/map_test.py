# -*- coding: utf-8 -*-
def normalize(name):
    if name == None:
        return 'No Name'
    else:
        nor_name = [letter.lower() for letter in name]
        nor_name[0] = nor_name[0].upper()
        return ''.join(nor_name)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
