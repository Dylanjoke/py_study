import requests


def safe_get(url, params=None, headers=None, timeout=10):
    """发送 GET 请求：成功返回 JSON 数据（dict/list），失败返回 None。"""
    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=timeout,
        )
        response.raise_for_status()  # 状态码非 2xx 时抛出 HTTPError
        return response.json()
    except requests.exceptions.Timeout:
        print(f"请求超时：{url}")
    except requests.exceptions.ConnectionError:
        print(f"连接错误：{url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 请求出错，状态码：{e.response.status_code}, {url}")
    except requests.exceptions.JSONDecodeError:
        print(f"响应不是合法 JSON：{url}")
    except requests.exceptions.RequestException as e:
        print(f"请求异常：{e},{url}")
    return None


if __name__ == "__main__":
    data = safe_get("https://v1.hitokoto.cn/")
    if data is not None:
        print("成功获取数据:", data.get("hitokoto"))
    else:
        print("获取数据失败")

    print("程序结束")
