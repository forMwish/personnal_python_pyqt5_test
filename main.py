# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import MainWindows as mw
import cv2


class MainWin(mw.Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.scaleX = 1
        self.scaleY = 1

    def loadPic(self, widget, ui):
        file_path = QtWidgets.QFileDialog.getOpenFileName(widget, "选择加载图片", "./resource/picture/")
        print("[test] picture path: ", file_path[0])

        scene = QtWidgets.QGraphicsScene()

        pix = QtGui.QPixmap(file_path[0])
        rect = QtWidgets.QGraphicsRectItem(0, 0, 100, 100)

        scene.addPixmap(pix)
        scene.addItem(rect)

        ui.graphicsView.setScene(scene)
        ui.graphicsView.show()


    def zoomInPic(self, widget, ui):
        self.scaleX = 1.1
        self.scaleY = 1.1
        ui.graphicsView.scale(self.scaleX, self.scaleY)
        ui.graphicsView.show()


    def zoomOutPic(self, widget, ui):
        self.scaleX = 0.9
        self.scaleY = 0.9
        ui.graphicsView.scale(self.scaleX, self.scaleY)
        ui.graphicsView.show()


    def connect(self):
        ui.pushButton_loadPicture.clicked.connect(lambda: self.loadPic(widget, ui))
        ui.zoomIn.triggered.connect(lambda: self.zoomInPic(widget, ui))
        ui.zoomOut.triggered.connect(lambda: self.zoomOutPic(widget, ui))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()

    ui = MainWin()
    ui.setupUi(widget)
    ui.connect()

    widget.show()
    sys.exit(app.exec_())
