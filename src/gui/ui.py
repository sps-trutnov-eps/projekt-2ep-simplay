from Custom_Widgets.Widgets import *
from qtpy.QtCore import *
import os

from gui.views import *
from obj.game import *


class Ui_MainWindow(object):

    def __init__(self, MainWindow) -> None:
        self.MainWindow = MainWindow

        self.setupHomeView()

        
    def setupHomeView(self) -> None:
        self.HomeView = HomeView()
        self.HomeView.setupUi(self.MainWindow)

        self.game_manager = GameManager()

        
        self.HomeView.addGameBtn.clicked.connect(self.addGame)

    def setupAddCategoryView(self) -> None: 
        self.AddCategoryView = AddCategoryView()
        self.AddCategoryView.setupUi(self.MainWindow)

    def setupSetPasswordView(self) -> None:
        self.SetPasswordView = SetPasswordView()
        self.SetPasswordView.setupUi(self.MainWindow)

    def setupPlayedTimeView(self) -> None:
        self.PlayedTimeView = PlayedTimeView()
        self.PlayedTimeView.setupUi(self.MainWindow)

    
    def addGame(self) -> None:
        path = QFileDialog.getOpenFileUrl()
        if (type(path) == str):
            name = os.path.basename(path)
            self.game_manager.addGame(name, path)
