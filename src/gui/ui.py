from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from gui.dialogs import *


class Ui_MainWindow(QMainWindow):

    def __init__(self) -> None:
        super(Ui_MainWindow, self).__init__()


    def setupUi(self, MainWindow):
        # TODO Here paste the design
        dialog = AddCategoryDialog()
        print("Setup ui...")