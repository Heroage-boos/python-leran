'''
多态：简单理解，传入不同的参数，使用同一个方法都能进行处理
'''
print(len('123'))
print(len([1,2,3,4,5,6,7,8]))


class Animal(object):
    def speak(self):
        print("动物的叫声")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

class Dog(Animal):
    def speak(self):
        print( "汪汪汪" )

#多态
def speak(object): #animal
    object.speak()

animal=Animal()
animal.speak()
speak(animal)

cat1=Cat()
dog1=Dog()
speak(cat1)
speak(dog1)