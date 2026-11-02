import csv
import random

def generate_cases(count):
    """随机生成测试用例数据（模拟从 Excel 读取）"""
    modules = ["登录", "充值", "战斗", "商城", "任务", "设置"]
    results = ["pass", "fail", "block","pass","block","fail"]
    cases = []
    for i in range(1, count + 1):
        cases.append({
            "id": i,
            "module": random.choice(modules),
            "title": f"测试用例 {i}",
            "result": random.choice(results)
        })
    return cases

def calc_stats(cases):
    """统计各状态数量"""
    stats = {"pass": 0, "fail": 0, "block": 0}
    for case in cases:
        stats[case["result"]] += 1
    return stats

def export_to_csv(cases, filename):
    """将测试用例数据导出为 CSV 文件"""
    with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile:
        fieldnames = ["id", "module", "title", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for case in cases:
            writer.writerow(case)

def main():
    print("=====测试用例统计程序=====")
    case_count = int(input("请输入要生成的测试用例数量：") or 50) 
    cases = generate_cases(case_count)
    stats = calc_stats(cases)

    total = len(cases)
    print(f"总用例数: {total}")
    for result, count in stats.items():
        print(f"{result} 数量: {count} 通过率:({(count / total) * 100:.2f}%)")

    export_to_csv(cases, "test_cases.csv")
    export = input("是否导出测试用例到 CSV 文件？(y/n): ").strip().lower()
    if export == 'y':
        export_to_csv(cases, "test_cases.csv")

if __name__ == "__main__":
    main()