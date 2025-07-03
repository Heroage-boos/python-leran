#文件读取 a a+ 文件追加
f=open("./静夜思.txt",mode="a+",encoding="utf-8")

#文件写入
f.writelines("床前明月光\n,疑是地上霜\n,剧透望明月\n,低头思故乡\n,")

#关闭文件
f.close()