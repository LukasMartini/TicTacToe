from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QGridLayout,
    )

from BoardLayout import BoardLayout
from InputLayout import InputLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TicTacToe")
        self.setGeometry(0,0,350,700)

        # Initialize widgets
        self.parentLayout = QVBoxLayout()
        self.boardLayout = QGridLayout()
        self.inputLayout = QGridLayout()

        #Add start-up assets to respective layouts
        self.boardLayout.addWidget(bl)
        self.inputLayout.addWidget(il)

        # Add each layout to the parent
        self.parentLayout.addLayout(self.boardLayout)
        self.parentLayout.addLayout(self.inputLayout)

        # Initialize everything else and show.
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.parentLayout)
        self.setCentralWidget(self.mainWidget)
        self.show()


main = QApplication([])

bl = BoardLayout()
boardStyleSheet = """
QWidget {
    background-image: url(:/assets/board.png);
    background-repeat: no-repeat;
    background-position: center;
}
"""
bl.setStyleSheet(boardStyleSheet)

il = InputLayout(bl)

window = MainWindow()
main.exec()