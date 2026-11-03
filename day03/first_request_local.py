import requests

url = "http://127.0.0.1:8000/"
re = requests.get(url, timeout=10)

print("状态码", re.status_code)
data = re.json()
print("内容：", data)
print("句子：", data["hitokoto"])