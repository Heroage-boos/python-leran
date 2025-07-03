a=1
b=2

# 单分支判断
if a == b:
    print("a and b are equal")
if a < b:
    print("a < b")
if a>b:
    print("a > b")

# 双分支判断
weather='天晴'
if weather=='天晴':
    print("出去玩")
else :
    print("打伞")

# 多分支判断
age=10
if age<=11:
    print("小孩")
elif age>11 and age<18:
    print("青少年")
else :
    print('成年')