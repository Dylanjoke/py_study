import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "登录模块测试用例",
    "body": "验证账号密码正确时可以登录成功",
    "userId": 1,
}

re = requests.post(url, json=payload, timeout=10)

print("状态码：", re.status_code)
print("返回内容：", re.json())
