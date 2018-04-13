"""
定义一个学生类.
"""


# 定义一个空的类
class Student():
    # 一个空类pass  代表直接跳过
    pass
# 定义一个对象
# mingyue = Student()


class PythonStudent():
    name = None
    age = 18
    course = "python"

    def doHomework(self):
        print("I  在做作业")
        # 推荐在函数末尾returned

        return None
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
print(yueyue.doHomework())


