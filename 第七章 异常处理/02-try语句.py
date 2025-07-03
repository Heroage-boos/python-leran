
try:
    print("有可能出现异常的代码")
    n=int(input("请输入一个数字"))
    n=5/n
    print("n的值是%d" % n)

# 根据异常类型进入
except ZeroDivisionError as e:
    print("除数不能为0，请重新输入一个数字")
    print("原始报错信息是：", e) #division by zero
except:
    print("请输入一个数字" )
else:
    print('运行没有被except语句补货，执行else模块')

# 内存清除，文件过滤，数据重置
finally:
    print('无论如何，都要执行finally模块')



