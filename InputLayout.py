from PyQt6.QtWidgets import QPushButton, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget

class InputLayout(QWidget):
    def __init__(self, boardLayout, database):
        super().__init__()

        # Set important variables
        self.currTurn = 1

        self.bl = boardLayout
        self.db = database

        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QGridLayout()
        self.bottomLayout = QVBoxLayout()

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

        self.B00.setText("Top Left")
        self.B01.setText("Top Centre")
        self.B02.setText("Top Right")
        self.B10.setText("Centre Left")
        self.B11.setText("Centre")
        self.B12.setText("Centre Right")
        self.B20.setText("Bottom Left")
        self.B21.setText("Bottom Centre")
        self.B22.setText("Bottom Right")

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

        # Add status label
        self.playerLabel = QLabel()
        self.playerLabel.setText("Still Playing...")
        self.bottomLayout.addWidget(self.playerLabel)

        # Set layout for display
        self.mainLayout.addLayout(self.bottomLayout)
        self.mainLayout.addLayout(self.buttonLayout)
        self.setLayout(self.mainLayout)

    # Run on end-state to require a reset.
    def lockBoard(self, ifWon):
        if ifWon == -1:
            return 0
        self.B00.setEnabled(False)
        self.B01.setEnabled(False)
        self.B02.setEnabled(False)
        self.B10.setEnabled(False)
        self.B11.setEnabled(False)
        self.B12.setEnabled(False)
        self.B20.setEnabled(False)
        self.B21.setEnabled(False)
        self.B22.setEnabled(False)
        if ifWon == -2:
            self.playerLabel.setText("It's a Tie!")
        else:
            self.playerLabel.setText("Player " + str(self.currTurn) + " Won!")

    # Just a method to cut down on lines
    def flipTurn(self, turn):
        if turn == 1:
            return 2
        if turn == 2:
            return 1

    # Define methods for adding stuff to BoardLayout
    def B00Pressed(self):
        self.bl.place00(self.currTurn)
        self.B00.setEnabled(False)
        self.db.updateValue(0, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 0)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)


    def B01Pressed(self):
        self.bl.place01(self.currTurn)
        self.B01.setEnabled(False)
        self.db.updateValue(1, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 1)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B02Pressed(self):
        self.bl.place02(self.currTurn)
        self.B02.setEnabled(False)
        self.db.updateValue(2, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 2)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B10Pressed(self):
        self.bl.place10(self.currTurn)
        self.B10.setEnabled(False)
        self.db.updateValue(10, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 10)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B11Pressed(self):
        self.bl.place11(self.currTurn)
        self.B11.setEnabled(False)
        self.db.updateValue(11, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 11)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B12Pressed(self):
        self.bl.place12(self.currTurn)
        self.B12.setEnabled(False)
        self.db.updateValue(12, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 12)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B20Pressed(self):
        self.bl.place20(self.currTurn)
        self.B20.setEnabled(False)
        self.db.updateValue(20, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 20)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B21Pressed(self):
        self.bl.place21(self.currTurn)
        self.B21.setEnabled(False)
        self.db.updateValue(21, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 21)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)

    def B22Pressed(self):
        self.bl.place22(self.currTurn)
        self.B22.setEnabled(False)
        self.db.updateValue(22, self.currTurn)
        ifWon = self.db.checkWin(self.currTurn, 22)
        self.lockBoard(ifWon)
        self.currTurn = self.flipTurn(self.currTurn)