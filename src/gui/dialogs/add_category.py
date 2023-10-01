from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from gui.navigation_bar import NavigationBar


class AddCategoryDialog(QWidget):

    def __init__(self) -> None:
        super(AddCategoryDialog, self).__init__()

        self.setMinimumHeight(200)
        self.setMinimumWidth(300)
        self.initUi()
        self.show()


    def initUi(self):
        central_layout = QVBoxLayout(self)
        central_layout.setContentsMargins(QMargins(0, 0, 0, 0))

        navbar = NavigationBar(central_layout)
        central_layout.addStretch(1)