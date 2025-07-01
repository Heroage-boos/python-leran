'''
集合
不允许有重复元素，如果有会自动合并
是一种无序且无重复的数据结构
与dict类似
'''
# 直接使用大括号创建集合
set1={1,2,3,4,5,6}

# 使用 set() 函数从列表创建集合
set2=set([1,2,3,4,5,6])

print(set1,set2)

# 元组转set
print(set((1,2,3)))
#字典转set
print(set({'a':'1','b':2}))

#集合常用方法
print(len(set1))
print(min(set1))
print(max(set1))

s6=set1.remove(1)
print(s6)
s3=set1.update({11,23})
print(s3)
s4=set1.add(1)
print(s4)

#交集 并集
s7={5,6,7,8,9}
print(s7)
print(set1 & s7)
print(set1 | s7)

#列表去重
score=[80,81,82,82,834,80]
s8=set(score)
d={}
print(s8)
for i in s8:
    t=score.count(i)
    d[i]=t

print(d)
for k,v in d.items():
    print('得分为%d有%d个人' % (k,v))
