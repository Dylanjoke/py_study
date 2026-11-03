import requests

re = requests.get("https://v1.hitokoto.cn/", timeout=10)

print("状态码", re.status_code)
print("原始文本", re.text)
print("===============")


data = re.json()
print("解析后：", data)
print("类型：", type(data))
print("句子：", data["hitokoto"])
print("出处：", data["from"])
