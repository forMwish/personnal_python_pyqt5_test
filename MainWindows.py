# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import CustomGraphicsView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 939)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 100))
        self.centralwidget.setMaximumSize(QtCore.QSize(3000, 3000))
        self.centralwidget.setBaseSize(QtCore.QSize(500, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_loadPicture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadPicture.setObjectName("pushButton_loadPicture")
        self.verticalLayout.addWidget(self.pushButton_loadPicture)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.pushButton_close)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        #self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView = CustomGraphicsView.CustomGraphicsView(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setBaseSize(QtCore.QSize(2000, 2000))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.zoomIn = QtWidgets.QAction(MainWindow)
        self.zoomIn.setObjectName("zoomIn")
        self.zoomOut = QtWidgets.QAction(MainWindow)
        self.zoomOut.setObjectName("zoomOut")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.toolBar.addAction(self.zoomIn)
        self.toolBar.addAction(self.zoomOut)
        self.toolBar.addAction(self.save)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_loadPicture, self.graphicsView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_loadPicture.setText(_translate("MainWindow", "加载图片"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.zoomIn.setText(_translate("MainWindow", "放大图片"))
        self.zoomIn.setShortcut(_translate("MainWindow", "Ctrl++"))
        self.zoomOut.setText(_translate("MainWindow", "缩小图片"))
        self.zoomOut.setShortcut(_translate("MainWindow", "Ctrl+-"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.save.setShortcut(_translate("MainWindow", "Ctrl+S"))

