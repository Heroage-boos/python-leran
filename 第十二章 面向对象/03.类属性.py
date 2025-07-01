class Player:
    numbers=0 #类属性  一般做一些统计 一些共享的设置
    max_damage=100000
    level=["青铜","白银","黄金","铂金"]
    def __init__(self, name, damage,level):     #self初始化函数
        self.name = name   #实例属性
        self.damage = damage
        self.level = level
        Player.numbers+=1

        try:
            if damage > Player.max_damage:
                raise  Exception ("最大伤害值为:%d  请重试！" % Player.max_damage)
            if level not in Player.level:
                raise Exception ("段位错误")
        except Exception as e:
           print(e)


mai=Player("mia",1000,"青铜")
tom=Player("tom",1000,"钻石")

print('欢迎荣耀王者第 %d 个玩家注册' % Player.numbers)
