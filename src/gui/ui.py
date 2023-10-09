from Custom_Widgets.Widgets import *

from gui.views import *


class Ui_MainWindow(object):

    def __init__(self, MainWindow) -> None:
        self.MainWindow = MainWindow

        self.setupAddCategoryView()

        
    def setupHomeView(self) -> None:
        self.HomeView = HomeView()
        self.HomeView.setupUi(self.MainWindow)

    def setupAddCategoryView(self) -> None: 
        self.AddCategoryView = AddCategoryView()
        self.AddCategoryView.setupUi(self.MainWindow)