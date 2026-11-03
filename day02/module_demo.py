import random
import os
import datetime

print(random.randint(1, 100))  # 生成一个1到100之间的随机整数
print(random.choice(["apple", "banana", "cherry"]))  # 从列表中随机选择一个元素

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 格式化日期时间输出

print(os.getcwd())  # 获取当前工作目录
