'''
需求：用户输入用户名、密码后，根据用户是否已经注册，用户是否在黑名单中，提示用户是否登录成功。
'''

# 优化前
# user_info=[
#     {'username':"小白",'password':'123456','status':True},
#     {'username':"小白3",'password':'123456','status':True},
#     {'username':"小白3",'password':'123456','status':False}
# ]
#
# # 登录验证
# is_login = False
# login_info = {}
#
# # 添加只能重试输入三次
# for info in range(3):
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     for i, j in enumerate(user_info):
#         if j['username'] == username:
#             if j['password'] == password:
#                 if j['status']:
#                     print('登录成功!')
#                     is_login = True
#                     login_info = j
#                     break
#                 else:
#                     print('您账号已被封禁')
#                     break
#             else:
#                 print('密码错误')
#         else:
#             print('')
#     if is_login:
#         print('登录成功,欢迎您：', login_info['username'])
#         break
#     elif info == 2:
#         print('登录失败三次，限制登录.')
#         break
#     else :
#         print('登录失败请重试')
#


# 优化后
user_info={
    "小白":{'username':"小白",'password':'123456','status':True},
    "小红":{'username':"小红",'password':'123456','status':False},
    "小紫":{'username':"小紫",'password':'123456','status':False},
}

# 登录验证
login_info = {}

# 添加只能重试输入三次
for info in range(3):
    username = input("请输入用户名：")
    password = input("请输入密码：")
    if username in user_info and user_info[username]['password'] == password and user_info[username]['status']:
        print('登录成功,欢迎您：', username)
        login_info = user_info[username]
    elif username in user_info and not user_info[username]['status']:
        print("用户被封禁,请联系管理员")
        break
    elif username in user_info and password != user_info[username]['password']:
        print("密码错误,请重试")
    elif info == 2:
        print('用户不存在请先注册,登录失败三次，限制登录')
        break
    else :
        print("用户不存在请先注册!")




