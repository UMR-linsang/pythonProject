class HeightError(Exception):
    """身高异常"""

    def __init__(self, message):
        self.message = message


def check_height(height):
    if height < 50 or height > 250:
        raise HeightError("身高超出范围")


def main():
    try:
        height = int(input("请输入身高(厘米)："))
        assert 50 <= height <= 250, "身高超出范围"
        weight = int(input("请输入体重(千克)："))
        assert 0 < weight <= 1000, "体重超出范围"
    except ValueError:
        print("输入无效，请输入整数")
    except AssertionError as e:
        print(e)
    else:
        try:
            check_height(height)
        except HeightError as e:
            print(e.message)
        else:
            standard_weight = height - 100  # 计算标准体重
            if weight <= standard_weight + 5 and weight >= standard_weight - 5:
                print("体重正常")
            elif weight > standard_weight:
                print("体重超标")
            else:
                print("体重不达标")


main()
