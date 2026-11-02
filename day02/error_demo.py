try:
    num = int(input("请输入一个数字："))
    result = 100 / num
    print(f"100 除以 {num} 的结果是: {result}")
except ValueError:
    print("输入的不是一个有效的数字！")
except ZeroDivisionError:
    print("除数不能为零！")
except Exception as e:
    print(f"发生了一个意外的错误: {e}")
else:
    print("计算成功，没有发生异常。")
finally:
    print("程序执行结束。")