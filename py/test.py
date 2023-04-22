import requests

# 发送 GET 请求
response = requests.get('https://www.baidu.com')

# 获取响应内容
content = response.text

# 将响应内容保存为 html 文件
with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('文件已保存为 baidu.html')
