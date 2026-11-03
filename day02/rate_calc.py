def calc_pass_rate(test_cases):
    """
    计算通过率。参数是列表，元素是含result键的字典。
    """
    total = len(test_cases)
    if total == 0:
        return 0.0
    passed = 0
    for case in test_cases:
        if case.get("result") == "pass":
            passed += 1
    rate = (passed / total) * 100
    return round(rate, 2)  # 保留两位小数


def get_failed_cases(test_cases):
    """
    获取失败的测试用例列表。参数是列表，元素是含result键的字典。
    """
    failed_cases = []
    for case in test_cases:
        if case.get("result") == "fail":
            failed_cases.append(case)
    return failed_cases


case_list = [
    {"id": 1, "name": "test_login", "result": "pass"},
    {"id": 2, "name": "test_register", "result": "fail"},
    {"id": 3, "name": "test_payment", "result": "pass"},
    {"id": 4, "name": "test_logout", "result": "fail"},
    {"id": 5, "name": "test_profile", "result": "pass"},
    {"id": 6, "name": "test_settings", "result": "pass"},
]

rate = calc_pass_rate(case_list)
print(f"通过率: {rate}%")  # 输出通过率

failed_cases = get_failed_cases(case_list)
print("失败的测试用例:")

failed_cases = get_failed_cases(case_list)
print(f"失败{len(failed_cases)}个测试用例:")
for case in failed_cases:
    print(f"用例ID: {case['id']}, 名称: {case['name']}, 结果: {case['result']}")
