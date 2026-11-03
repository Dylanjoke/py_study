import json

# 1. 定义一个字典，用 json.dumps 转成字符串，再用 json.loads 转回来

data = {"name": "张三", "age": 30, "is_student": False}
dumps_str = json.dumps(data)
print(type(dumps_str))
loaded_data = json.loads(dumps_str)
print(type(loaded_data))

# 2. 把上面的 data 存成 data.json 文件，再读回来

with open("data.json", "w") as f:
    f.write(dumps_str)

# 读取刚才写入的文件，并解析为字典对象
with open("data.json", "r") as f:
    loaded_config = json.load(f)
print(loaded_config)

# 3. 用 .get() 的方式，安全地取出 "屠龙刀"（即使 equipments 为空也不报错）

equipment = {"剑": 10, "盾牌": 5}
print(equipment.get("屠龙刀", None))  # 输出: None

equipment["匕首"] = 2  # 新增一个装备项
print(equipment)  # 输出: {'剑': 10, '盾牌': 5, '匕首': 2}
