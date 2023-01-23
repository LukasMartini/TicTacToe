from PyQt6 import QtCore, QtGui, QtWidgets

class EmptyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.resize(100,100)

        self.setStyleSheet("background:transparent")