import requests
import time


def fetch_one():
    """取一条数据，失败返回 None"""
    try:
        r = requests.get("https://v1.hitokoto.cn/", timeout=5)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"请求出错：{e}")
    return None

if __name__ == "__main__":
    print("======开始采集 10 条======")
    results = []

    for i in range(1,21):
        item = fetch_one()
        if item:
            results.append(item)
            print(f"  第 {i} 条：{item.get('hitokoto', '')[:30]}...")
        else:
            print(f"  第 {i} 条：失败")
        time.sleep(1)  # 等待两秒，避免过快请求导致 IP 被封禁

    print("\n======采集结束======")

    type_count = {}
    for item in results:
        t = item.get("type", "未知")
        type_count[t] = type_count.get(t, 0) + 1

    print("类型分布：", type_count)
