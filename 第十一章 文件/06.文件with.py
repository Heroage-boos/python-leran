
#with 自动关闭，可以省略close()
with open("日记本.txt",mode="r",encoding="utf-8") as f:
    context=f.read()
    print(context)