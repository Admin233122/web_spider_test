# from urllib.parse import urlparse
#
# result = urlparse('https://www.baidu.com/s?wd=周杰伦&rsv_spt=1&rsv_iqid=0xcdead78d000f5030&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=25&rsv_sug1=17&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=5394&rsv_sug4=7205')
# print(type(result))
# print(result)

# from urllib.parse import urlunparse
#
# data = ['https', 'www.baidu.com', 's', '周杰伦', '周杰伦', 'comment']
# print(urlunparse(data))

# from urllib.parse import urlencode
#
# params = {
#     'name': 'germey',
#     'age': 25
# }
# base_url = 'https://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

# 反序列化
# from urllib.parse import parse_qs
#
# query = 'name=germey&age=25'
# print(parse_qs(query))

# 中文编码
from urllib.parse import unquote

keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
