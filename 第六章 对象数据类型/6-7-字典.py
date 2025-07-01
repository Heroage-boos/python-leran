'''
dictionary(字典)是除列表以外python 之中 最灵活 的数据类型
字典同样可以用来 存储多个数据
通常用于存储 描述一个 物体 的相关信息
和列表的区别 列表 是 有序 的对象集合字典 是 无序 的对象集合
'''

xiaoming ={"name":'小明',"age": 18,"gender": True,"height": 1.75}

#空字典
d1={}

#空字典6
d1 = dict()
d2 = {'name':'麻辣龙虾','taste':'美味'}
d3 = dict(a='l',b=2)
d4 = dict([('a',1),('b',2)])
d5 = dict({'a':1,'b':2})

print('%s======%s=======%s'%(d2,d3,d3))

#新增键值对
d6=dict()
d6['age']=10
#修改键值对
d6['age']=11
#删除
# del d6['age']

#遍历字典
for k,v in d6.items():
    print(k,v)

#获取所有key
for a in d6.keys():
    print(a)

#获取所有value
for k in d6.values():
    print(k)


d7={'a':1,'b':2,'C':3}
d8=d7.pop('b')
d9=d7.popitem()
print(d8,d7,d9)

print(d6.get('age'))

#字典拼接
d10=dict({'a':1,'b':2,'C':3})
d11=dict({'d':5})
print(d10.update(d11),d10.update({'d':5}))