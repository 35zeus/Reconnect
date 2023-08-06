from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    )

from main_window import MainWindow

WINDOW_HEIGHT = 693
WINDOW_WIDTH = 320
LABEL_HEIGHT = 40
LABEL_WIDTH = 119

class Exercise(MainWindow):
    def __init__(self):
        super().__init__()
        self.footer()
        exercise = QLabel(self)
        exercise.setPixmap(QPixmap("./Resources/exercisetop.jpg"))
        exercise.move(0, 16)
        exercise.resize(320, 104)

        nature_button = QPushButton(self)
        nature_button.setIcon(QIcon("./Resources/walknature.jpg"))
        nature_button.setIconSize(QSize(296, 148))
        nature_button.move(12, 136)
        nature_button.resize(296, 148)

        workout_button = QPushButton(self)
        workout_button.setIcon(QIcon("./Resources/quickworkout.jpg"))
        workout_button.setIconSize(QSize(296, 148))
        workout_button.move(12, 300)
        workout_button.resize(296, 148)

        stretch_button = QPushButton(self)
        stretch_button.setIcon(QIcon("./Resources/stretchbody.jpg"))
        stretch_button.setIconSize(QSize(296, 149))
        stretch_button.move(12, 464)
        stretch_button.resize(296, 149)