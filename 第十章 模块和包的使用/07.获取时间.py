import  time

t =time.time() #时间戳 1970年
print(t)

t=time.localtime()  #结构化的时间
print(t)
print(t.tm_year,t.tm_mon,t.tm_mday)

#获取当前的时间
s=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(s)

from my_package import my_tools
s=my_tools.get_current_time()
print(s)
