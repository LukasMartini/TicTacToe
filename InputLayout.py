from PyQt6.QtWidgets import QPushButton, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget

from BoardLayout import BoardLayout


class InputLayout(QWidget):
    def __init__(self, boardLayout):
        super().__init__()

        # Set important variables
        self.currTurn = 1

        self.bl = boardLayout

        self.inputLayout = QVBoxLayout()
        self.labelLayout = QHBoxLayout()
        self.buttonLayout = QGridLayout()

        # Add all buttons to layout
        self.B1 = QPushButton()
        self.B2 = QPushButton()
        self.B3 = QPushButton()
        self.B4 = QPushButton()
        self.B5 = QPushButton()
        self.B6 = QPushButton()
        self.B7 = QPushButton()
        self.B8 = QPushButton()
        self.B9 = QPushButton()

        self.buttonLayout.addWidget(self.B1, 0, 0)
        self.buttonLayout.addWidget(self.B2, 0, 1)
        self.buttonLayout.addWidget(self.B3, 0, 2)
        self.buttonLayout.addWidget(self.B4, 1, 0)
        self.buttonLayout.addWidget(self.B5, 1, 1)
        self.buttonLayout.addWidget(self.B6, 1, 2)
        self.buttonLayout.addWidget(self.B7, 2, 0)
        self.buttonLayout.addWidget(self.B8, 2, 1)
        self.buttonLayout.addWidget(self.B9, 2, 2)

        # Connect buttons to events
        self.B1.clicked.connect(self.B1Pressed)
        self.B2.clicked.connect(self.B2Pressed)

        # Add label to layout
        self.playerLabel = QLabel()
        self.setBotMode = QPushButton()
        self.labelLayout.addWidget(self.playerLabel)
        self.labelLayout.addWidget(self.setBotMode)

        # Set layout for display
        self.inputLayout.addLayout(self.labelLayout)
        self.inputLayout.addLayout(self.buttonLayout)
        self.setLayout(self.inputLayout)

    # Define methods for adding stuff to BoardLayout
    def B1Pressed(self):
        self.bl.place00(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B1.setEnabled(False)

    def B2Pressed(self):
        self.bl.place01(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B2.setEnabled(False)