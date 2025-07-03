'''
函数名               函数值
int(x，[基数])       将数字或字符串转换为整数，如果x为浮点数，则自动截断小数部分
float(x)            将x转换成浮点型
bool(x)             转换成bool类型 的True或 False
str(x)              将x转换成字符串，适合人阅读
'''

number_1=111
float_1=222.222233
bool_1=''
bool_2='NoNe'
bool_3=' '
string_1='234324'

print(str(number_1))
print(int(string_1),float(string_1))
print(bool(bool_1),bool(bool_2),bool(bool_3))
print(float(float_1),float(number_1))

#  进制的转换
print('进制的转换==========')
s='10'
print(int(s))
print(int(s,2))  #二进制 逢二进一
s2='1a'
print(int(s2,16))