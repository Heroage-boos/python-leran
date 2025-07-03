import turtle
import time

pen =turtle.Turtle()
# 设置速度
pen.speed(0)
# 画一个正方形
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
for index in range(8):
    pen.forward(100)
    pen.right(80)

# 写字
pen.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

input()