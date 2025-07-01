'''
range
-系统提供的内置函数，生成一个等差序列[start,end]  range(start,end,[step=1])
-序列不支持可变序列，不支持元素修改，不支持+和*操作
-range一般用于for-in 循环遍历
'''

print(list(range(10)))
print(list(range(10,20)))
print(list(range(10,20,2)))

for a in range(10):
    print(a)