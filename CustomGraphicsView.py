from PyQt5 import QtWidgets, QtGui


class CustomGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, *__args):
        super(CustomGraphicsView, self).__init__(*__args)
        self.pointMode = 0
        self.rectMode = 0
        self.mousePressPos = [0, 0]
        self.setTransformationAnchor(self.NoAnchor)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        print("mousePressEvent in")
        self.mousePressPos = event.globalPos()

        #self.setTransformationAnchor(self.AnchorUnderMouse)
        #self.ancho

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        pass
        #self.setTransformationAnchor(self.NoAnchor)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        print("mouseMoveEvent in")
        mouse_pos = event.globalPos()
        print(mouse_pos)
        print(self.mousePressPos)
        temp = mouse_pos - self.mousePressPos
        print(temp)
        
        self.translate(temp.x(), temp.y())
        #self.translate(-1, -1)
        #self.rotate(90)


        self.show()

    def dragMoveEvent(self, event: QtGui.QDragMoveEvent):
        print("dragMoveEvent in")
        pass
