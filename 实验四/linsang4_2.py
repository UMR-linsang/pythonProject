list1 = list()
for x in range(11):
    for y in range(21):
        z = 100 - 10 * x - 5 * y
        if z<0:
           pass
        else:
            list1.append([x, y, z])
[print("10元:{}张，5元:{}张，1元：{}张。".format(i[0], i[1], i[2])) for i in list1]
