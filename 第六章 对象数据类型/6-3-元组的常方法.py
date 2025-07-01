
tuple1=[1,2,3,4,5,6,3]

#索引
print(tuple1[-1])

#切面
print(tuple1[0:3])
print(tuple1[::-1])  #翻转


#len  max  min
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))

#count
print(tuple1.count(3))

# del
del tuple1

tuple2=[1,2,3,4,5,6,3]
print(tuple2.index(3))
