# coding: utf-8
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib'.encode('utf-8'))
print(sha1.hexdigest())

# 计算密码的md5
def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

# 判断用户输入的口令是否正确
def login(db, user, password):
    pass_md5 = add_salt_md5(user, password)
    if(db[user] == pass_md5):
        return True
    else:
        return False

# 加盐md5
def add_salt_md5(user, password, salt = 'Salt'):
        md5 = hashlib.md5()
        md5.update((user+password+salt).encode('utf-8'))
        return md5.hexdigest()

if(__name__ == '__main__'):
    db = {
        'michael': add_salt_md5('michael', 'hello'),
        'bob': add_salt_md5('bob', '123456'),
        'alice': add_salt_md5('alice', 'password')
    }
    print(login(db, 'michael', 'hello'))
