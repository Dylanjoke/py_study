import random

target_number = random.randint(1, 100)
attempts = 0

print("欢迎来到猜数字游戏！")
print("我已经选择了一个1到100之间的数字。你能猜到它吗？")

while True:
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
    
    if guess < target_number:
        print("太小了！再试一次。")
    elif guess > target_number:
        print("太大了！再试一次。")
    else:
        print(f"恭喜你！你猜对了，数字是 {target_number}。你总共尝试了 {attempts} 次。")
        break