# 方式一:全模块导入
import my_modules
# 函数可以调用
print(my_modules.add(3, 4))
print(my_modules.total([10, 20, 30]))

#变量可以使用
print(my_modules.author)

# 方式二:单模块导入  不用加模块名
from my_modules import add
print(add(3,4))

# 方式3: 所有导入  不用加模块名
from my_modules import *
print(add(3,4))

# 方式4： 导入内容重命名   不用加模块名
from my_modules import add as insert
print(insert(3,4))



