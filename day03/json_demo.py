import json

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {"street": "123 Main St", "zipcode": "10001"},
}

print("=====原始字典=====")
print(person)
print(type(person))

# 1. 将字典转换为 JSON 字符串
print("=====字典转JSON字符串=====")
json_string = json.dumps(person, indent=4, ensure_ascii=False)
print(json_string)

# 2. 将 JSON 字符串转换回字典
print("=====JSON字符串转字典=====")
back_json_string = json.loads(json_string)
print(back_json_string["name"])
print(back_json_string["skills"][1])
