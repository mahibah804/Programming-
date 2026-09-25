import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox)
from PyQt6.QtCore import QTimer
#Set up the window
class MyFirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AWhackAMoleGame")
        # Window size
        self.setFixedSize(500, 500)

        # Game state variables
        self.score = 0
        self.time_left = 50
        self.mole_row = -1
        self.mole_col = -1

        # Central widget
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: #72E04E;")
        self.setCentralWidget(central_widget)

        # Header and Grid
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Header set-up
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
                         color: white;
                        font-weight: bold;
                        font-size: 14px;
                    }
                """)
                grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
                button.clicked.connect(lambda clicked, r=row, c=col: self.button_clicked(r, c))
            
            self.buttons.append(row_buttons)

        main_layout.addLayout(grid_layout)
        
        # Game timer
        self.game_timer = QTimer()
        self.game_timer.timeout.connect(self.update_timer)
        self.game_timer.start(1000)

        # Spawn initial mole
        self.spawn_mole()

    def spawn_mole(self):
        # Clear previous mole position text
        if self.mole_row != -1 and self.mole_col != -1:
            self.buttons[self.mole_row][self.mole_col].setText("")

        # Random Placement
        self.mole_row = random.randint(0, 3)
        self.mole_col = random.randint(0, 3)
        self.buttons[self.mole_row][self.mole_col].setText("Mole")

        # Timer logic function
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.setText(f"Timer: {self.time_left}s")
        else:
            self.game_timer.stop()
            self.timer_label.setText("Time's Up!")
            for row in self.buttons:
                for button in row:
                    button.setEnabled(False)

            # Save score
            self.save_score()

            #  Play Again or Exit
            self.show_game_over_prompt()

    def button_clicked(self, row, col):
      # Check if the player clicked the mole
        if row == self.mole_row and col == self.mole_col and self.time_left > 0:
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")
            self.spawn_mole()

    def save_score(self):
        # Append final score 
        with open("score.txt", "a") as file:
            file.write(f"Final Score: {self.score}\n")

    def show_game_over_prompt(self):
        reply = QMessageBox.question(
            self, "Game Over", 
            f"Game Over! Your final score is {self.score}.\nWould you like to play again?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.reset_game()
        else:
            self.close()

    def reset_game(self):
        self.score = 0
        self.time_left = 50
        self.score_label.setText(f"Score: {self.score}")
        self.timer_label.setText(f"Timer: {self.time_left}s")
        
        # Re-enable grid buttons
        for row in self.buttons:
            for button in row:
                button.setEnabled(True)

        self.spawn_mole()
        self.game_timer.start(1000)   


app = QApplication(sys.argv)
window = MyFirstWindow()
window.show()
sys.exit(app.exec())
