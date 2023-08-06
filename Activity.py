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



class ActivityScreen(MainWindow):
    def __init__(self):
        super().__init__()

        activity_screen = QLabel(self)
        activity_screen.resize(320,585)
        activity_screen.setPixmap(QPixmap("./Resources/middle content.jpg"))
        self.setCentralWidget(activity_screen)

    def footer(self):
        #creates buttons
        home_button = QPushButton(self)
        home_button.setIcon(QIcon("./Resources/Icon.jpg"))
        stat_button = QPushButton(self)
        stat_button.setIcon(QIcon("./Resources/bar-chart-10.jpg"))
        profile_button = QPushButton(self)
        profile_button.setIcon(QIcon("./Resources/user-02.jpg"))
        home_bar = [home_button, stat_button, profile_button]

        #locates and stylizes buttons
        for button in home_bar:
            button.resize(24, 24)
            button.setStyleSheet("border:none; margin:20px")
        home_button.move(10, WINDOW_HEIGHT - 34)
        stat_button.move(int(WINDOW_WIDTH/2) - 12, WINDOW_HEIGHT - 34)
        profile_button.move(WINDOW_WIDTH - 34, WINDOW_HEIGHT-34)