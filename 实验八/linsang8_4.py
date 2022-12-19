def black_hole(n: int) -> int:
    # 如果 n 位数中出现了重复数字，则不可能是黑洞数
    if len(set(str(n))) != len(str(n)):
        return False

    # 将数字的每一位排序，得到最大数和最小数
    max_num = int(''.join(sorted(str(n), reverse=True)))
    min_num = int(''.join(sorted(str(n))))

    # 如果最大数减去最小数等于原数，则是黑洞数
    if max_num - min_num == n:
        return True
    # 否则，将差值赋值给 n，继续迭代
    else:
        return black_hole(max_num - min_num)


print(black_hole(495))  # 输出 True
print(black_hole(6174))  # 输出 True
print(black_hole(12345))  # 输出 False
