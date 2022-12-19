from collections import namedtuple

Student = namedtuple('Student', 'name age gender')
s=list()
s.append(Student('xiaoming', 20, 'boy'))
s.append(Student('xiaohua', 19, 'girl'))
s.append(Student('xiaochao', 20, 'girl'))
for i in s:
    print('姓名：%s，年龄：%d，性别：%s。' % i)