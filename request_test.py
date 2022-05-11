# import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text[:100])
# print(r.cookies)

# data = {
#     'name': 'germy',
#     'age': 25
# }
# r = requests.get('https://www.httpbin.org/get', params=data)
# print(r.text)
# import requests
# import re
#
# r = requests.get('https://ssr1.scrape.center/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
# 模拟添加请求头
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
# }
# r = requests.get('https://ssr1.scrape.center/', headers=headers)
# print(r.text)


# 模拟post请求
# import requests
#
# data = {'name':'germey', 'age': 25}
# r = requests.post("https://www.httpbin.org/post", data=data)
# print(r.text)


# 状态码
# import requests
#
# r = requests.get('https://ssr1.scrape.center/')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
# 文件上传
# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('https://www.httpbin.org/post', files=files)
# print(r.text)


# 获取cookies测试
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + "=" + value)


# 利用模拟登录GitHub
# import requests # 导入请求模块
#
# headers = {
#     'Cookie':'_octo=GH1.1.805117466.1650969610; _device_id=8debd26aff3e088241464595c5f109ae; user_session=lCIdJXeG1aHzs4L8U0NHikPiPrH9d8y7ZEzmdjUuHdkB1BHp; __Host-user_session_same_site=lCIdJXeG1aHzs4L8U0NHikPiPrH9d8y7ZEzmdjUuHdkB1BHp; logged_in=yes; dotcom_user=Admin233122; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=3cuIQw%2FPs9MHNqAmUrvQs7PcspwQdYSEPKH46YBfRidt8XXoVbFOuKXPMkmhXMJeooHRNvjWIOnBFvMq1jg7IcH5sYeUKXVhXv3h2hMTPBetHClICqwvvoACPI5z4JCfv8eFTbLSadCiQ%2B35a8KNOhLiw6QrcFBsbi%2F41CMBuVn3zb386zyVoSiBM3HVBeI9--2D5HLsYWnz74DzK9--WJsQnIKJd2HeIDPmGigMag%3D%3D',
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
# }  # 模拟请求头，包含了cookie和用户代理
# r = requests.get('https://github.com', headers=headers)  # 指定请求头并解析GitHub网址
# print(r.text)  # 输出网址文本


# 通过cookies参数来设置cookie信息
# import requests  # 导入requests模块
#
# cookies = '_octo=GH1.1.805117466.1650969610; _device_id=8debd26aff3e088241464595c5f109ae; user_session=lCIdJXeG1aHzs4L8U0NHikPiPrH9d8y7ZEzmdjUuHdkB1BHp; __Host-user_session_same_site=lCIdJXeG1aHzs4L8U0NHikPiPrH9d8y7ZEzmdjUuHdkB1BHp; logged_in=yes; dotcom_user=Admin233122; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai; _gh_sess=3cuIQw%2FPs9MHNqAmUrvQs7PcspwQdYSEPKH46YBfRidt8XXoVbFOuKXPMkmhXMJeooHRNvjWIOnBFvMq1jg7IcH5sYeUKXVhXv3h2hMTPBetHClICqwvvoACPI5z4JCfv8eFTbLSadCiQ%2B35a8KNOhLiw6QrcFBsbi%2F41CMBuVn3zb386zyVoSiBM3HVBeI9--2D5HLsYWnz74DzK9--WJsQnIKJd2HeIDPmGigMag%3D%3D'
# jar = requests.cookies.RequestsCookieJar() # 实例化RequestsCookieJar类
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36' } # 设置请求头
# for cookie in cookies.split(';'): # 遍历cookies,以；分隔开
#     key, value = cookie.split('=', 1)  # 使用split筛选出每个cookie的键值
#     jar.set(key, value)  # 设置jar实例的键值对
# r = requests.get('https://www.github.com', cookies=jar, headers=headers)
# print(r.text)
# import requests # 导入requests类
#
# s = requests.session()  # 赋予会话请求给变量s
# s.get('https://www.httpbin.org/cookies/set/name/123456789') # 请求这个测试网站，设置了cookies
# r = s.get('https://www.httpbin.org/cookies') # 再次请求测试网站，并付给变量s
# print(r.text) # 打印所请求的测试网站的文本信息
# import logging  # 导入日志模块
# import requests  # 导入requests模块
#
# logging.captureWarnings(True)
# response = requests.get('https://ssr2.scrape.center/', verify=False) # 请求这个测试网址，并使verify参数布尔值为否，以便忽略ssl证书，将其付给变量response
# print(response.status_code)  # 打印请求状态码
# 超时设置
# import requests # 导入requests模块
#
# r = requests.get('https://httpbin.org/get', timeout=1)
# print(r.status_code)
# import requests
# # from requests.auth import HTTPBasicAuth  # 从requests模块中导入HTTP认证类
#
# r = requests.get('https://ssr3.scrape.center/', auth=('admin', 'admin'))
# print(r.status_code)
