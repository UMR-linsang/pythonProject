def get_grade(score):
    if not isinstance(score, int):
        raise TypeError("成绩必须是数值类型")
    if not 0 <= score <= 100:
        raise ValueError("成绩必须在0-100之间")
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "E"


while True:
    try:
        # 获取用户输入并转换为数值类型
        score = int(input("请输入成绩（0-100）："))
        # 调用函数获取成绩等级
        grade = get_grade(score)
        # 输出成绩等级
        print(f"你的成绩等级是：{grade}")
        # 退出循环
        break
    except ValueError as e:
        # 如果输入的成绩不合法，提示错误并继续循环
        print(e)
    except TypeError as e:
        # 如果输入的内容不是数值类型，提示错误并继续循环
        print(e)
