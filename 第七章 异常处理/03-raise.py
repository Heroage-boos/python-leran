# pwd = input("请输入你的密码：")
# if len(pwd) < 6:
#     raise ValueError("密码长度不能少于6位")  # 抛出异常，提示用户密码长度不合法
# else:
#     print('登录操作')

try:
    pwd = input("请输入你的密码：")
    if len(pwd) < 6:
        raise Exception("密码长度不能少于6位")  # 主动抛出异常
except Exception as e:
    print(f"发生异常: {e}")  # 捕获异常并打印
