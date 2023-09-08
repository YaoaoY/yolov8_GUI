# -*- coding: utf-8 -*-
# @Author : pan
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.dialog.rtsp_dialog import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
