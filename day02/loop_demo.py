for i in range(5):
    print(f"第{i + 1}次循环")   # 0,1,2,3,4,

print("---------")

for i in range(1, 6):
    print(f"第{i}次循环")   # 1,2,3,4,5

print("---------")


count = 0
while count < 3:
    print(f"count = {count}")
    print(f"第{count + 1}次循环")   # 0,1,2
    count += 1

print("---------")

for i in range(10):
    if i == 3:
        print("第3次循环结束，退出")
        break
    print(i)   # 0,1,2

print("---------")

for i in range(10):
    if i == 3:
        print("第3次循环结束，跳过")
        continue
    print(i)   # 0,1,2,4,5,6,7,8,9