import random

red_num = sorted([random.choice(range(99)) for i in range(6)])
blue_num = sorted([random.choice(range(99)) for i in range(2)])
tuple1 = (tuple(red_num), tuple(blue_num))
print(tuple1)
