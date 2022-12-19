x = int(input("请输入一个整数: "))

# 计算百分位
hundred_digit = x // 100

# 计算十分位
ten_digit = (x % 100) // 10

# 计算个数
one_digit = x % 10

# 输出结果
print("百分位:", hundred_digit)
print("十分位:", ten_digit)
print("个数:", one_digit)
