bugs = ["登录闪退", "支付金额错误", "页面加载慢", "数据丢失", "UI显示异常"]

print(bugs[0])  # 取第一个元素
print(bugs[-1])  # 取最后一个元素
print(bugs[1:4])  # 取第二个到第四个元素
print(bugs[::2])  # 取偶数索引的元素
print(bugs[::-1])  # 反转列表
print(len(bugs))  # 列表长度
print("登录闪退" in bugs)  # 判断元素是否在列表中

bugs.append("网络异常")  # 添加元素
bugs.remove("支付金额错误")  # 删除元素
bugs[0] = "登录失败"  # 修改元素
print(bugs)

# 遍历:一个个拿出来处理
for bug in bugs:
    print(f"待处理：{bug}")


# 带序号遍历
for i, bug in enumerate(bugs):
    print(f"{i + 1}. 待处理：{bug}")

# 判断是否在里面
if "数据丢失" in bugs:
    print("数据丢失需要优先处理")
