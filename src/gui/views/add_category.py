from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from gui.components import NavigationBar


class AddCategoryView(QWidget):

    def __init__(self, parent = None) -> None:
        super(AddCategoryDialog, self).__init__(parent)

        self.setupUi()


    def setupUi(self):
        central_layout = QVBoxLayout(self)
        central_layout.setContentsMargins(QMargins(0, 0, 0, 0))

        navbar = NavigationBar(central_layout)
        central_layout.addStretch(1)