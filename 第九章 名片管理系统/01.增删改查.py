
def menu():
    print("*"*20)
    print(" 1.新建名片\n 2.显示全部\n 3.查询名片\n 0.退出系统")
    print("*" * 20)

menu()

user_list=[]
def add_card(a,b,c):
    print("新建名片")
    user = {
        'name': a,
        'age': b,
        'email': c
    }
    user_list.append(user)
    print("名片添加成功！",list(user_list))


def show_card():
    print("显示全部名片")
    for user in user_list:
        print("用户名%s\t 年龄%d\t 邮箱%s" % (user, user['age'], user['email']))


def select_card(n):
    print("查询名片")
    for user in user_list:
        if n in user['name']:
            return user
        else:
            return False

def deleteCard(name):
    parent_index=-1
    for index in range(len(user_list)):
        if user_list[index]['name'] == name:
            parent_index=index
    user_list.remove(user_list[parent_index])
    print("删除成功!")

def quit_card():
    print("退出系统")

while True:
    try:
        c = int(input())
        if c == 1:
            name = str(input('请输入您的姓名:'))
            age = int(input('请输入您的年龄:'))
            email = str(input('请输入您的邮箱:'))
            add_card(name,age,email)
        elif c == 2:
            show_card()
        elif c == 3:
            name = str(input('请输入要查询的姓名:'))
            user=select_card(name)
            print(list(user))
            if user:
                print("用户名%s\t 年龄%d\t 邮箱%s" % (user['name'], user['age'], user['email']))
            else:
                print("没有找到该名片")
        elif c == 4:
            name=str(input("请输入用户名称"))
            deleteCard(name)
        elif c == 0:
            quit_card()
            break
        else:
            raise Exception("输入的数字不在范围内")
    except Exception as e:
        print(e)








