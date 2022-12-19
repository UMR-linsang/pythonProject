def calc_bouncing_ball(h, n):
    Cn = 0
    Hn = h
    for i in range(n):
        Cn += Hn
        Hn *= 0.52
    return Cn, Hn


def main():
    h = int(input("输入小球的初始高度："))  # 小球的初始高度
    n = int(input("输入落地次数："))  # 落地次数

    # 调用 calc_bouncing_ball 函数，并将结果赋给 Cn 和 Hn
    Cn, Hn = calc_bouncing_ball(h, n)

    # 输出小球的总路程和第n次落地的高度
    print("Cn: ", Cn)
    print("Hn: ", Hn)


# 调用主函数
main()
