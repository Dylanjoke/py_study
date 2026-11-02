case_list = [
    {"id": 1, "name": "test_login","level": "high", "result": "pass"},
    {"id": 2, "name": "test_register", "level": "medium", "result": "fail"},
    {"id": 3, "name": "test_payment", "level": "high", "result": "pass"},
    {"id": 4, "name": "test_logout", "level": "low", "result": "fail"},
    {"id": 5, "name": "test_profile", "level": "medium", "result": "pass"},
    {"id": 6, "name": "test_settings", "level": "high", "result": "pass"},
]



# 封装 3 个函数：
# 1. celsius_to_fahrenheit(c)：摄氏度转华氏度，返回 c * 9/5 + 32
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

# 2. count_words(text)：统计一段英文里有几个单词（提示：len(text.split())）
# def count_words(text):
#     return len(text.split())
# print(f"单词数量: {count_words('Hello World! This is a test.')}")

input_text = str(input("请输入一段英文文本："))
def count_words(text):
    return len(text.split())
print(f"单词数量: {count_words(input_text)}")
# 3. filter_by_level(cases, level)：从用例列表里筛出指定优先级的用例
def filter_by_level(cases, level):
    filtered_cases = []
    for case_list in cases:
        if case_list.get("level") == level:
            filtered_cases.append(case_list)
    return filtered_cases
print(f"筛选出优先级为 'high' 的用例: {filter_by_level(case_list, 'high')}")