'''
os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。
sys 模块提供了与 Python 解释器和流相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。
time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间计时等。
datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。
random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。
math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等
re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等
ison 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON格式，并从 JSON 格式中解析出 Python 对象。
urllib 模块提供了访问网页和处理 URL的功能，包括下载文件、发送 POST请求、处理 cookies 等。
'''


import random
# 生成随机小数
print(  random.random()  )

# 随机数 1-10
print( random.randint(1,10) )

#获取列表中的随机元素
list1=[1,2,3,4,5,6]
print( list1[random.randint(0,len(list1)-1)] )
print( random.choice('hello'))
# A-Z的ask码
print( ord('A'),ord('Z'))

#生成一个随机字母组成的列表
a = [] #存储随机字符组成的列表
n = 5  #生成单个字符的长度
for item in range(10):
    str=''
    for i in range(n):
        t = random.randint(65, 90)
        # 数字转字母  chr(t)
        str+=chr(t)
    a.append(str)

print('随机字母组成的列表',list(a))

#随机洗牌 
random.shuffle(list1)
print('随机字母组成的列表',list1)
