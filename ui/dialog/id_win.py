# -*- coding: utf-8 -*-
# @Author : pan
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui.dialog.id_dialog import id_form


class id_Window(QWidget, id_form):
    def __init__(self):
        super(id_Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = id_Window()
    window.show()
    sys.exit(app.exec())
