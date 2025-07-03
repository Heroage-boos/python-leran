# 打开文件 W w+覆盖以前内容
f=open("./静夜思.txt",mode='w+',encoding="utf-8")

#写入文件内容
f.write("作者李白111\n床前明月光") #不会自动换行  多个一样
f.writelines("作者李白111\n作者李白111\n作者李白111\n")#也不会自动换行
ontext=['作者李白222','作者李白1222','作者李白2222']  #也不会自动换行
for line in ontext:
    f.write(line+'\n')

#关闭文件
f.close()