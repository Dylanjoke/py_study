# 1. 用 input() 让用户输入一个游戏名，打印 正在启动：<游戏名>
input_game = input("请输入游戏名：")
print(f"正在启动：{input_game}")

# 2. 让用户输入两个数字，打印它们的和（注意转类型！）
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
print(f"两个数字的和是：{num1 + num2}")

# 3. 定义变量 server = "S102-体验服"，用 .replace() 把它变成 "S102-正式服" 并打印
server = "S102-体验服"
server = server.replace("体验服", "正式服")
print(server)