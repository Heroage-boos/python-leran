# 使用关键字 def
def f():
    print('hello def')

f()

# 可变参数
def sum_2(a):
    b=2
    print(a+b)

sum_2(3)

# 默认参数
def sum_3(a=1,b=2):
    print(a+b)

sum_3()


# 函数返回
def sum_4(a,b):
    return a+b
print(sum_4(6,6) + 10)

def countA_arr(s):
    count = 0
    for i in s:
        count += i
    print(count)  # 45
countA_arr([1, 2, 3, 4, 5, 6, 7, 8, 9])

#可变参数 字典
def welcome_name(**d):
  for k,v in d.items():
      print(k,v)
d={'name':"小白",'age':18}
welcome_name(**d)

