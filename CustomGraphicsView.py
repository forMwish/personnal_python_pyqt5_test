from PyQt5 import QtWidgets, QtGui


class CustomGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, *__args):
        super(CustomGraphicsView, self).__init__(*__args)
        self.pointMode = 0
        self.rectMode = 0
        self.mousePressPos = [0, 0]
        self.mouseMovePos0 = [0, 0]
        self.mouseMovePos1 = [0, 0]
        self.setMouseTracking(0)
        self.setTransformationAnchor(self.NoAnchor)
        self.keyCtrlOn = 0
        self.mousePressOn = 0

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        print("mousePressEvent in")
        self.mousePressPos = event.globalPos()
        self.mouseMovePos1 = event.globalPos()
        self.mousePressOn = 1

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        print("mouseReleaseEvent in")
        self.mousePressOn = 0

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        print("mouseMoveEvent in")
        if self.mousePressOn:
            self.mouseMovePos0 = self.mouseMovePos1
            self.mouseMovePos1 = event.globalPos()
            temp = self.mouseMovePos1 - self.mouseMovePos0
            self.translate(temp.x(), temp.y())
            self.show()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        print("dragMoveEvent in")
        pass

    def wheelEvent(self, event: QtGui.QWheelEvent):
        print("wheelEvnet in")
        angle = event.angleDelta()

        if self.keyCtrlOn:
            self.setTransformationAnchor(self.AnchorUnderMouse)
            if angle.y() > 0:
                self.scale(1.1, 1.1)
                self.show()
            else:
                self.scale(0.9, 0.9)
                self.show()
            self.setTransformationAnchor(self.NoAnchor)
            #self.show()

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        print("keyPressEvnet in")
        # Ctrl
        if 16777249 == event.key():
            self.keyCtrlOn = 1

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        print("keyReleaseEvnet in")
        # Ctrl
        if 16777249 == event.key():
            self.keyCtrlOn = 0
