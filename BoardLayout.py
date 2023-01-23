from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtGui import QPixmap
from EmptyWidget import EmptyWidget
import assets # NOTE: don't forget that :/<prefix>/<filename in qrc>
              # To compile the qrc, use pyside6-rcc <qrc filename>.qrc -o <desired python filename>.py
              # After that, don't forget to change the import: import PySide6 -> import PyQt6

class BoardLayout(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.boardAsset = QPixmap(':/assets/board.png')
        self.board = QLabel()
        self.board.setPixmap(self.boardAsset)

        self.xAsset = QPixmap(':/assets/X.png')
        self.x = QLabel()
        self.x.setPixmap(self.xAsset)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

    def place00(self):
        self.layout.addWidget(self.x, 0, 0)