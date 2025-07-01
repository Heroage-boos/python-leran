# 序列：字符串 元组 列表  range
'''
序列的通用操作：
len(item)     计算容器中元素个数
del(item)     删除变量
max(item)     返回容器中最大值
min(item)     返回容器中最小值
切片  item[起始位置:结束位置:步长]
'''

#列表
list1=['1',2,3,{}]

print(list1)

print(type(list1))

for a in range(len(list1)):
    print(list1[a])

#类型转换： 把参数转换为列表
list2=list()
print(list2)
# list3=list('1','3',2,True)
list3=list('3')
print(list3)

#列表常用操作
list4=['1',2,3,4,5,6,7,8,9]
#列表的索引
print(list4[8])
#列表的切片
print(list4[0:8])
#列表的加法和乘法
print(list1+list4)
print(list1*3)

#列表的成员运算
print('0'  in list4)
print('0' not in list4)

list5=[3,4,5,6,7,8,9]
#内置函数
print(len(list4))
print(max(list5))
print(min(list5))

del list3 #删除变量
# print(list3)


#列表的遍历
for index2 in range(len(list4)):
    print(list4[index2],end=" ")

print('\n')
for i,j in enumerate(list4):  #枚举
    print('索引：',i,'值：',j,end=" ")
print('\n')

# 列表的常用方法  变量.方法名()
list6=[1,2,3,1]
list6.append(4) #添加元素
print(list6)
list6.extend([131,132])  #添加列表
print(list6)
list6.insert(1,'hello')
print(list6)
list6.pop(0)  #删除索引下的元素
print(list6)
list6.remove('1')  #根据元素删除  删除第一个元素
print(list6)
  #计算列表中元素个数
print(list6.count('hello'))
list6.clear()  #清空所有元素
print(list6)