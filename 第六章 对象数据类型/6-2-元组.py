# Tuple 元组，与列表类似 ，不同之处在于元组数据内容不能修改

tuple1 = (1,2,3,4,5)
print(type(tuple1))
print(tuple1)

#只有一个元素
list1 =(1,)
print(list1)

#tuple 类型转换
tuple_f=tuple()
print(tuple_f)

str="hello world"
tuple_f2=tuple(str)
print(tuple_f2)
print(tuple([1,2,3,4,5,6]))
