# 测试URLError
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuqingcai.com/user')
# except error.URLError as e:
#     print(e.reason)


# 测试HTTPError
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')


# 测试先捕获子类的错误再捕获父类的错误
# import urllib.error
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/404')
# except urllib.error.HTTPError as e:
#     print(e.reason, e.headers, e.code, sep='\n')
# except urllib.error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')


# reason返回可能为字符串
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.google.com', timeout=0.1)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
