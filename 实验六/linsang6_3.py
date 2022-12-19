# 初始化变量 T
T = 0

# 循环计算 T 的值
for i in range(1, 101):
    # 如果 i 是奇数，则加上 1/i
    if i % 2 == 1:
        T += 1 / i
    # 如果 i 是偶数，则减去 1/i
    else:
        T -= 1 / i

# 输出 T 的值
print("T =", T)
