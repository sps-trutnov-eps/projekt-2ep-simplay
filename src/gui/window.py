from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

from Custom_Widgets.Widgets import *
from gui.ui_interface import *
from PySide2 import *

from gui.qss import *



class Window(QMainWindow):
    
    def __init__(self) -> None:
        super(Window, self).__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setMinimumSize(600, 400)
        #self.init_gui()
        #self.setStyleSheet()
        self.show()

    
    def init_gui(self):
        pass