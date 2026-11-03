tester = {
    "name": "张三",
    "age": 25,
    "company": "ABC公司",
    "skills": ["Python", "Java", "C++"],
}

print(tester["name"])  # 访问字典中的值
print(tester.get("age"))  # 使用 get() 方法访问字典中的值
print(
    tester.get("salary", "13K")
)  # 使用 get() 方法访问字典中的值，如果键不存在则返回默认值


print(tester.keys())  # 获取字典的所有键
print(tester.values())  # 获取字典的所有值
print(tester.items())  # 获取字典的所有键值对
print(tester)  # 打印整个字典

tester["age"] = 26  # 修改字典中的值
tester["salary"] = "15K"  # 添加新的键值对
del tester["company"]  # 删除字典中的键值对
tester.pop("skills")  # 删除字典中的键值对

for key in tester:
    print(f"{key}: {tester[key]}")  # 遍历字典中的键值对

for key, value in tester.items():
    print(f"{key} => {value}")  # 遍历字典中的键值对


test_case = [
    {"id": 1, "title": "登录功能", "status": "通过"},
    {"id": 2, "title": "支付功能", "status": "失败"},
    {"id": 3, "title": "搜索功能", "status": "通过"},
]

passed = 0
failed = 0
for case in test_case:
    if case["status"] == "通过":
        passed += 1
    else:
        failed += 1

print(f"共{len(test_case)}条测试用例，通过: {passed}, 失败: {failed}")

print("测试用例详情：")
for case in test_case:
    if case["status"] == "通过":
        print(f"用例ID: {case['id']}, 标题: {case['title']}, 状态: {case['status']} ✅")
    if case["status"] == "失败":
        print(f"用例ID: {case['id']}, 标题: {case['title']}, 状态: {case['status']} ❌")
