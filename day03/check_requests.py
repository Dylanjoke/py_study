import json
import requests

url = "https://v1.hitokoto.cn/"

i = 0
while i < 5:
    i += 1
    re = requests.get(url, timeout=10)
    if re.status_code != 200:
        print(f"第{i}次请求失败",re.status_code)
        continue
    print(f"第{i}次请求状态码", re.status_code)
    data = re.json()
    print("内容：", data)
    print("句子：", data["hitokoto"])
