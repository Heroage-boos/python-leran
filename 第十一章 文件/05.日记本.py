def menu():
    while True:
        print("*" * 10)
        print("1.文件阅读")
        print("2.文件写入")
        print("3.退出系统")
        print("*" * 10)
        checked =int(input("请输入:"))
        if checked == 1:
            flag=read_date()
            if flag:
                print("日记读取成功!")
        elif checked == 2:
            flag=write_date()
            if flag:
                print("日记写入成功!")
        elif checked == 3:
            quit()
            break
        else:
            print("无效选项，请重新输入")

def write_date():

    date=str(input("请输入日记日期:"))
    context=str(input("请输入日记内容:"))

    # 读取文件  文件追加
    f = open("./日记本.txt", mode="a+", encoding="utf-8")

    # 写入文件
    f.write("pyrjb\n")
    f.write(date+"\n"+context+"\n")

    # 文件关闭
    f.close()

    return True

def read_date():
    date=input("请输入读取的日期")

    # 读取文件  文件追加
    f = open("./日记本.txt", mode="r", encoding="utf-8")
    content=f.read()

    # 文件关闭
    f.close()

    content=content.split("pyrjb\n")
    for i in content:
        if i[:10] == date:
            print(i)
            return True
    return True

def quit():
    print("退出日记本系统")

menu()
