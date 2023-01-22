from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget
from PyQt6.QtGui import QPixmap
import pkg_resources

class BoardLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.boardAsset = QPixmap(':/assets/board.png') #MAY NEED TO MAKE THIS RELATIVE
        self.board = QLabel()
        self.board.setPixmap(self.boardAsset)

        self.layout = QGridLayout()
        self.layout.addWidget(self.board,0,0)
        self.setLayout(self.layout)