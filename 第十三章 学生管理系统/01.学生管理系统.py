'''
需求：学生管理系统
学生
老师
班级
课程
'''
# 学生和老师的公共类
class User(object):
    def __init__(self, name, age, gender, in_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.in_number = in_number

    def show_infos(self):  # 显示学生信息
        print( "姓名:%s" % self.name )
        print( "年龄:%s" % self.age )
        print( "性别:%s" % self.gender )
        print( "工号:%s" % self.in_number )

class Student(User):
    # 属性: 姓名 年龄 性别 学号
    def __init__(self, name, age, gender, in_number):
        super().__init__(name, age, gender, in_number)

    def show_infos(self):
        print( "*" * 10 + "学生信息start" + "*" * 10 )
        super().show_infos()
        print( "*" * 10 + "学生信息end" + "*" * 10 )

class Teacher(User):
    # 属性: 姓名 年龄 性别 工号 是否是指导员 、 班级列表
    def __init__(self, name, age, gender, in_number,dao,cla):
        super().__init__( name, age, gender, in_number )
        self.dao=dao
        self.cla=cla

    def show_infos(self):
        print( "*" * 10 + "老师信息start" + "*" * 10 )
        super().show_infos()
        print("是否是导员%s"%['否','是'][self.dao] )
        for i in self.cla:
            print(i,end="\t")
        print( "*" * 10 + "老师信息end" + "*" * 10)

class cla(object):
    # 属性： 班级名称、班级号、辅导员、学生
    def __init__(self, name, in_number, teacher, students):
        self.name = name
        self.in_number = in_number
        self.teacher = teacher
        self.students = students

    def show_infos(self):
        print( "*" * 10 + "班级信息start" + "*" * 10 )
        print("班级名称%s"%self.name )
        print("班级号%s"%self.in_number )
        print("辅导员%s"%self.teacher )
        print("学生")
        for i in self.students:
            print(i.name,end="\t")
        print( "*" * 10 + "班级信息end" + "*" * 10 )

    #增加学生
    def add_student(self, student):
        if student in self.students:
            print("该学生已在班级中，不允许重复操作")
        else:
            self.students.append( student )

    #减少学生
    def sub_student(self, student):
        if student in self.students:
            self.students.remove(student)
        else:
           raise Exception("此学生不在此班级")

class Course(object):
    # 属性 ;课名  课程id 老师  学生列表 课程性质  课程容量
    def __init__(self,name,id_number,teacher,students,type,number):
        self.name = name
        self.id_number = id_number
        self.teacher = teacher
        self.students = students
        self.type = type
        self.number = number
        self.student_number=len(self.students)
        self.valid_number=self.number - self.student_number

    def show_infos(self):
        print( "*" * 10 + "课程信息start" + "*" * 10 )
        print( "课名%s" % self.name )
        print( "课程id%d" % self.id_number )
        print( "老师%s" % self.teacher )
        print( "学生列表:" )
        for i in self.students:
            print(i.name)
        print( "课程性质%s" % self.type )
        print( "课程容量%d" % self.number )
        print( "学生数量%d" % self.student_number )
        print( "剩余容量%d" % self.valid_number )
        print( "*" * 10 + "课程信息end" + "*" * 10 )

    def add_student(self, student):
        if student in self.students:
            raise Exception("学生重复！")
        elif self.valid_number==0:
            raise Exception("此课程学生已满")
        else:
            self.students.append( student )
            self.valid_number-=1
            self.student_number=len(self.students)

    def sub_student(self, student):
        if student in self.students:
            self.students.remove(student)
            self.valid_number += 1
            self.student_number = len( self.students )
        else:
            raise Exception("移除学生失败")

mia=Student("mia",19,"女",1)
tom=Student("tom",19,"女",1)
mia.show_infos()

mia_teacher=Teacher("mia_teacher",30,"女",1,False,['110班'])
mia_teacher.show_infos()
mia_teacher2=Teacher("mia_teacher2",30,"女",1,False,[])
mia_teacher2.show_infos()

cumpoer_1=cla("计算机一班",110,'胜军',[])
cumpoer_1.show_infos()
cumpoer_2=cla("计算机二班",111,'胜军2',[])
cumpoer_2.add_student(mia)
cumpoer_2.show_infos()

course_1=Course("数学",1,"jack",[],"必修课",6)
course_1.show_infos()
course_1.add_student(mia)
course_1.add_student(tom)
course_1.sub_student(tom)
course_1.show_infos()