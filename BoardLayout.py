from PyQt6.QtWidgets import QLabel, QGridLayout, QWidget
from PyQt6.QtGui import QPixmap

class BoardLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.boardAsset = QPixmap("board.png")
        self.board = QLabel()
        self.board.setPixmap(self.boardAsset)

        self.layout = QGridLayout()
        self.layout.addWidget(self.board,0,0)
        self.setLayout(self.layout)