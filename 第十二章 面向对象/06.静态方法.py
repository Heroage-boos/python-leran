'''
静态方法
'''
from msilib import knownbits

class Player(object):
    numbers=0 #类属性  一般做一些统计 一些共享的设置
    levels=['青铜',"白银","黄金","钻石","王者"]
    all_weapons = []
    def __init__(self, name, damage,level):     #self初始化函数
        self.name = name   #实例属性
        self.damage = damage
        self.level = level
        Player.numbers+=1

    def show(self):
        print("我是王者荣耀的第%d位玩家，名字是%s ,段位是%s" %(Player.numbers, self.name, self.level))

    def level_up(self):
        index1 = Player.levels.index(self.level)
        if index1 < len(Player.levels)-1:
            self.level = Player.levels[index1 + 1]

    def get_weapon(self,weapon):
        self.weapon=weapon
        self.all_weapons.append(self.weapon)

    def show_weapon(self):
        return self.weapon.show_weapon()


    @classmethod
    def get_players(cls):
        print("王者荣耀用户数已经达到了%d人"%cls.numbers)

    @classmethod
    def get_my_max_weapons(cls):
        max_weapon = 0
        for k in cls.all_weapons:
            print(k.damage)
            if k.damage > max_weapon :
                max_weapon =k.damage

        return max_weapon

    #静态方法
    @staticmethod
    def isvalid(**kwargs):
        print(kwargs)
        if kwargs['damage'] < 10000 :
            return True
        else :
            return False

class Weapon(object):
    max_damage=100000
    weapons_list=["刀","枪","剑"]
    weapons = [{'name':'刀','dam':1000},{'name':'枪','dam':999},{'name':'剑','dam':99}]
    def __init__(self, name, damage,weapon):     #self初始化函数
        self.name = name   #实例属性
        self.damage = damage
        self.weapon = weapon
        try:
            if damage > Weapon.max_damage:
                raise  Exception ("最大伤害值为:%d  请重试！" % Weapon.max_damage)
            if weapon not in Weapon.weapons_list:
                raise Exception ("武器错误")
        except Exception as e:
           print(e)


    def show_weapon(self):
        for k, v in self.__dict__.items():
            print(k, v)

    @classmethod
    def get_max_damage(cls):
        max_weapon = max(cls.weapons, key=lambda x: x['dam'])
        print(max_weapon)  # 输出: {'name': '刀', 'dam': 1000}

# 模拟数据校验
infos={'name':'mia','damage':100000 ,'level':'白银'}
if Player.isvalid(**infos):
    mia = Player("mia", 100000, '白银')
else :
    print("请检查")
