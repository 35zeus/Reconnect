from main_window import MainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

class SplashPage(MainWindow):
    def __init__(self):
        super().__init__()
        background = QLabel(self)
        background.setPixmap(QPixmap("./Resources/Splash Page.jpg"))
        self.setCentralWidget(background)