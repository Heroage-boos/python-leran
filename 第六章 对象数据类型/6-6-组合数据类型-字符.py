'''
字符串就是 一串字符，是编程语言中表示文本的数据类型。
在 Pvthon 中可以使用 一对双引号或者 一对单引号'定义一个字符串。
字符串是以单引号或者双引号括起来的任意文本，也可以是以三引号""或者"""引起来的任意文本。
'''

#单字符串
str1 = 'hello'

#空串
str2 = str()

#双引号字符串
str2 = "hello world"

#三引号字符串 多行字符串
str3='''hello world
hello 2024'''

str4 ="""hello 2024
hello world"""

#运损 加 乘法
print(str1*2)
print(str1+'ssssssssssssssss')

#序列的通用操作
str5='hello world'
print(max(str5),min(str5))  #最小为 空格
print('h' in str5 )
str6='abcd'
str7='abc'
print(str6>str7)

# 类型转换
print(str(12),type(str(12)))# int-->str
print(str([1,234]),type(str([1,2,3,4]))) #ist--
print(str((1,)),type(str(1,)))

#常用方法
#判断字符是否都是大写
print(str6.islower())
#判断字符是否都是小写
print(str7.isupper())


#字符串的统计
s=input("请输入一篇文章:")
a,b,c=0,0,0
for i in s:
    if i.isdigit(): # 数字
        a+=1
    elif i.isalpha(): # 字符
        b+=1
    else : # 其他
        c+=1

print(a,b,c)
