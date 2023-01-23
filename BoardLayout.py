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

        # Add in image assets
        self.boardAsset = QPixmap(':/assets/centre.png')
        self.TLeft = QLabel()
        self.TCentre = QLabel()
        self.TRight = QLabel()
        self.MLeft = QLabel()
        self.MCentre = QLabel()
        self.MRight = QLabel()
        self.BLeft = QLabel()
        self.BCentre = QLabel()
        self.BRight = QLabel()

        self.TLeft.setPixmap(self.boardAsset)
        self.TCentre.setPixmap(self.boardAsset)
        self.TRight.setPixmap(self.boardAsset)
        self.MLeft.setPixmap(self.boardAsset)
        self.MCentre.setPixmap(self.boardAsset)
        self.MRight.setPixmap(self.boardAsset)
        self.BLeft.setPixmap(self.boardAsset)
        self.BCentre.setPixmap(self.boardAsset)
        self.BRight.setPixmap(self.boardAsset)

        self.xAsset = QPixmap(':/assets/wX.png')
        self.oAsset = QPixmap(':/assets/wO.png')

        # Set up grid layout for display
        self.layout = QGridLayout()
        self.layout.addWidget(self.TLeft, 0, 0)
        self.layout.addWidget(self.TCentre, 0, 1)
        self.layout.addWidget(self.TRight, 0, 2)
        self.layout.addWidget(self.MLeft, 1, 0)
        self.layout.addWidget(self.MCentre, 1, 1)
        self.layout.addWidget(self.MRight, 1, 2)
        self.layout.addWidget(self.BLeft, 2, 0)
        self.layout.addWidget(self.BCentre, 2, 1)
        self.layout.addWidget(self.BRight, 2, 2)
        self.setLayout(self.layout)

    def place00(self, currTurn):
        self.TLeft.setHidden(True)
        if currTurn == 1:
            x00 = QLabel()
            x00.setPixmap(self.xAsset)
            self.layout.addWidget(x00, 0, 0)
        elif currTurn == 2:
            o00 = QLabel()
            o00.setPixmap(self.oAsset)
            self.layout.addWidget(o00, 0, 0)

    def place01(self, currTurn):
        self.TCentre.setHidden(True)
        if currTurn == 1:
            x01 = QLabel()
            x01.setPixmap(self.xAsset)
            self.layout.addWidget(x01, 0, 1)
        elif currTurn == 2:
            o01 = QLabel()
            o01.setPixmap(self.oAsset)
            self.layout.addWidget(o01, 0, 1)
