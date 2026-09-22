import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLabel)

#Set up the window
class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AWhackAMoleGame")
        # Window size
        self.setFixedSize(400, 400)

        # Game state variables
        self.score = 0
        self.time_left = 0

        # Central widget
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #72E04E;")
        self.setCentralWidget(central_widget)

        # Header and Grid
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Header sset-up
        header_bar = QWidget()
        header_bar.setStyleSheet("background-color: #E2FA75; font-weight: bold;")
        header_layout = QHBoxLayout()
        header_bar.setLayout(header_layout)

        self.timer_label = QLabel(f"Timer: {self.time_left}s")
        self.score_label = QLabel(f"Score: {self.score}")

        self.pause_btn = QPushButton("Pause")
        self.quit_btn = QPushButton("Quit")
        self.quit_btn.clicked.connect(self.close)

        header_layout.addWidget(self.timer_label)
        header_layout.addWidget(self.score_label)
        header_layout.addStretch()
        header_layout.addWidget(self.pause_btn)
        header_layout.addWidget(self.quit_btn)

        main_layout.addWidget(header_bar)

        grid_layout = QGridLayout()
        self.buttons = []

        # Grid setup
        for row in range(4):
            row_buttons = []
            for col in range(4):
                button = QPushButton()
                button.setFixedSize(80, 80)
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #8B4513;
                        border-radius: 40px;
                        border: 3px solid #5c2e0b;
                    }
                """)
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=col: self.button_clicked(r, c))
            
            self.buttons.append(row_buttons)

        main_layout.addLayout(grid_layout)

    def button_clicked(self, row, col):
        print(f"button {row}, {col}")

app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())