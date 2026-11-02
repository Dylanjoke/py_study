import random

# 1. 写一个程序：输入一个分数，输出等级（90+ 优秀 / 80+ 良好 / 60+ 及格 / 其他 不及格）

score = float(input("请输入分数："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 2. 写一个循环，打印 1 到 20 中所有能被 3 整除的数
for i in range(1, 21):
    if i % 3 == 0:
        print(i)

# 3. 改造猜数字游戏：加一个"最多只能猜 7 次"的限制，用完就提示失败
random_number = random.randint(1, 100)
attempts = 0

while attempts < 7:
    guess = input("请输入你的猜测（输入'q'退出）：")
    
    if guess.lower() == 'q':
        print("游戏结束。谢谢参与！")
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("请输入一个有效的数字！")
        continue
    
    attempts += 1
    
    if guess < random_number:
        print("太小了！再试一次。")
    elif guess > random_number:
        print("太大了！再试一次。")
    else:
        print(f"恭喜你！你猜对了，数字是 {random_number}。你总共尝试了 {attempts} 次。")
        break

else:
    print(f"很遗憾,你没有在7次内猜对数字。正确答案是 {random_number}。")