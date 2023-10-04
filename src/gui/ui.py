from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from gui.views import *


class Ui_MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()

        self.setupHomeView()


    def setupHomeView(self):
        self.HomeView = HomeView(self)
        self.show()