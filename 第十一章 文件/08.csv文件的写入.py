import csv

with open("./data.csv",mode="a+",encoding="utf-8") as f:
    cf=csv.writer(f)
    cf.writerow(["tom",'c','100'])
    list=["tom",'python','100'],["tom",'GO','11'],["tom",'JS','68']
    cf.writerows(list)
