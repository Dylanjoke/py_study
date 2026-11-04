import requests
import time


def request_with_retry(url, max_retry=3, timeout=10):
    """
    带有重试机制的请求函数，最多尝试max_retry次。
    如果所有尝试都失败，则返回None。
    """
    for _ in range(max_retry):
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"请求出错：{e}，正在重试...")
            if _ < max_retry:
                wait = 2**_  # 使用指数退避策略增加等待时间
                print(f"等待{wait}秒后重试...")
                time.sleep(wait)
            else:
                print("多次尝试后仍无法获取数据.")
                return None


result = request_with_retry("https://v1.hitokoto.cn")
if __name__ == "__main__":
    if result:
        print("获取到的数据：", result)
    else:
        print("无法从服务器获取数据。")
