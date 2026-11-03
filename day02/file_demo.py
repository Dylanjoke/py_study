with open("result.txt", "w", encoding="utf-8") as f:
    f.write("第一条测试结果：\n")
    f.write("第二条测试结果：\n")

print("写入完成！")

with open("result.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的一行：\n")

with open("result.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("=====文件内容如下=====")
    print(content)

with open("result.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


print("=====按行读取文件内容=====")
for line in lines:
    print(line.strip())  # 去掉每行末尾的换行符
