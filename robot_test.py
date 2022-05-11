from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://www.baidu.com/robots.txt')
rp.read()
print(rp.can_fetch('Baiduspider', 'https://www.google.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('GoogleBot', 'https://www.baidu.com/homepage/'))

获取robots.txt文件

from urllib import request


url = 'https://www.baidu.com/robots.txt'
response = request.urlopen(url)
print(response.read().decode('utf-8'))

