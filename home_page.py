from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QWidget, QLabel, QPushButton

from main_window import MainWindow
name = "Edith"


class HomePage(MainWindow):
    def __init__(self):
        super().__init__()
        self.footer()

        welcome_label = QLabel(f"Hello, {name}!", self)
        welcome_label.resize(320, 54)
        welcome_label.move(16, 30)
        welcome_label.setStyleSheet("font-family: Poppins;font-size: 20px;font-weight: 400;"
                                    "line-height: 30px;letter-spacing: 0em;text-align: left;")
        fact_labels = QLabel(self)
        fact_labels.resize(320, 107)
        fact_labels.setPixmap(QPixmap("./Resources/top 2 widgets.jpg"))
        fact_labels.move(0, 84)

        exercise_button = QPushButton(self)
        exercise_button.setIcon(QIcon("./Resources/exercise.jpg"))
        exercise_button.move(0, 201)

        interaction_button = QPushButton(self)
        interaction_button.setIcon(QIcon("./Resources/interaction.jpg"))
        interaction_button.move(0, 347)

        meditate_button = QPushButton(self)
        meditate_button.setIcon(QIcon("./Resources/meditate.jpg"))
        meditate_button.move(0, 493)

        home_page_buttons = [exercise_button, interaction_button, meditate_button]
        for button in home_page_buttons:
            button.resize(320, 136)
            button.setIconSize(QSize(296, 136))
            button.setStyleSheet("border:none")
