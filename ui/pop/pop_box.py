# -*- coding: utf-8 -*-
# @Author : pan
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QMessageBox, QLabel, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap, QIcon, QFont

# Single-button dialog box, which disappears automatically after appearing for a specified period of time
class MessageBox(QMessageBox):
    def __init__(self, *args, title='提示', count=1, time=1000, auto=False, **kwargs):
        super(MessageBox, self).__init__(*args, **kwargs)

        self._count = count
        self._time = time
        self._auto = auto  # Whether to close automatically

        assert count > 0  # must be greater than 0
        assert time >= 500  # Must be >=500 milliseconds
        self.setStyleSheet('''
                            QWidget{color:black;
                                    background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(100,107,240), stop:1 rgb(56,187,249));
                                    font: 13pt "Microsoft YaHei UI";
                                    padding-right: 5px;
                                    padding-top: 14px;
                                    font-weight: light;
                                    border-radius:30px;
                                    }
                            QLabel{
                                color:white;
                                background-color: rgba(107, 128, 210, 0);}
                                ''')


        self.setWindowTitle(title)

        # self.setIcon(QMessageBox.Information)
        # 设置自定义图标
        # icon = QIcon("../img/logo.jpg")
        # self.setIconPixmap(icon.pixmap(64, 64))  # 设置图标大小为64x64像素




        # 设置无边框窗口样式
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        # 移除标题栏
        self.setWindowFlag(Qt.WindowTitleHint, False)


        self.setStandardButtons(QMessageBox.StandardButton.Close)  # close button
        self.closeBtn = self.button(QMessageBox.StandardButton.Close)  # get close button
        self.closeBtn.setText('Close')
        self.closeBtn.setVisible(False)


        self._timer = QTimer(self, timeout=self.doCountDown)
        self._timer.start(self._time)



    def doCountDown(self):
        self._count -= 1
        if self._count <= 0:
            self._timer.stop()
            if self._auto:  # auto close
                self.accept()
                self.close()

if __name__ == '__main__':
    MessageBox(QWidget=None, title='提示', text='test...', time=2000, auto=True).exec()

