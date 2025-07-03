a=1.2
b=111111.111111

print('a:%.2f' %a)
print('b:%.2f' %b)
c=a=b
print('a+b:%.2f' %c)

'''
round()   四舍五入
ceil() 向上取整
floor()  向下取整
'''
import math
n1=10.55455
n1_round=round(n1)
n1_ceil=math.ceil(n1)
n1_floor=math.floor(n1)
print('n1 四舍五入',n1_round)
print('n1 向上取整',n1_ceil)
print('n1 向下取整',n1_floor)