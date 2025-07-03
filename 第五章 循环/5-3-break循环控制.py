

while True:
    print('test')
    break


#  判断一个数是不是质数
# n=input("请输入判断一个数是不是质数:")
# n=int(n)
# n=10
# while n:
#     if n%2==0:
#         print('%d 是一个质数' %n)
#         break


n2=20
n3=1
while n2>n3:
    n3 += 1
    if n3%2==0:
        print('%d is 是质数' %n3)


for n in range(1,n2+1):
    if n%2==0:
        print('%d is 是质数' %n)
    else:
        print('%d is 不是质数' % n)
