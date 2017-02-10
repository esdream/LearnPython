# 从wsgiref模块引入符合WSGI规范的服务器
from wsgiref.simple_server import make_server
# 导入自己编写的application
from hello import application

# 创建一个服务器，ip为空，端口是8000，处理函数是application
httpd = make_server('', 8000, application)
print('Servering HTTP on port 8000...')
# 监听HTTP请求
httpd.serve_forever()
