import json

config = {
    "api_url": "https://v1.hitokoto.cn/",
    "timeout": 30,
    "retries": 3,
    "tags": ["语录", "随机", "每日一言"],
}

# 将配置保存到 JSON 文件
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4, ensure_ascii=False)

# 从 JSON 文件读取配置
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)


print("=====从JSON文件读取的配置=====")
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print(loaded_config)
print("api_url:", loaded_config["api_url"])
print("timeout:", loaded_config["timeout"])


data = {
    "code": 200,
    "message": "success",
    "data": {
        "player": {
            "id": 10086,
            "name": "剑圣无双",
            "level": 78,
            "equipments": [
                {"name": "屠龙刀", "atk": 999},
                {"name": "软猬甲", "atk": 0},
            ],
        },
        "server_time": "2026-10-31 20:00:00",
    },
}

# 一层层取
print("=====一层层取=====")
print(data["code"])
print(data["data"]["player"]["name"])
print(data["data"]["player"]["equipments"][0]["name"])

# 安全取值（万一某层不存在也不会崩）
print("=====安全取值=====")
player = data.get("data", {}).get("player", {})
print(player.get("name", "未知玩家"))
print(player.get("vip_level", "无 VIP 信息"))
