class Player(object):
    numbers=0 #类属性  一般做一些统计 一些共享的设置
    levels=['青铜',"白银","黄金","钻石","王者"]
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

    def show_weapon(self):
       return self.weapon.show_weapon()

class Weapon(object):
    max_damage=100000
    weapons = ['刀', "枪", "剑"]
    def __init__(self, name, damage,weapon):     #self初始化函数
        self.name = name   #实例属性
        self.damage = damage
        self.weapon = weapon
        try:
            if damage > Weapon.max_damage:
                raise  Exception ("最大伤害值为:%d  请重试！" % Weapon.max_damage)
            if weapon not in Weapon.weapons:
                raise Exception ("武器错误")
        except Exception as e:
           print(e)

    def show_weapon(self):
        for k, v in self.__dict__.items():
            print(k, v)



mai=Player("mia",1000,"青铜")
tom=Player("tom",1000,"钻石")

mai.show()
mai.level_up()
mai.level_up()
mai.level_up()
mai.level_up()
mai.level_up()
mai.level_up()
mai.level_up()
mai.show()
tom.show()

gun=Weapon("mia",1000,"刀")
mai.get_weapon(gun)
mai.show_weapon()