class User(object):
    def __init__(self,name):
        print("__init__被调用")
        self.__name=name

    # 魔法方法
    def __str__(self):
        print('hello')
        return  "我的名字是%s" % self.__name

    def __add__(self,other):
        return self.name+other.name

    def __eq__(self, other):
         return self.name==other.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name


mia=User("mia")
print( str([1,2,3]),type(str([1,2,3])))
print(str(mia))  # hello   我的名字是mia

jake=User("jake")
#直接打印报错 使用修改后的__add__魔发方法后有效
print(mia+jake)  #miajake

print(9==8)
print(mia==jake)  #miajake
