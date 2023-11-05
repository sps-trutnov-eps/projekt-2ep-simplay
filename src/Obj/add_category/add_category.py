from Custom_Widgets import *

class AddCategory():  
    def __init__(self):
        pass

    def insertTab(self):
        self.tabWidget.addTab(QWidget(), "Jméno hry")

    def removeTab(self):
        self.tabWidget.removeTab(0)