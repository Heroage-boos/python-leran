# 简单计算器 支持加减乘除 四则运算

while True:
    try:
        print('请输入一个四则运算，例如 1+2"')
        a = str(input())
        value = 0;
        if '+' in a:
            b = a.split('+')
            value = int(b[0]) + int(b[1])
        elif '-' in a:
            b = a.split('-')
            value = int(b[0]) - int(b[1])
        elif '*' in a:
            b = a.split('*')
            value = int(b[0]) * int(b[1])
        elif '/' in a:
            b = a.split('/')
            value = int(b[0]) / int(b[1])
        elif 'C' == a or 'c' == a:
            print("感谢使用笨计算器")
            continue
        else:
            raise Exception("请使用例如1+2这种格式")
        print("计算结果是: %d" % value)
    except Exception as e:
        print('发生异常:', e)


