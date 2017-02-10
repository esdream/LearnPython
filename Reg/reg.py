import re

email1 = 'faizal@gmail.com'
email2 = 'bill.gates@microsoft.com'

re_email1 = re.compile(r'([a-zA-Z0-9\_]+)(\.?)([a-zA-Z0-9\_]*)@([a-zA-Z0-9]+).([a-zA-Z]+)')
result1 = re_email1.match(email1)
result2 = re_email1.match(email2)

print(result1.groups())
print(result2.groups())
