#封装
class User(object):
    def __init__(self,name,age):
        self._name=name #受保护的变量   不能被修改
        self.__age=age #私有变量  不能被查看和修改

    @property  #装饰器  获取变量
    def age(self):
        return self.__age

    @age.setter   #变量的修改器  age是第八行获取变量的引用
    def age(self,age):
        if isinstance(age,int):
            self.__age = age
        else:
            print("年龄只能是整数")


    #方法也是和属性一样的
    def _show_infos(self):
        print("大家好，我是%s，年龄%d"%(self._name, self.__age))

mia=User("mia",24)
print(mia._name)

#当变量受保护和私有化之后 不允许随便更改  ,私有化变量不能被查看
# print(mia.__age)

# mia._name='小白'
# mia.__age=100
# print(mia.name,mia.age)

#通过类操作属性和方法是可以随意使用的
mia._show_infos()
# 私有化方法不能被查看  其实是因为类将你的变量名和方法改一个名字了
# mia.__show_infos()
print(mia.__dict__)

print(mia._User__age)

#通过类中的get查看和set更改值
# print(mia.age())  #使用装饰器后获取方式变更
# mia.age('二十五')  年龄只能是整数
mia.age=28  #私有化变量设置setter 装饰器后的修改方式
# print(mia.age())  #28   #使用装饰器后获取方式变更
print(mia.age)  #使用装饰器后的获取方式  函数变成了变量