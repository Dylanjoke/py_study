FILE = "bugs.txt"


def add_bug():
    title = input("请输入bug标题：")
    level = input("请输入bug等级（P1/P2/P3，默认P2）：") or "P2"
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{title} | {level}\n")

    print("Bug已添加！")


def show_bugs():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("文件不存在。")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
    if not lines:
        print("没有bug记录。")
        return
    print(f"=====当前bug列表（共{len(lines)}条）=====")
    for i, line in enumerate(lines, start=1):
        level, title = line.strip().split(" | ")
        print(f"{i}. {title} (等级: {level})")


def main():
    while True:
        print("\n=====Bug追踪器=====")
        print("1. 添加bug")
        print("2. 查看bug列表")
        print("3. 退出")
        choice = input("请选择操作（1/2/3）：")

        if choice == "1":
            add_bug()
        elif choice == "2":
            show_bugs()
        elif choice == "3":
            print("退出程序。")
            break
        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()
