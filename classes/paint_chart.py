# -*- coding: utf-8 -*-
# @Author : pan
# @Description : 废弃方案（雷达图）
# @Date : 2023年7月27日10:46:04

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QMainWindow
)
from PyQt5.QtGui import (
    QPixmap,
    QPaintEvent,
    QImage
)
from PyQt5.QtCore import (
    QThread
)
from PyQt5.Qt import *
import sys
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvas
import matplotlib.pyplot as plt


class drawCloudMain(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.r = 2 * np.random.rand(100)  # 生成100个服从“0~1”均匀分布的随机样本值
        self.angle = 2 * np.pi * np.random.rand(100)  # 生成角度

    def paintEvent(self, painter: QPaintEvent) -> None:
        plt.cla()  # 清屏
        # 获取绘图并绘制
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1], projection="polar")
        ax.set_ylim(0, 10)
        ax.set_yticks(np.arange(0, 10, 2))
        ax.scatter(self.angle, self.r)
        cavans = FigureCanvas(fig)
        self.setCentralWidget(cavans)


class drawCloud(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.r = 2 * np.random.rand(100)  # 生成100个服从“0~1”均匀分布的随机样本值
        self.angle = 2 * np.pi * np.random.rand(100)  # 生成角度

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

    def paintEvent(self, painter: QPaintEvent) -> None:
        ax = self.figure.add_axes([0, 0, 1, 1], projection="polar")
        ax.set_ylim(0, 10)
        ax.set_yticks(np.arange(0, 10, 2))
        ax.scatter(self.angle, self.r)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = drawCloud()
    windows.show()
    sys.exit(app.exec())

