#lambda函数是一种快速定义单行的最小函数，可以用在任何需要使用函数的地方   优点：让代码更简洁，不用费心去想函数的名字

# def f(a,b):
#     return a+b
# a=f(1,2)

fun =lambda a,b:a+b
print(fun(2,3))


#map 作为映射
a=[1,2,3,4,5]
# def map_f(x):
#     return x**2
# map_value=map(map_f,a)
map_value=map(lambda x:x**3,a)
print(list(map_value))  # 将map对象转换为列表以便打印完整结果


#filter 过滤
b=[2,3,4,5,61,1]
def filter_f(x):
    return x>3
filter_value=filter(filter_f,b)
print(list(filter_value))

# result =0
# mul=1
# for i in b[::-1]:
#     result = result + i*mul
#     mul=  mul*10**len(str(i))
