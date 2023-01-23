from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QGridLayout,
    )

from BoardLayout import BoardLayout
from InputLayout import InputLayout

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TicTacToe")

        # Initialize widgets
        self.parentLayout = QVBoxLayout()
        self.boardLayout = QGridLayout()
        self.inputLayout = QGridLayout()

        # Add start-up assets to respective layouts
        self.boardLayout.addWidget(BoardLayout())
        self.inputLayout.addWidget(InputLayout())

        # Add each layout to the parent
        self.parentLayout.addLayout(self.boardLayout)
        self.parentLayout.addLayout(self.inputLayout)
        self.show()