import re
p = re.compile(r'^1[3-9]\d{9}$')
tel = input("请输入手机号码\n")
if(p.match(tel)):
    print("你的手机号是:{}".format(tel))
else:
    print("手机号不正确")