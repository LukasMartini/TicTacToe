from PyQt6.QtWidgets import QPushButton, QLabel, QGridLayout, QWidget

class InputLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()

        self.B1 = QPushButton()
        self.B2 = QPushButton()
        self.B3 = QPushButton()
        self.B4 = QPushButton()
        self.B5 = QPushButton()
        self.B6 = QPushButton()
        self.B7 = QPushButton()
        self.B8 = QPushButton()
        self.B9 = QPushButton()

        self.layout.addWidget(self.B1, 0, 0)
        self.layout.addWidget(self.B2, 0, 1)
        self.layout.addWidget(self.B3, 0, 2)
        self.layout.addWidget(self.B4, 1, 0)
        self.layout.addWidget(self.B5, 1, 1)
        self.layout.addWidget(self.B6, 1, 2)
        self.layout.addWidget(self.B7, 2, 0)
        self.layout.addWidget(self.B8, 2, 1)
        self.layout.addWidget(self.B9, 2, 2)

        self.setLayout(self.layout)