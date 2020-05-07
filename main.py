# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MainWindows as mw


class MainWin(mw.Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.scene = QtWidgets.QGraphicsScene()
        self.scaleX = 1
        self.scaleY = 1

    def loadPic(self, widget):
        print("[test] class:MainWin -> fun:loadPic -> In ")
        file_path = QtWidgets.QFileDialog.getOpenFileName(widget, "选择加载图片", "./resource/picture/", "图片 (*.jpg)")

        print("[test] picture path: ", file_path[0])

        pix = QtGui.QPixmap(file_path[0])
        # rect = QtWidgets.QGraphicsRectItem(0, 0, 100, 100)

        self.scene.addPixmap(pix)
        # self.scene.addItem(rect)

        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

    def connect(self, widget):
        print("[test] class:MainWin -> fun:connect -> In ")
        self.pushButton_loadPicture.clicked.connect(lambda: self.loadPic(widget))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget1 = QtWidgets.QMainWindow()

    ui = MainWin()
    ui.setupUi(widget1)
    ui.connect(widget1)

    widget1.show()
    sys.exit(app.exec_())
