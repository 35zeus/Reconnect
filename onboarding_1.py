from main_window import MainWindow
from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QLabel

class Onboarding1(MainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#F3EEFF")

        continue_button = QPushButton("Continue", self)
        continue_button.setStyleSheet("border:2px solid white; border-radius:20px; "
                                      "background-color:white; color:#6323FA; font-size:16px")
        continue_button.resize(240, 40)
        continue_button.move(40, 637)

        # copy = QLabel("Reconnect with real life", self)
        # copy.setStyleSheet("font-size:24px;color:#6323FA;font-weight:600;text-align:center")
        # copy.resize(288, 36)
        # copy.move(32, 100)
        copy = QLabel(self)
        copy.setPixmap(QPixmap("./Resources/onboard1_copy.jpg"))
        copy.resize(288, 144)
        copy.move(16, 100)


        image = QLabel(self)
        image.setPixmap(QPixmap("./Resources/meditation-image.jpg"))
        image.resize(288, 269)
        image.move(16, 300)
