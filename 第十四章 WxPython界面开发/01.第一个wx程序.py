'''
 wxPython，它是 Python 语言的跨平台 GUI 工具包。使用 wxPython，软件开发人员可以为他们的 Python 应用程序创建真正的原生用户界面，这些应用程序几乎无需修改即可在 Windows、Mac、Linux 或其他类 Unix 系统上运行。
'''

import wx

def onClick(event):
    print("按钮被点击了！")  # 打印到控制台
    # 事件处理函数
    wx.MessageBox("按钮被点击了！", "提示", wx.OK | wx.ICON_INFORMATION)

# 创建应用程序对象
app = wx.App()

# 创建窗口
frm = wx.Frame(None, title="学习系统", size=(800, 600),pos=(200,200))

# 展示
frm.Show()

#创建面板
pl=wx.Panel(frm,size=(400,300),pos=(100,100))

#创建静态文本
staticText=wx.StaticText(pl, label="欢迎使用wxPython学习系统", pos=(50, 50))
#创建按钮
btn=wx.Button(pl, label="点击我", pos=(50, 100))
#给按钮绑定事件
frm.Bind(wx.EVT_BUTTON, onClick,btn)

# 进入主循环，让程序一直显示
app.MainLoop()