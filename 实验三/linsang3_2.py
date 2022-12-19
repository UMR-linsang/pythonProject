import re
p = re.compile(r'^[1-9]\d{14}(\d{2}[0-9X])?$')
iden = input("请输入身份证号码\n")
if(p.match(iden)):
    print("你的身份证号是:{}".format(iden))
else:
    print("身份证号不正确")