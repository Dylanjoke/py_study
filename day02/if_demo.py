score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("需要努力")


is_login = True
has_permission = False
level = 60

if is_login and level >= 50:
    print("可以进入游戏")

if level >= 80 or has_permission:
    print("可以查看隐藏商城")

if not has_permission:
    print("没有权限")
