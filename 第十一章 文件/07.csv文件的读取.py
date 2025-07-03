import csv
with open('./data.csv',mode="r",encoding="utf-8") as f:
    # context=f.readlines()
    cf =csv.reader(f)
    head=next(cf)  #获取表头
    # print(head)

    scores=[]
    # 处理信息
    for row in cf:
        scores.append(int(row[2]))
        print(row)

    print("总分%d,平均分%d" %(sum(scores),sum(scores)/len(scores)))


