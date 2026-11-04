import requests
import json
import csv
import os
import time
from datetime import datetime

API_URL = "https://v1.hitokoto.cn/"
OUTPUT_JSON = "quotes.json"
OUTPUT_CSV = "quotes.csv"


def fetch_quotes():
    """从一言API获取数据"""
    try:
        r = requests.get(API_URL, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"    请求失败: {e}")
        return None


def clean_item(raw):
    """清理数据，使之更适合存储"""
    if not raw:
        return None

    content = (raw.get("hitokoto") or "").strip()
    if len(content) > 30:
        return None
    # if raw.get("length", 0) > 30:
    #   return None
    # length 其实是冗余字段 它就是句子长度，用 len(content) 自己算更可靠，还能顺便去掉对 API 字段的依赖
    return{
        "content": raw.get("hitokoto","").strip(),
        "source": raw.get("from","未知"),
        "type": raw.get("type", "未知"),
        "length":raw.get("length",0),
        "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def load_existing():
    """读取已有的数据（用于去重）"""
    if not os.path.exists(OUTPUT_JSON):
        return []
    try:
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        return []


def save_json(data):
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_csv(data):
    if not data:
        return
    with open(OUTPUT_CSV, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()  # 写入表头
        writer.writerows(data)
    print(f"    已保存 {len(data)} 条数据到 {OUTPUT_CSV}")


def main():
    exisiting = load_existing()
    seen = {item["content"] for item in exisiting}
    print(f"    已有 {len(exisiting)} 条数据")

    want = int(input("    你想采集多少条数据？"))
    new_count = 0

    for i in range(1, want + 1):
        raw = fetch_quotes()
        item = clean_item(raw)
        if item and item["content"] not in seen:
            exisiting.append(item)
            seen.add(item["content"])
            new_count += 1
            print(f"    第 {i} 条：{item['content'][:30]}...")
        else:
            print(f"    第 {i} 条：重复或失败")
        time.sleep(2)

    save_json(exisiting)
    save_csv(exisiting)
    print("\n======采集结束======")
    print(f"    新增 {new_count} 条数据，共 {len(exisiting)} 条")


if __name__ == "__main__":
    print("======开始采集======")
    main()