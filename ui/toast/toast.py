# -*- coding: utf-8 -*-
# @Author : pan
import sys
import queue
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton, QHBoxLayout, QVBoxLayout,
)
from PySide6.QtCore import (
    QPoint,
    Qt, 
    QTimer,
    QPropertyAnimation,
    QEasingCurve,
)
from PySide6.QtGui import (
    QPixmap,
    QFont,
    QPainter,
    QPaintEvent,
    QColor,
    QFontMetrics, )

try:
    from ui.toast import rc_icons
except ImportError:
    import rc_icons





class DialogOver(QWidget):
    
    _instanceWidget: queue.Queue = queue.Queue(7)  # 存储实例化对象序号的队列，供paintEvent调用时判断位置
    _instanceDel: queue.Queue = queue.Queue(7)  # 存储实例化对象序号的队列, 供__del__调用时判断位置
    _instanceQueue: queue.Queue = queue.Queue(7)   #存储实例索引的队列，防止被回收
    _count: list = [0, 0, 0, 0, 0, 0, 0]  # 记录每个位置是否有对象

    def __new__(cls, *args, **kwargs) -> None:
        try:
            _index = cls._count.index(0)  # 寻找可用位置，即_count中为0的索引
        except ValueError:
            return
        cls._count[_index] = 1  # 将对应位置置为1，表示该位置已被使用
        cls._instanceWidget.put(_index)  # 将可用位置的索引加入_instanceWidget队列
        cls._instanceDel.put(_index)  # 将可用位置的索引加入_instanceDel队列
        instance = super(DialogOver, cls).__new__(cls)
        cls._instanceQueue.put(instance)
        return instance

    def __del__(self) -> None:
        DialogOver._count[DialogOver._instanceDel.get()] = 0  # 将被删除对象的位置在_count中置为0，标记为空闲位置
        
    def __init__(self,
                 parent: QWidget,
                 text: str,
                 title: str = "",
                 flags: str = "success" or "warning" or "danger" or "info",
                 _showTime: int = 3000,
                 _dieTime: int = 500,
                 ):
        super().__init__()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint|Qt.WindowTransparentForInput)
        # self.setAttribute(Qt.WA_DeleteOnClose)  # pyside6 此函数没有用,因此要自己对自己进行强索引
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 设置窗口背景透明

        # 参数设置
        self.title = title
        self.text = text
        self.flags = flags

        # 颜色属性
        self.QBackgroundColor = QColor(240, 249, 235)
        self.QBorder = QColor(227, 249, 214)
        self.QTextColor = QColor(0, 191, 0)


        # 父窗口
        self.parent = parent
        self.w = 200 # 弹窗宽度

        self.resize(500, 40)
        self.moveSizeH = 6  # 每个框的高度偏移量
        self.moveSize = 6  # 框的初始高度偏移量
        self._dieTime = _dieTime

        self.moveDialog()  # 移动动画

        self.showTime = QTimer(self)  # 定时器，控制显示时间
        self.showTime.setSingleShot(True)  # 只触发一次
        self.showTime.start(_showTime)
        self.showTime.timeout.connect(self.disDialog)  # 显示时间到达后调用disDialog方法

        self.dieTime = QTimer(self)  # 定时器，控制关闭时间
        self.dieTime.setSingleShot(True)  # 只触发一次
        self.dieTime.start(_showTime + _dieTime + 50)
        self.dieTime.timeout.connect(self.closeDialog)  # 关闭时间到达后调用closeDialog方法
        self.show()

    def paintStatus(self, flags):
        if flags == "success":
            self.QBackgroundColor = QColor(240, 249, 235)
            self.QBorder = QColor(227, 249, 214)
            self.QTextColor = QColor(0, 191, 0)

        elif flags == "warning":
            self.QBackgroundColor = QColor(253,246,236)
            self.QBorder = QColor(241, 228, 208)
            self.QTextColor = QColor(241, 170, 62)

        elif flags == "danger":
            self.QBackgroundColor = QColor(254,240,240)
            self.QBorder = QColor(239, 220, 219)
            self.QTextColor = QColor(245,108,108)

        elif flags == "info":
            self.QBackgroundColor = QColor(244,244,245)
            self.QBorder = QColor(244,244,245)
            self.QTextColor = QColor(142,142,142)

            # 渐变方案舍弃
            # self.gradient = QLinearGradient(0, 0, self.width(), 0)
            # self.gradient.setColorAt(0, QColor(255,66,100))
            # self.gradient.setColorAt(1, QColor(255,75,45))

    def paintEvent(self, event: QPaintEvent) -> None:
        # 绘制事件
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)

        # 设置绘画颜色
        self.paintStatus(self.flags)

        # 自定义的绘画方法
        if self.flags in ["success", "warning", "danger", "info"]:
            self.drawDialog(event, painter, self.flags)
        else:
            self.drawDialog(event, painter, "success")

    def drawDialog(self, event: QPaintEvent, painter: QPainter, flags: str) -> None:

        # 设置字体大小
        titleFont = QFont('Microsoft YaHei', 8, QFont.Bold)
        textFont = QFont('Microsoft YaHei', 8)

        # 计算长度
        titleSizeMoveH = (self.height() - QFontMetrics(titleFont).height()) // 2  # 计算文本在垂直方向上的位置
        titleWidth = QFontMetrics(titleFont).horizontalAdvance(self.title)+5  # 计算标题的宽度
        textWidth = QFontMetrics(textFont).horizontalAdvance(self.text)# 计算标题的宽度

        # 计算整个矩形长度
        self.w = 40+ titleWidth + textWidth + 20

        # 绘制背景
        a = event.rect()
        a.setWidth(self.w) # 绘制长度
        painter.setPen(self.QBorder) # 背景边框颜色
        painter.setBrush(self.QBackgroundColor) # 背景颜色设置
        painter.drawRoundedRect(a, 3.0, 3.0)

        # 画图标@@@@
        # 创建一个 QPixmap 对象，用于加载指定路径的图像文件，并将其大小缩放为 20x20 像素。
        # Qt.IgnoreAspectRatio 表示忽略图像的宽高比，Qt.SmoothTransformation 表示对图像进行平滑处理。
        img = QPixmap(f':/img/{flags}.png').scaled(50, 50, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        # 在画布上绘制图像，起始点坐标为 (10, 10)，宽度和高度均为 20 像素，使用前面加载的 img 图像对象。
        painter.drawPixmap(10, 10, 20, 20, img)


        # 画笔颜色
        painter.setPen(self.QTextColor)
        # 画 title
        painter.setFont(titleFont)
        painter.drawText(
            40,
            titleSizeMoveH,
            titleWidth,
            QFontMetrics(titleFont).height(),
            Qt.AlignLeft,
            self.title
        )


        # 画 text
        painter.setFont(textFont)
        painter.drawText(
            40 + titleWidth + 5,
            titleSizeMoveH,
            textWidth,
            QFontMetrics(textFont).height(),
            Qt.AlignLeft,
            self.text
        )



    def moveDialog(self) -> None:

        # w, h = desktop.width() // 2, self.moveSize + (self.height() + self.moveSizeH) * (DialogOver._instanceWidget.get())
        # self.moveSize + (self.height() + self.moveSizeH) * (DialogOver._instanceWidget.get())
        # 居中
        x = self.parent.x() + (self.parent.width() / 2) - (self.w/2)
        y = self.parent.y() + 30 + (DialogOver._instanceWidget.get() * 50)

        # print(f"x:{x}")

        animation = QPropertyAnimation(self, b"pos", self)
        animation.setStartValue(QPoint(x + 100, y))
        animation.setEndValue(QPoint(x, y))

        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutCubic)
        animation.start()

    def disDialog(self) -> None:
        animation = QPropertyAnimation(self, b"windowOpacity", self)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.setDuration(self._dieTime)
        animation.setEasingCurve(QEasingCurve.OutCubic)
        animation.start()
        
    def closeDialog(self) -> None:
        DialogOver._instanceQueue.get()  # 取出强索引, 主动激活python回收释放实例对象，调用__del__函数
        self.close()

    # 计算文本长度
    def prepare(self, text: str, font: QFont) -> int:
        text = text.replace("\n", "")
        font = QFontMetrics(font)
        textLen = 0
        for x in text:
            textLen += font.horizontalAdvance(x)  # 计算文本的宽度
        return textLen
    


class Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Window")
        self.resize(450, 650)

        layout = QVBoxLayout(self)
        buttonLayout = QHBoxLayout()

        button1 = QPushButton("success", self)
        button2 = QPushButton("warning", self)
        button3 = QPushButton("danger", self)
        button4 = QPushButton("info", self)

        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        buttonLayout.addWidget(button4)

        layout.addStretch(1)
        layout.addLayout(buttonLayout)

        button1.clicked.connect(lambda x: self.dialog(title="success标题",text="success的内容",flags="success"))
        button2.clicked.connect(lambda x: self.dialog(title="warning标题", text="warning内容", flags="warning"))
        button3.clicked.connect(lambda x: self.dialog(title="danger标题", text="danger内容", flags="danger"))
        button4.clicked.connect(lambda x: self.dialog(title="info标题", text="info内容", flags="info"))

    def dialog(self,title,text,flags) -> None:
        DialogOver(parent=self, title=title, text=text, flags=flags)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec())
