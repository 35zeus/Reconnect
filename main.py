from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from home_page import HomePage
from profile_page import ProfilePage
from splash_page import SplashPage
from onboarding_1 import Onboarding1
from exercise_widget import Exercise
import sys

app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# home = HomePage()
# home.show()
# profile = ProfilePage()
# profile.show()
# splash = SplashPage()
# splash.show()
onboard_1 = Onboarding1()
onboard_1.show()
# exercise = Exercise()
# exercise.show()
app.exec()

