# import httpx
#
# url = 'https://www.httpbin.org/get'  # 输入要解析的url链接
# headers = {
#     'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
# }
# response = httpx.get(url, headers=headers)  # get解析url链接，返回到response变量
# print(response.text)  # 返回响应体
# print(response.headers)  # 返回响应头
# import httpx
#
# client = httpx.Client(http2=True)
# response = client.get('https://spa16.scrape.center')
# print(response.text)
import httpx

headers = {
     'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
 }
url = 'https://httpbin.org/get'
with httpx.Client(headers=headers, http2=True) as client:
    r = client.get(url)
print(r.text)
print(r.http_version)
