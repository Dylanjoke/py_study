name = " HelloWorld "

print(len(name))  # 长度
print(name.strip())  # 去掉首尾空格
print(name.upper())  # 大写
print(name.lower())  # 小写
print(name.replace("Hello", "Python"))  # 替换
print(name.split("o"))  # 分割

level = 45
gold = 1280
print(f"等级是{level}金币是{gold}")  # f-string
# print("等级是", level, "金币是", gold)    # 逗号分隔
# print("等级是" + str(level) + "金币是" + str(gold))
# print("等级是%d金币是%d" % (level, gold))    # 占位符
# print("等级是{}金币是{}".format(level, gold))    # format
# print("等级是{0}金币是{1}".format(level, gold))    # format
# print("等级是{level}金币是{gold}".format(level=level, gold=gold))    # format
# print("等级是{level}金币是{gold}".format_map({"level": level, "gold": gold}))    # format_map
