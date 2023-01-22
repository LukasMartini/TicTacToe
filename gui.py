from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QGridLayout,
    )

from BoardLayout import BoardLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TicTacToe")

        # Initialize widgets
        self.parentLayout = QVBoxLayout()
        self.boardLayout = QGridLayout()
        self.inputLayout = QGridLayout()

        #Add start-up assets to respective layouts
        self.boardLayout.addWidget(BoardLayout())

        # Add each layout to the parent
        self.parentLayout.addLayout(self.boardLayout)
        self.parentLayout.addLayout(self.inputLayout)

        # Initialize everything else and show.
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.parentLayout)
        self.setCentralWidget(self.mainWidget)
        self.show()


def guiLauncher():
    main = QApplication([])
    window = MainWindow()

    main.exec()


guiLauncher()