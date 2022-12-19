class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

    def getName(self):
        return self.name

    @classmethod
    def getCount(self):
        return Student.count


list = []
list.append(Student("张丹"))
list.append(Student("里斯"))
list.append(Student("王武"))
for i in list:
    print("学生姓名：", i.getName())
print("学生总人数：", Student.getCount())
