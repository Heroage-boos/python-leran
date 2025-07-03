# 石头剪刀布，双方轮流出拳，三局两胜   电脑，随机
import  random
from logging import exception


def match_big_small():
    while_number = 0
    player = 0  # 玩家
    computer_number = 0
    while while_number<3:
        a = str(input("请输入石头剪刀布:"))
        while_number+=1
        computer = random.choice(['石头', "剪刀", "布"])
        print('第%d局,玩家出%s 电脑出%s' % (while_number, a, computer))
        try:
            if computer == a:
                print("第%d局,平" % while_number)
            elif a == "石头" and computer == '剪刀':
                player += 1
                print("玩家胜")
            elif a == "剪刀" and computer == '布':
                player += 1
                print("玩家胜")
            elif a == "布" and computer == '石头':
                player += 1
                print("玩家胜")
            elif computer == "石头" and a == '剪刀':
                computer_number += 1
                print("电脑胜")
            elif computer == "布" and a == '石头':
                computer_number += 1
                print("电脑胜")
            elif computer == "剪刀" and a == '布':
                computer_number += 1
                print("电脑胜")
            else:
                while_number -= 1
                raise Exception("不允许出石头剪头布以外的游戏内容，请重新出")

        except Exception as e:
            print(e)
    print("最终得分:玩家：%d 电脑：%d" % (player, computer_number))

match_big_small()