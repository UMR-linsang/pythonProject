import random
from collections import defaultdict
print("本周表现情况如下：")
list1 = [random.choice([0,1]) for i in range(7)]
frequences = defaultdict(int)
for i in list1:
    frequences[i] += 1
ability =(1-0.05)**frequences[0]+(1+0.08)**frequences[1]
print("本周你放松了{}天".format(frequences[0]))
print("本周你努力了{}天".format(frequences[1]))
print("你本周的能力表现值为:{}".format(ability))
print("以此坚持一学期，20周后你的能力表现值为:{}".format(ability**20))