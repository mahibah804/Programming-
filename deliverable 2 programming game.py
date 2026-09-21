import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
#Set up the window
class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AWhackAMoleGame")
        # Window size
        self.setFixedSize(500, 500)

        # Central widget
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #72E04E;")
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        self.buttons = []

        # Grid setup
        for row in range(4):
            row_buttons = []
            for col in range(4):
                button = QPushButton()
                button.setFixedSize(80, 80)
                   
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=col: self.button_clicked(r, c))
           
            self.buttons.append(row_buttons)

        central_widget.setLayout(grid_layout)

    def button_clicked(self, row, col):
        print(f"button {row}, {col}")

app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())
