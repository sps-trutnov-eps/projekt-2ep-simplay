from Custom_Widgets import *

from gui.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow(self)

        loadJsonStyle(self, self.ui, jsonFiles = {
            "gui/style.json"
        })

        self.show()

        #self.insert.clicked.connect(self.insertTab)
        #self.remove.clicked.connect(self.removeTab)

    def insertTab(self):
        self.tabWidget.addTab(QWidget(), "Jméno hry")

    def removeTab(self):
        self.tabWidget.removeTab(0)