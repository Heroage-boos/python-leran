# 题目要求：输入2024-02-25，输出这一天是这年的第多少天
# 例如：2024-1-3 第三天   2023-12-21

date = input("请输入日期：").split('-')
year=int(date[0])
month=int(date[1])
day=int(date[2])

#存储每个月有多少天
days=[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #合计365天

how_day=0
print(sum(days))

#判断是否是闰年
if (year%4==0 and year%100!=0) or (year%400==0):
    days[2]+=1
    print('%d是闰年' %year)

for i in range(month):
    if(i<month):
        how_day+=days[i]
how_day+=day
print("是%d年的第%d天" %(year,how_day))
