from main_window import MainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
)

first_name = "Edith"
last_name = "Law"
badge = "Junior Adventurer"
points = 28
tenth_hour = 0
hour = 1

class ProfilePage(MainWindow):
    def __init__(self):
        super().__init__()
        self.footer()

        profile_picture = QLabel(self)
        profile_picture.setPixmap(QPixmap("./Resources/avatar frame.jpg"))
        profile_picture.resize(80, 80)
        profile_picture.move(16, 16)

        name = QLabel(f"{first_name} {last_name}", self)
        name.setStyleSheet("font-family: Poppins;font-size: 20px;font-weight: 400;"
                           "line-height: 24px;letter-spacing: 0em;text-align: center;")
        name.move(116, 32)

        game_data = QLabel(f"{badge} {points} pts", self)
        game_data.setStyleSheet("font-family: Poppins;font-size: 12px;font-weight: 400;"
                                "letter-spacing: 0em;")
        game_data.resize(144, 24)
        game_data.move(116, 56)

        tenth_hour_box = QLabel(f"{tenth_hour}", self)
        tenth_hour_box.resize(50, 63)
        tenth_hour_box.setAlignment(Qt.AlignCenter)
        tenth_hour_box.setStyleSheet("border:2px solid #6323FA;font-size:24px;")
        tenth_hour_box.move(56, 128)

        hour_box = QLabel(f"{hour}", self)
        hour_box.resize(50, 63)
        hour_box.setAlignment(Qt.AlignCenter)
        hour_box.setStyleSheet("border:2px solid #6323FA;font-size:24px;")
        hour_box.move(114, 128)

        hour_saved = QLabel("hours saved", self)
        hour_saved.resize(99, 24)
        hour_saved.setStyleSheet("font-size:16px")
        hour_saved.move(114+50+8, 31+116)

        activities_label = QLabel(self)
        activities_label.setPixmap(QPixmap("./Resources/this_weeks_activities.jpg"))
        activities_label.resize(320, 282)
        activities_label.move(12, 232)




