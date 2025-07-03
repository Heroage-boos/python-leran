
# 基本语法
for i in range(5):
    print('我要吃面，第%d次' %i)


#高斯求和
a=0
for i in range(101):
    a+=i
print(a)

# 阶乘   1！+2！+3！...+n！
# cj=input("请输入要计算的乘阶：")
# cj=int(cj)
result_2=0
for n in range(6):
    if n>0:
        result = 1
        for i in range(n + 1):
            if i > 0:
                result *= i
        result_2 += result
        print(result)
