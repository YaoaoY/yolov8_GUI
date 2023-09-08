# -*- coding: utf-8 -*-
# @Author : pan
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PySide6.QtGui import QPixmap, QPainter, QColor, QFontMetrics
from PySide6.QtWidgets import QApplication, QWidget, QLabel

class Toast(QWidget):
    def __init__(
        self,
        text: str,
        duration: int = 3000,
        parent: QWidget = None,
    ):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.duration = duration

        label = QLabel(self)
        label.setText(text)
        label.setStyleSheet("""
            background-color: rgba(60, 179, 113, 0.8);
            color: white;
            font-size: 16px;
            padding: 12px;
            border-radius: 4px;
        """)
        label.setAlignment(Qt.AlignCenter)

        fm = QFontMetrics(label.font())
        width = fm.boundingRect(text).width() + 80

        # 高度与宽度
        label.setFixedWidth(width)
        label.setFixedHeight(40)

        self.setGeometry(*self.calculatePosition(label.sizeHint()))

        self.fadeIn()

        self.animationTimer = QTimer()
        self.animationTimer.setSingleShot(True)
        self.animationTimer.timeout.connect(self.fadeOut)
        self.animationTimer.start(self.duration)



    def fadeIn(self):
        # 创建并设置淡入动画
        fadeInAnimation = QPropertyAnimation(self, b"windowOpacity", self)
        fadeInAnimation.setStartValue(0)
        fadeInAnimation.setEndValue(1)
        fadeInAnimation.setDuration(500)
        fadeInAnimation.finished.connect(lambda: print('加载成功'))
        # 启动淡入动画
        fadeInAnimation.start()

    def calculatePosition(self, sizeHint):
        desktopRect = QApplication.primaryScreen().availableGeometry()
        x = (desktopRect.width() - sizeHint.width()) // 2
        y = desktopRect.height() - sizeHint.height() - 50
        return x, y, sizeHint.width(), sizeHint.height()



    # 淡出动画
    def fadeOut(self):
        # 停止计时器
        self.animationTimer.stop()
        # 断开计时器的超时信号与当前方法的连接
        self.animationTimer.timeout.disconnect(self.fadeOut)

        # 创建并设置并行动画组
        parallelAnimation = QParallelAnimationGroup()

        # 创建并设置不透明度动画
        opacityAnimation = QPropertyAnimation(self, b"windowOpacity")
        opacityAnimation.setStartValue(1.0)
        opacityAnimation.setEndValue(0.0)
        opacityAnimation.setDuration(500)

        # 创建并设置位置动画
        yAnimation = QPropertyAnimation(self, b"geometry")
        targetY = self.y() - 50
        yAnimation.setStartValue(self.geometry())
        yAnimation.setEndValue(QApplication.primaryScreen().availableGeometry().translated(0, targetY))
        yAnimation.setDuration(500)
        yAnimation.setEasingCurve(QEasingCurve.OutCubic)

        # 将动画添加到并行动画组中
        parallelAnimation.addAnimation(opacityAnimation)
        parallelAnimation.addAnimation(yAnimation)



        # 连接并行动画组的完成信号与关闭窗口的槽
        parallelAnimation.finished.connect(self.close)

        parallelAnimation.start()  # 启动动画组
        print(111)




    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 0))

    def mousePressEvent(self, event):
        pass


if __name__ == "__main__":
    app = QApplication([])

    toast = Toast("操作成功")
    toast.show()

    app.exec()
