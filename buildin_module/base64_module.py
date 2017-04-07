#-*- coding: utf-8 -*-
import base64
encode_b = base64.b64encode(b'string')
print(encode_b)
decode_b = base64.b64decode(encode_b)
print(decode_b)

urlsafe_b = base64.urlsafe_b64encode(b'string')
print(urlsafe_b)
urlsafe_decode_b = base64.urlsafe_b64decode(urlsafe_b)
print(urlsafe_decode_b)

# 能处理去掉`=`的base64解码函数
# def safe_base64_decode(s):
#     complement_num = 4 - len(s) % 4
#     if(complement_num == 4):
#         complement_s = base64.b64decode(s)
#     else:
#         complement_s = base64.b64decode(s + complement_num * '=')
#
# print(safe_base64_decode('YWJjZA=='))
# print(safe_base64_decode('YWJjZA'))

# python2可以通过, python3不能通过，需要深入研究一下
def safe_base64_decode(s):
    if len(s) % 4 == 0:
        return base64.urlsafe_b64decode(s)
    else:
        return safe_base64_decode(s+b'=')
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
