# 1. 建一个含 5 个游戏名的列表，打印第 1 个、第 3 个、最后一个
list_of_games = ["王者荣耀", "和平精英", "原神", "英雄联盟", "绝地求生"]
print(list_of_games[0])  # 第 1 个
print(list_of_games[2])  # 第 3 个
print(list_of_games[-1])  # 最后一个


# 2. 建一个列表装 3 个字典，每个字典有 用例名 和 状态（pass/fail）
test_cases = [
    {"用例名": "登录功能", "状态": "pass"},
    {"用例名": "支付功能", "状态": "fail"},
    {"用例名": "数据同步", "状态": "pass"},
]


# 3. 遍历它们，把所有 fail 的用例名打印出来
for case in test_cases:
    if case["状态"] == "fail":
        print(case["用例名"])
