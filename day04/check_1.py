import safe_request
import batch_collect
import time

# 1. 写一个 fetch_with_params(url, params) 函数，内部调用 safe_get
def fetch_with_params(url):
    
    data = safe_request.safe_get(url)
    return data


# 2. 批量请求 20 次，统计成功率和失败率
def batch_collect_times(times):
    results = []
    success_rate = 0
    fail_rate = 0
    for i in range(1,times+1):
        item = batch_collect.fetch_one()
        if item:
            results.append(item)
            success_rate += 1
            print(f"  第 {i} 条：{item.get('hitokoto', '')[:30]}...")
        else:
            fail_rate += 1
            print(f"  第 {i} 条：失败")
        time.sleep(1)
    return results, success_rate, fail_rate

# 3. 断网测试：拔掉网线或关 WiFi 跑一次，确认程序不崩溃且给出友好提示（这才是及格线）
def fetch_with_params(url):
    
    data = safe_request.safe_get(url)
    if data is None:
        print("网络连接失败，请检查您的网络设置")
    return data


if __name__ == "__main__":
    url = "https://v1.hitokoto.cn/"
    data = fetch_with_params(url)
    if data is not None:
            print("成功获取数据:", data.get("hitokoto"))
    else:
            print("获取数据失败")

    print("程序结束")

    rates = batch_collect_times(20)
    print(f"成功次数：{rates[1]}，失败次数：{rates[2]}")