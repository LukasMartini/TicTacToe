from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton
    )

from BoardLayout import BoardLayout
from InputLayout import InputLayout
from WinConDatabase import WinConDBControl as dbc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TicTacToe")
        self.setGeometry(0,0,350,550)

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



""" GLOBALS AND OTHER INITS """
# Initialize main application
main = QApplication([])

# Initialize BoardLayout as a global variable and set the main style sheet
bl = BoardLayout()

# Set up database
db = dbc(':/dbfiles/wc.db')
db.initLookUpTable()
db.initAdjacencyTable()

# Initialize InputLayout as a global variable passing the global BoardLayout
il = InputLayout(bl, db)
window = MainWindow()

# Start MainWindow and run
main.exec()

db.closeConnection()

# Style Sheet is no longer necessary, but kept for reference purposes
"""boardStyleSheet = \"""
QWidget {
    background-image: url(:/assets/board.png);
    background-repeat: no-repeat;
    background-position: center;
}
\"""
bl.setStyleSheet(boardStyleSheet)"""
