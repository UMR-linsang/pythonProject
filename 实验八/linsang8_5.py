import hashlib


def encrypt(data):
    # 创建 MD5 哈希对象
    m = hashlib.md5()
    # 使用 update() 方法对数据进行加密
    m.update(data.encode('utf-8'))
    # 返回加密后的数据
    return m.hexdigest()


def main():
    # 读取用户名
    username = input("请输入用户名：")
    # 读取密码
    password = input("请输入密码：")
    # 加密用户名和密码
    encrypted_username = encrypt(username)
    encrypted_password = encrypt(password)

    print("未加密的用户名：", username)
    print("未加密的密码：", password)
    # 输出加密后的用户名和密码
    print(f"加密后的用户名：{encrypted_username}")
    print(f"加密后的密码：{encrypted_password}")


if __name__ == '__main__':
    main()
