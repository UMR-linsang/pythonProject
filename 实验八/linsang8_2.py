import random


def guess_number():
    # 生成1到100之间的随机数
    correct_number = random.randint(1, 100)

    # 给玩家5次机会猜数字
    for i in range(5):
        guess = int(input("请输入您的猜测: "))
        if guess == correct_number:
            print("恭喜你!你猜对了。")
            return
        elif guess < correct_number:
            print("你猜得太低了。")
        else:
            print("你猜得太高了。")

    # 如果玩家在5次尝试后仍未猜出正确的数字，通知他们他们已经输了
    print("抱歉，你已经用了所有的机会了。正确的号码是", correct_number)


guess_number()
