# import http.cookiejar, urllib.request
#
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)


import urllib.request, http.cookiejar

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie_1.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))


