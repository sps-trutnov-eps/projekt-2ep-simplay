from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from gui.views import *


class Ui_MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupHomeView()
        loadJsonStyle(self, self.ui)
        
    def setupHomeView(self):
        self.HomeView = HomeView(self)
        self.show()