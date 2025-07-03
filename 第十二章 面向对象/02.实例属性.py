class Player:
    def __init__(self, name, age,city):     #self初始化函数
        self.name = name   #实例属性
        self.age = age
        self.city = city

mia=Player('mia', 20,"上海")
tom=Player('tom', 20,"北京")

print(mia.name, mia.age, mia.city)
print(tom.name, tom.age, tom.city)
print(tom.__dict__)
