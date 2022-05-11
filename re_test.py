# import re  # 导入正则表达式模块
#
# content = 'Hello 123 4567 World_This is a Regex Demo'  # 声明一个content字符串
# print(len(content))  # 打印字符串长度
# result = re.match('^Hello.*Demo$', content)   # 使用match方法检查content字符串的正则匹配
# print(result)   # 输出结果，看是否匹配
# print(result.group())   # 输出匹配内容
# # print(result.group(1))  # 输出第一组表达式的结果
# print(result.span())  # 输出匹配范围
import re  # 导入re正则模块

content = '''Hello 1234567 World_This is a 
          Regex Demo'''  # 声明一个content字符串
result = re.match('^He.*?(\d+).*mo$', content, re.S)  # 正则表达式匹配结果赋予result
print(result)  # 输入结果
print(result.group())  # 输入匹配内容
print(result.group(1))  # 输出匹配的第一组

