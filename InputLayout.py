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
        self.B00 = QPushButton()
        self.B01 = QPushButton()
        self.B02 = QPushButton()
        self.B10 = QPushButton()
        self.B11 = QPushButton()
        self.B12 = QPushButton()
        self.B20 = QPushButton()
        self.B21 = QPushButton()
        self.B22 = QPushButton()

        self.buttonLayout.addWidget(self.B00, 0, 0)
        self.buttonLayout.addWidget(self.B01, 0, 1)
        self.buttonLayout.addWidget(self.B02, 0, 2)
        self.buttonLayout.addWidget(self.B10, 1, 0)
        self.buttonLayout.addWidget(self.B11, 1, 1)
        self.buttonLayout.addWidget(self.B12, 1, 2)
        self.buttonLayout.addWidget(self.B20, 2, 0)
        self.buttonLayout.addWidget(self.B21, 2, 1)
        self.buttonLayout.addWidget(self.B22, 2, 2)

        # Connect buttons to events
        self.B00.clicked.connect(self.B00Pressed)
        self.B01.clicked.connect(self.B01Pressed)
        self.B02.clicked.connect(self.B02Pressed)
        self.B10.clicked.connect(self.B10Pressed)
        self.B11.clicked.connect(self.B11Pressed)
        self.B12.clicked.connect(self.B12Pressed)
        self.B20.clicked.connect(self.B20Pressed)
        self.B21.clicked.connect(self.B21Pressed)
        self.B22.clicked.connect(self.B22Pressed)

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
    def B00Pressed(self):
        self.bl.place00(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B00.setEnabled(False)

    def B01Pressed(self):
        self.bl.place01(self.currTurn)
        if self.currTurn == 1:
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B01.setEnabled(False)

    def B02Pressed(self):
        self.bl.place02(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B02.setEnabled(False)

    def B10Pressed(self):
        self.bl.place10(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B10.setEnabled(False)

    def B11Pressed(self):
        self.bl.place11(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B11.setEnabled(False)

    def B12Pressed(self):
        self.bl.place12(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B12.setEnabled(False)

    def B20Pressed(self):
        self.bl.place20(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B20.setEnabled(False)

    def B21Pressed(self):
        self.bl.place21(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B21.setEnabled(False)

    def B22Pressed(self):
        self.bl.place22(self.currTurn)
        if self.currTurn == 1: # It's too late at night and I don't know why pattern matching isn't working
            self.currTurn = 2
        elif self.currTurn == 2:
            self.currTurn = 1
        elif self.currTurn == 3:
            pass
        self.B22.setEnabled(False)