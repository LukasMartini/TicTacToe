from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtGui import QPixmap
import assets # NOTE: don't forget that :/<prefix>/<filename in qrc>
              # To compile the qrc, use pyside6-rcc <qrc filename>.qrc -o <desired python filename>.py
              # After that, don't forget to change the import: import PySide6 -> import PyQt6

class BoardLayout(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Add in image assets
        try:
            self.boardAsset = QPixmap(':/assets/centre.png')
        except:
            print("Could not find files, please ensure that you have the assets directory included in the executable.")
            exit(0)

        # Creates labels to add pixmaps to
        self.TLeft = QLabel()
        self.TCentre = QLabel()
        self.TRight = QLabel()
        self.MLeft = QLabel()
        self.MCentre = QLabel()
        self.MRight = QLabel()
        self.BLeft = QLabel()
        self.BCentre = QLabel()
        self.BRight = QLabel()
        
        # Adds the pixmaps
        self.TLeft.setPixmap(self.boardAsset)
        self.TCentre.setPixmap(self.boardAsset)
        self.TRight.setPixmap(self.boardAsset)
        self.MLeft.setPixmap(self.boardAsset)
        self.MCentre.setPixmap(self.boardAsset)
        self.MRight.setPixmap(self.boardAsset)
        self.BLeft.setPixmap(self.boardAsset)
        self.BCentre.setPixmap(self.boardAsset)
        self.BRight.setPixmap(self.boardAsset)

        # Try to load additional assets
        try:
            self.xAsset = QPixmap(':/assets/wX.png')
            self.oAsset = QPixmap(':/assets/wO.png')
        except:
            print("Could not find files, please ensure that you have the assets directory included in the executable.")
            exit(0)

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
        
    # Functions called from InputLayout that replace the images as required
    def place00(self, currTurn):
        self.TLeft.setHidden(True) # Hides the board section, as the new asset has the necessary parts to avoid change in the board's appearance
        if currTurn == 1: # If it's player 1's turn, use the x asset
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 0, 0)
        elif currTurn == 2 or currTurn == 3: # Otherwise, use the y asset. Note that player 3 is intended to be for a bot player, but that hasn't been implemented yet.
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 0, 0)

    def place01(self, currTurn):
        self.TCentre.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 0, 1)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 0, 1)

    def place02(self, currTurn):
        self.TRight.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 0, 2)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 0, 2)

    def place10(self, currTurn):
        self.MLeft.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 1, 0)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 1, 0)

    def place11(self, currTurn):
        self.MCentre.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 1, 1)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 1, 1)

    def place12(self, currTurn):
        self.MRight.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 1, 2)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 1, 2)

    def place20(self, currTurn):
        self.BLeft.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 2, 0)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 2, 0)

    def place21(self, currTurn):
        self.BCentre.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 2, 1)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 2, 1)

    def place22(self, currTurn):
        self.BRight.setHidden(True)
        if currTurn == 1:
            x = QLabel()
            x.setPixmap(self.xAsset)
            self.layout.addWidget(x, 2, 2)
        elif currTurn == 2 or currTurn == 3:
            o = QLabel()
            o.setPixmap(self.oAsset)
            self.layout.addWidget(o, 2, 2)
