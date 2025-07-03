'''
包是Python模块的一种组织形式，将多个模块组合在一起，形成一个大的Python工具库。包通常是一个拥有__init_-.py文件的目录，它定义了包的属性和方法。
'''
from my_package import my_math
from my_package import card
from my_package import my_tools

print(my_math.add(3,4))

print("*"*10)
print("请选择菜单项")
print("1.卡片系统")
print("2.生成随机验证码")
print("请选择菜单项")
print("*"*10)

input_=int(input("请选择菜单项"))

if input_==1 :
    card.start_menu()
elif input_==2:
    my_tools.yanzhengma(8)


