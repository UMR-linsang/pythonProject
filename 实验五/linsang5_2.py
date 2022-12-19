dict1 = {'a':'apple','b':'banana','c':'cat'}
key = input("请输入一个Key:")
if key in dict1.keys():
    print("{0}:{1}".format(key,dict1[key]))
else:
    print("您输入的键值不存在！")
