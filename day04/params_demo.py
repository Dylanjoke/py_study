import requests

url = "https://v1.hitokoto.cn/"
params = {
    "c": "i",  # 句子类型，这里选择“i”表示名人名言
    "encode": "json",  # 设置返回数据的格式为 JSON
}

response = requests.get(url, params=params)
print("实际请求的url:", response.url)
print("响应状态码:", response.status_code)
print("内容:", response.json())

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
}

respons = requests.get(
    "https://v1.hitokoto.cn/",
    headers=headers,
    timeout=10,  # 设置超时时间为 10 秒
)

print("发送的请求头:", respons.request.headers)
