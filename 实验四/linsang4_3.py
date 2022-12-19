n = int(input("请输入数字：3-求三位的水仙花数，4-求四位的玖瑰花数"))
test = []  # 用于存放所有符合条件的自幂数
for i in range(pow(10, n - 1), pow(10, n)):  # 100-999   1000-9999
    list2 = list(map(lambda y: pow(int(y), n), str(i)))  # 将0-n范围内的每一个数i转换为字符串后，将字符串的每一位字符（数字）映射到pow函数实现求n次方
    if (sum(list2) == i):
        test.append(i)
print(test)
