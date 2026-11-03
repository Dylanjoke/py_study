def say_hello():
    print("Hello, World!")


say_hello()  # 调用函数，输出 "Hello, World!"

print("------------------------------")


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # 调用函数，输出 "Hello, Alice!"
greet("Bob")  # 调用函数，输出 "Hello, Bob!"

print("------------------------------")


def add(a, b):
    result = a + b
    return result


sum1 = add(3, 5)  # 调用函数，返回 8
print(f"3 + 5 = {sum1}")
sum2 = add(10, 20)  # 调用函数，返回 30
print(f"10 + 20 = {sum2}")
print(sum1 + sum2)  # 输出 38

print("------------------------------")


def create_bug(title, level="P2", owner="未分配"):
    bug = {
        "title": title,
        "level": level,
        "owner": owner,
    }
    return bug


print(
    create_bug("登录失败")
)  # 输出 {'title': '登录失败', 'level': 'P2', 'owner': '未分配'}
print(create_bug("支付失败", "P1"))  # 只覆盖 level
print(create_bug("头像异常", owner="李四"))  # 指定覆盖 owner
