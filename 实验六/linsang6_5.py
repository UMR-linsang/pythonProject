attempts = 0
while attempts < 3:
    username = input("请输入用户: ")
    password = input("请输入密码: ")
    if username == "20200404430534" and password == "666666":
        print("登录成功!")
        exit()
    else:
        print("用户或密码不正确，请重新输入")
        attempts += 1
print("3次用户名或者密码均有误！退出程序。")
