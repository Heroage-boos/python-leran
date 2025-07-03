import wx

class HelloFrame(wx.Frame):
    """
    一个显示Hello World的窗口框架
    """

    def __init__(self, *args, **kw):
        # 确保调用父类的__init__方法
        super(HelloFrame, self).__init__(*args, **kw)

        # 在框架中创建一个面板
        pnl = wx.Panel(self)

        # 在面板上放置一些带有较大粗体字体的文本
        st = wx.StaticText(pnl, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # 创建一个布局管理器来管理子控件的布局
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # 创建菜单栏
        self.makeMenuBar()

        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("欢迎使用wxPython!")


    def makeMenuBar(self):
        """
        菜单栏由菜单组成，菜单由菜单项组成。
        此方法构建一组菜单并绑定在选择菜单项时调用的处理程序。
        """

        # 创建包含Hello和Exit项目的文件菜单
        fileMenu = wx.Menu()
        # "\t..."语法定义了一个也会触发相同事件的快捷键
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "在状态栏中为此菜单项显示的帮助字符串")
        fileMenu.AppendSeparator()
        # 当使用标准ID时，我们不需要指定菜单项的标签
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # 现在为关于项目创建帮助菜单
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # 创建菜单栏并向其添加两个菜单。'&'定义下一个字母是菜单项的"助记符"。
        # 在支持它的平台上，这些字母会被下划线标出，可以从键盘触发。
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&文件")
        menuBar.Append(helpMenu, "&帮助")

        # 将菜单栏给予框架
        self.SetMenuBar(menuBar)

        # 最后，将处理函数与每个菜单项的EVT_MENU事件关联。
        # 这意味着当激活该菜单项时，将调用关联的处理函数。
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """关闭框架，终止应用程序。"""
        self.Close(True)


    def OnHello(self, event):
        """向用户问好。"""
        wx.MessageBox("再次来自wxPython的问候")


    def OnAbout(self, event):
        """显示关于对话框"""
        wx.MessageBox("这是一个wxPython Hello World示例",
                      "关于Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # 当此模块被运行（而不是导入）时，创建应用程序、框架，显示它并启动事件循环。
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()